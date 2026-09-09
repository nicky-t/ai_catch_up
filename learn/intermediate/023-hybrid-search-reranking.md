---
type: learn
track: intermediate
number: 023
title: "ハイブリッド検索とリランキング"
date: 2026-09-10
level: intermediate
audience: [engineer, business]
tags: [rag]
reading_minutes: 4
sources:
  - url: https://denser.ai/blog/hybrid-search-for-rag/
    title: "Hybrid Search for RAG: Combining BM25 and Dense Vector Search (2026 Guide)"
    fetched: 2026-09-10
  - url: https://www.digitalapplied.com/blog/hybrid-search-bm25-vector-reranking-reference-2026
    title: "Hybrid Search: BM25, Vector & Reranking Reference 2026"
    fetched: 2026-09-10
related: [learn/intermediate/021-rag-overview-pipeline-failure-points.md, learn/intermediate/022-chunking-strategies.md, topics/rag.md]
---

# 023 ハイブリッド検索とリランキング

!!! abstract "この記事で説明できるようになること"
    - キーワード検索（BM25）とベクトル検索を組み合わせる「ハイブリッド検索」がなぜ必要か
    - スコアの異なる2種類の検索結果を統合する Reciprocal Rank Fusion（RRF）の考え方
    - 候補を絞ってから並べ直す「リランキング（リランク）」の役割と、2段階アーキテクチャの全体像

## 仕組み

BM25（キーワード検索）とベクトル検索（意味検索）は、それぞれ異なる種類のクエリで強みを発揮する。BM25は製品コード・エラーコード・人名など「完全一致」が重要なクエリに強く、ベクトル検索は「壊れた商品の返品方法」のような言い換えや概念的なクエリに強い。どちらか一方だけでは、もう一方が得意なクエリで取りこぼしが起きる（出典: [Denser Blog](https://denser.ai/blog/hybrid-search-for-rag/)、取得日 2026-09-10）。

そこでハイブリッド検索は、BM25とベクトル検索を並列に実行し、両方の結果を1つのランキングに統合する。ここで問題になるのが「BM25のスコア」と「ベクトル検索のコサイン類似度」は尺度が異なり、単純な加重平均では統合できないこと。この問題を解決するのが **Reciprocal Rank Fusion（RRF）** で、各手法での「順位（rank）」だけを使い、生スコアには頼らない。

```
score(d) = Σ 1 / (k + rank(d))
```

k は定数（デフォルト60が一般的）で、複数の検索結果リストにまたがって同じ文書の順位の逆数を足し合わせる。順位という共通の物差しに変換することで、スコアの尺度が異なる検索手法同士でも統合できる（出典: 同上）。

## 比較・判断基準

多くの実装ガイドは「ハイブリッド検索→リランキング」の**2段階アーキテクチャ**を標準パターンとして挙げている（出典: [Digital Applied Blog](https://www.digitalapplied.com/blog/hybrid-search-bm25-vector-reranking-reference-2026)、取得日 2026-09-10）。

| 段階 | やること | 候補数の目安 |
|---|---|---|
| ステージ1：ハイブリッド検索 | BM25とベクトル検索を並列実行しRRFで統合。広く候補を集める | 各手法で上位50〜500件を取得 |
| ステージ2：リランキング | 統合結果の上位候補を、クロスエンコーダー（例：Cohere Rerank、Voyage rerank）で1件ずつ深く再評価 | 上位50〜200件を対象に、最終的に5〜10件に絞る |

性能面では、電子商取引データセット（WANDS）でBM25単独・ベクトル検索単独がともにNDCG 0.69台だったのに対し、RRFによるハイブリッド化で0.71前後、フィールドの重み付けなどの調整を加えると0.75まで改善したと報告されている（7.4%の改善）。さらに金融文書ベンチマークでは、ハイブリッド検索にリランキングを組み合わせることでRecall@5が0.587（ベクトル検索単独）から0.816まで向上した（約39%の相対改善）という数値も報告されている（出典: [Denser Blog](https://denser.ai/blog/hybrid-search-for-rag/)、取得日 2026-09-10）。

## 落とし穴

1. **ベクトル検索さえあれば十分と考える**：BM25が得意な「完全一致」クエリ（型番・エラーコードなど）を取りこぼす。BM25の追加は「最も費用対効果の高い検索改善策」と紹介されるほど効果が大きい
2. **統合方法（フュージョン方式）をベンダー任せにする**：検索基盤ごとにデフォルトの統合方式が異なり、あるベクトルDBはバージョンアップでデフォルトの融合方式をRRFから別方式に変更した例もある。デフォルト任せにせず、使う基盤のドキュメントで方式を確認する
3. **候補数を絞りすぎる／広げすぎる**：ステージ1で候補を絞りすぎるとステージ2のリランキングで正解が拾えず、広げすぎるとリランキングのコスト・レイテンシが増える。50〜200件程度を目安に、自分のデータで調整する

## 実務への接続

- 社内文書検索で「型番」「エラーコード」「担当者名」のような完全一致クエリが多い業務では、ベクトル検索だけのRAGはBM25を追加するだけで体感精度が大きく変わりやすい
- リランキングはレイテンシとコストが増える処理なので、候補数の多い一次検索（ステージ1）は安価に広く、リランキング（ステージ2）は少数に絞って高コストな処理を使う、という役割分担を意識する
- チャンキング（学習記事022）で分割の粒度を工夫しても、検索手法自体が弱いと精度は頭打ちになる。「まずチャンキング、次にハイブリッド検索、最後にリランキング」の順で改善すると効果を切り分けやすい

## 講座で使うなら

- 30 秒説明: 「キーワード検索と意味検索を両方使って幅広く候補を集め、そのあと最終候補を1つずつ丁寧に見直して並べ直すのがハイブリッド検索とリランキングです」
- たとえ話: 図書館で「タイトルの一致」で探す係と「内容の近さ」で探す係を両方働かせてから、最後に専門の司書が候補を読んで順位を付け直すイメージ
- 演習案: 受講者が普段使う社内検索・チャットボットで「型番や固有名詞で検索したのに出てこなかった」経験を挙げてもらい、それがBM25（キーワード検索）の弱さで説明できるか議論させる

## 出典・参考
- [Hybrid Search for RAG: Combining BM25 and Dense Vector Search (2026 Guide)](https://denser.ai/blog/hybrid-search-for-rag/)（取得日 2026-09-10）
- [Hybrid Search: BM25, Vector & Reranking Reference 2026](https://www.digitalapplied.com/blog/hybrid-search-bm25-vector-reranking-reference-2026)（取得日 2026-09-10）

## 関連
- [learn/intermediate/021-rag-overview-pipeline-failure-points](021-rag-overview-pipeline-failure-points.md)
- [learn/intermediate/022-chunking-strategies](022-chunking-strategies.md)
