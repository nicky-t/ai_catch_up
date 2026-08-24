---
type: learn
track: intermediate
number: 007
title: "推論モデル（reasoning models）：思考過程を出すモデルは何が違うか"
date: 2026-08-25
level: intermediate
audience: [engineer, business]
tags: [reasoning, cost]
reading_minutes: 4
sources:
  - url: https://platform.claude.com/docs/en/build-with-claude/extended-thinking
    title: "Anthropic Docs — Extended thinking"
    fetched: 2026-08-25
  - url: https://developers.openai.com/api/docs/guides/reasoning
    title: "OpenAI Docs — Reasoning models"
    fetched: 2026-08-25
related: [topics/anthropic.md, topics/openai.md]
---

# 007 推論モデル（reasoning models）：思考過程を出すモデルは何が違うか

!!! abstract "この記事で説明できるようになること"
    - 推論モデルが「最終回答を書く前に内部で考える」仕組みと、それがトークン数・コストに直結する理由を説明できる
    - Claude の Extended Thinking／OpenAI の `reasoning.effort` など、実務で「思考の深さ」をどう調整するかを判断できる

## 仕組み

推論モデルは、最終的な回答を書く前に「内部推論（reasoning / thinking）」のステップを生成する。学習段階では、強化学習によってこの思考過程を鍛え、間違いに気づいて修正したり、難しい手順を小さく分解したり、うまくいかない方針を切り替えたりする挙動を身につけていく。これは通常のモデルが入力を受けてすぐ出力を組み立てるのとは異なる動き方になる。

各社の実装は共通して「思考トークンは通常の出力トークンと同様に課金・カウントされる」という設計を取る。

- **Anthropic（Claude）**：`thinking` パラメータで `budget_tokens`（最低1,024トークン）を指定すると、Claude はその予算の範囲で思考ブロック（thinking content block）を生成してから最終的なテキストブロックを出力する。思考トークンはコンテキストウィンドウを消費し、出力トークンとして課金される（出典: Anthropic Docs）
- **OpenAI**：推論モデルは入力・出力トークンに加えて「推論トークン」を生成する。推論トークンの中身はAPIからは見えないが、コンテキストウィンドウを占有し出力トークンとして課金される点はAnthropicと同じ。思考の深さは `reasoning.effort` で `none`〜`max` の6段階から選ぶ（出典: OpenAI Docs）

## 比較・判断基準

| 項目 | Anthropic（Claude） | OpenAI |
|---|---|---|
| 制御方法 | `budget_tokens`（トークン数を直接指定）／新しいモデルでは `effort` | `reasoning.effort`（`none`/`low`/`medium`/`high`/`xhigh`/`max` の段階指定） |
| 思考内容の可視性 | 思考ブロックとして応答に含まれる（要約表示の場合あり） | APIからは非表示 |
| 課金 | 思考トークンは出力トークンとして課金 | 同左 |
| コンテキストウィンドウ | 思考トークンが占有（OpenAIは最低25,000トークンの予約を推奨） | 同左 |

トークン数で細かく制御したいか、段階（低〜最高）で大まかに指定したいかが設計思想の違いになる。

## 落とし穴

- 「思考を増やせば無料で精度が上がる」わけではない。思考トークンも課金対象であり、予算・effortを上げるほどコストとレイテンシが増える
- 単純な分類・抽出タスクにまで一律で高い思考深度を設定すると、無駄なコスト増とレスポンス遅延を招く
- 内部の思考過程（chain of thought）は要約表示や非開示の場合があり、「思考の中身がそのまま安全性の説明根拠になる」と過信しない

## 実務への接続

タスクの複雑さに応じて思考の深さを使い分けるのが実務上の基本。定型的な分類・要約は低い設定（Anthropicなら小さめの `budget_tokens`、OpenAIなら `low`/`none`）で十分なことが多く、複雑な多段階のコーディング・分析タスクでは高い設定にコストをかける。実運用ではレスポンスに含まれるトークン内訳（例：Anthropicの `usage.output_tokens_details.thinking_tokens`）を監視し、想定外にコストがかかっていないか確認するとよい。

## 講座で使うなら

- 30秒説明: 「推論モデルは、答えを書く前に下書き（思考）をするAIです。下書きの量を増やすほど賢くなりますが、下書きにも原稿料（トークン課金）がかかります」
- たとえ話: 試験で下書き用紙を渡された生徒が、簡単な問題は即答し、難しい問題だけ下書きに時間をかけて解く姿
- 演習案: 受講者に「自分の業務タスクを1つ選び、下書き（思考）が必要な複雑なタスクか、即答でよい単純なタスクかを分類させる」

## 出典・参考

- [Anthropic Docs — Extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)（取得日 2026-08-25）
- [OpenAI Docs — Reasoning models](https://developers.openai.com/api/docs/guides/reasoning)（取得日 2026-08-25）

## 関連

- [topics/anthropic](../../topics/anthropic.md)
- [topics/openai](../../topics/openai.md)
