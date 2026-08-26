---
type: learn
track: intermediate
number: 009
title: "埋め込み（embeddings）とベクトル検索：意味の近さをどう測るか"
date: 2026-08-27
level: intermediate
audience: [engineer, business]
tags: [embeddings, rag]
reading_minutes: 4
sources:
  - url: https://developers.openai.com/api/docs/guides/embeddings
    title: "OpenAI Docs — Embeddings"
    fetched: 2026-08-27
  - url: https://platform.claude.com/docs/en/build-with-claude/embeddings
    title: "Anthropic Docs — Embeddings"
    fetched: 2026-08-27
related: [topics/openai.md, topics/anthropic.md]
---

# 009 埋め込み（embeddings）とベクトル検索：意味の近さをどう測るか

!!! abstract "この記事で説明できるようになること"
    - 埋め込み（embeddings）が何を数値化しているのかを説明できる
    - 次元数・類似度計算・料金という 3 つの軸でモデルを比較・選定できる

## 仕組み

埋め込みとは、文章を「意味の近さを測れる」数百〜数千個の数値の列（ベクトル）に変換したものである。意味が近い文章同士はベクトル空間上で近い位置に置かれ、遠い文章は離れた位置に置かれる。これを使うと、キーワードが一致しなくても「意味が近い文書」を検索で見つけられる（RAG の検索ステップの土台になる仕組み）。

- **OpenAI**：`text-embedding-3-small`（デフォルト 1,536 次元）と `text-embedding-3-large`（デフォルト 3,072 次元）の 2 種類を提供。`dimensions` パラメータで次元数を削減でき、性能低下を抑えたまま短いベクトルにできる（例：`text-embedding-3-large` を 256 次元に切り詰めても、旧モデル `text-embedding-ada-002`（1,536 次元）を上回る）。類似度計算にはコサイン類似度を推奨（出典: OpenAI Docs）
- **Anthropic**：自社の埋め込みモデルは提供しておらず、パートナーの Voyage AI を推奨している。最新の `voyage-4` シリーズはデフォルト 1,024 次元（256〜2,048 次元に調整可能）で、コンテキスト長は 32,000 トークン。ベクトルは正規化されているため、コサイン類似度と内積は同じ結果になる（出典: Anthropic Docs）

どちらの提供元も、検索したい対象が「クエリ（質問）」か「ドキュメント（保存する文書）」かで扱いを分ける設計を採る。Voyage AI では `input_type` に `query`/`document` を指定すると、内部で異なるプロンプトが自動的に付加され、検索精度が上がる。

## 比較・判断基準

| 項目 | OpenAI（`text-embedding-3-*`） | Anthropic 推奨（Voyage `voyage-4`） |
|---|---|---|
| 次元数（デフォルト） | small: 1,536 ／ large: 3,072 | 1,024（256〜2,048 に調整可） |
| 次元削減 | `dimensions` パラメータで可能 | 先頭から切り詰め可能（Matryoshka 学習） |
| コンテキスト長 | 8,192 トークン | 32,000 トークン |
| 類似度計算 | コサイン類似度推奨 | コサイン類似度＝内積＝ユークリッド距離の順位（正規化済みのため） |
| 特徴 | 自社 API に統合、価格が明確 | 分野特化モデル（法律・金融・コード）や量子化オプションが豊富 |

次元数が大きいほど表現力は高いがストレージ・検索コストも増える。業務データの規模が小さいうちは小型モデル（`text-embedding-3-small` や `voyage-4-lite`）で十分なことが多く、精度が足りない場合に大型モデルへ切り替える、という順序で検討するとよい。

## 落とし穴

- **埋め込みモデルを混在させない**：検索対象の文書と検索クエリを異なるモデル・異なる次元数で埋め込むと、ベクトル空間がずれて類似度が意味をなさなくなる。同じモデル・同じ設定で統一する
- **`input_type` の指定漏れ**：クエリとドキュメントを区別せずに埋め込むと検索精度が落ちる。Voyage AI のように区別できるモデルでは必ず指定する
- **次元を削っても再学習はできない**：切り詰め（truncation）は「精度を多少犠牲にしてコストを下げる」操作であり、元の次元に戻しても精度は戻らない。削減は保存前に十分検証してから決める

## 実務への接続

社内文書検索（RAG）を作る際、まず埋め込みモデルを 1 つに固定し、次元数を「保存コストと検索精度のバランス」で決めるのが最初の設計判断になる。検索対象の文書量が数千件程度なら小型・低次元モデルで始め、検索結果の精度が業務要件を満たさない場合にのみ大型モデルや次元数を上げる、という段階的な導入が費用対効果に優れる。

## 講座で使うなら

- 30秒説明: 「文章の『意味』を、近い意味の文章ほど近くに並ぶ数字の列に変換する技術です。この数字の列同士の距離を測ることで、キーワードが違っても意味が近い文書を探せます」
- たとえ話: 図書館の本を「タイトルの文字」ではなく「内容の近さ」で棚に並べ替えるようなもの。似た内容の本は自然と隣同士になる
- 演習案: 受講者に「請求書」「見積書」「領収書」という3つの言葉を挙げてもらい、キーワード検索では別物として扱われるが、意味的には近いはずだという例から、埋め込み検索が解決する課題を体感してもらう

## 出典・参考

- [OpenAI Docs — Embeddings](https://developers.openai.com/api/docs/guides/embeddings)（取得日 2026-08-27）
- [Anthropic Docs — Embeddings](https://platform.claude.com/docs/en/build-with-claude/embeddings)（取得日 2026-08-27）

## 関連

- [topics/openai](../../topics/openai.md)
- [topics/anthropic](../../topics/anthropic.md)
