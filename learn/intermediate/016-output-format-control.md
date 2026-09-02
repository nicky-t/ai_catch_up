---
type: learn
track: intermediate
number: 016
title: "出力フォーマット制御：JSON・構造化出力・スキーマ指定"
date: 2026-09-03
level: intermediate
audience: [engineer, business]
tags: [prompt-engineering, tool-use]
reading_minutes: 4
sources:
  - url: https://developers.openai.com/api/docs/guides/structured-outputs
    title: "OpenAI — Structured outputs"
    fetched: 2026-09-03
  - url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview
    title: "Anthropic — Tool use with Claude"
    fetched: 2026-09-03
related: []
---

# 016 出力フォーマット制御：JSON・構造化出力・スキーマ指定

!!! abstract "この記事で説明できるようになること"
    - 「プロンプトでJSONを頼む」出力と「構造が保証された」出力の違いを説明できる
    - OpenAIのStructured OutputsとClaudeのツール利用（tool use）が、それぞれどう構造を保証しているか比較できる
    - スキーマ指定が守るのは「形式」であって「内容の正しさ」ではない、という落とし穴を説明できる

## 仕組み

出力フォーマットを制御する方法には、保証の強さが異なる3段階がある。

1. **プロンプトでJSONを依頼するだけ**：「JSON形式で返して」と頼む方法。モデルが指示に従わなかったり、キー名が揺れたり、前後に余計な説明文が付いたりする。パース失敗時のリトライ処理が前提になる
2. **JSONモード**：「有効なJSONであること」だけを保証する。中身がどんなキー・構造になるかまでは保証しない
3. **スキーマ指定の構造化出力**：JSON Schema（キー名・型・必須項目など）そのものをAPI呼び出し時に渡し、モデルの出力をそのスキーマに沿うよう制約する

OpenAIのStructured Outputsは、リクエストで `type: "json_schema"` と `strict: true` を指定すると、レスポンスがスキーマに厳密に一致することを保証する。安全性を理由にモデルが回答を拒否した場合も、専用の `refusal` フィールドで拒否を検知できるため、スキーマ違反と拒否を区別できる（出典: OpenAI Structured Outputs ガイド、取得日 2026-09-03）。

Claudeは「ツール利用（tool use）」という仕組みで同等のことを行う。呼び出したい関数の名前・説明・`input_schema`（JSON Schema）を定義して渡すと、Claudeはその関数を呼ぶべきだと判断した際に、スキーマに沿った引数を含む `tool_use` ブロックを返す。カスタムツール定義に `strict: true` を付けると、Claudeのツール呼び出しがスキーマと厳密に一致することを保証できる（出典: Anthropic Tool use ドキュメント、取得日 2026-09-03）。「データ抽出専用の関数」を定義してClaudeに呼ばせる使い方をすれば、会話用の応答ではなく構造化データの取得だけを目的にできる。

## 比較・判断基準

| 方法 | 構造の保証 | 向いている場面 |
|---|---|---|
| プロンプトでJSONを依頼 | なし（リトライ前提） | 試作・低頻度の一回限りの処理 |
| JSONモード | 「有効なJSON」であることのみ | キー構造が多少ブレても後続処理で吸収できる場合 |
| Structured Outputs（OpenAI, strict） | スキーマに厳密一致 | 後続システムにそのまま連携する本番パイプライン |
| ツール利用 + strict（Claude） | スキーマに厳密一致 | 会話応答と切り離してデータ抽出だけをさせたい場合、複数の関数呼び出しを組み合わせたい場合 |

## 落とし穴

1. **max_tokensで途中で切れる**：スキーマを厳密に守らせていても、出力トークンの上限に達すると、有効なJSONとして閉じる前に応答が打ち切られる。OpenAIのガイドも「トークン上限に達すると不完全な応答になりうる」と明記している。長い配列を含むスキーマでは十分な `max_tokens` を確保する
2. **形式は保証されても内容は保証されない**：スキーマは「このキーにこの型の値が入る」ことを保証するだけで、値そのものが正しい（事実に基づく）ことは保証しない。OpenAIのガイドも「ユーザー入力がスキーマと無関係な場合、幻覚を防げない」「制約下でも誤りを含みうる」と注意している。抽出した数値・固有名詞は別途ファクトチェックする工程を挟む
3. **ツール定義自体がトークンコストを増やす**：Claudeでは、ツールを1つでも定義すると、その分の「ツール利用システムプロンプト」トークンが呼び出しごとに加算される（例：Claude Opus 5でtool_choice `auto`／`none` 時286トークン、`any`／`tool` 時406トークン）。多数のツール・複雑なスキーマを常時定義していると、地味にコストがかさむ

## 実務への接続

- 見積書・請求書などの文書から特定項目を抽出し、そのまま社内システムのデータベースに投入する、といった「後続処理が構造に依存する」業務ほど構造化出力の恩恵が大きい
- 「パースに失敗したらリトライ」というエラー処理コードを、スキーマ保証によって大幅に削減できる
- 抽出後の値については、金額・日付・固有名詞など重要な項目だけ人がダブルチェックする運用にすると、落とし穴2の対策になる

## 講座で使うなら

- 30 秒説明: 「AIに『JSON形式で』と頼むのはお願いベースですが、スキーマを渡す構造化出力は『この型でしか返せない』という規格を最初から強制する方法です」
- たとえ話: 自由記述のアンケート用紙（プロンプトでJSON依頼）と、記入欄が決まったマークシート（スキーマ指定の構造化出力）の違い。マークシートは形式のミスは防げるが、書いた内容が正しいかは別問題
- 演習案: 名刺の情報（会社名・氏名・電話番号）を抽出するスキーマを受講者に設計させ、わざと存在しない項目を含む入力を与えて「スキーマは守られるが中身は誤り」というケースを体験させる

## 出典・参考
- [OpenAI — Structured outputs](https://developers.openai.com/api/docs/guides/structured-outputs)（取得日 2026-09-03）
- [Anthropic — Tool use with Claude](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)（取得日 2026-09-03）

## 関連
- [learn/intermediate/013-prompt-structure-5-elements](013-prompt-structure-5-elements.md)
