---
type: learn
track: intermediate
number: 017
title: "システムプロンプトの設計と運用（バージョン管理・テスト）"
date: 2026-09-04
level: intermediate
audience: [engineer, business]
tags: [prompt-engineering, agent]
reading_minutes: 4
sources:
  - url: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/system-prompts
    title: "System prompts - Claude Platform Docs"
    fetched: 2026-09-04
  - url: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
    title: "Prompting best practices - Claude Platform Docs"
    fetched: 2026-09-04
related: [topics/claude-code.md, topics/openai.md]
---

# 017 システムプロンプトの設計と運用（バージョン管理・テスト）

!!! abstract "この記事で説明できるようになること"
    - システムプロンプトが「ユーザーの指示」と何が違うか、なぜ役割設定に向くか
    - 強い指示語（「CRITICAL: 必ず〜せよ」）がかえって逆効果になりうる理由
    - 本番投入前に何をテストし、更新をどう管理すべきか

## 仕組み

システムプロンプトは、会話の`system`パラメータに渡す特別な指示で、ユーザーの発言よりも優先度が高く扱われる。Anthropicの公式ドキュメントは、たった1文の役割設定でも挙動が変わる例として、`"You are a helpful coding assistant specializing in Python."`のような短い一文を挙げている。ユーザーの発言のたびに前提を書き直す必要がなく、「誰として振る舞うか」を会話全体に効かせられるのがシステムプロンプトの役割である。

構造化の面では、XMLタグでセクションを区切る書き方が推奨されている。例えば「デフォルトで提案だけでなく実行する」という方針を徹底させたい場合、`<default_to_action>`のようなタグで囲んで指示をまとめる書き方が示されている。長い文章の中に指示を埋め込むより、タグで区切ったほうがモデルが指示のまとまりを認識しやすい。

## 比較・判断基準

指示の「強さ」の付け方には落とし穴がある。公式ガイドは、最新モデルほどシステムプロンプトへの反応が敏感になっており、以前のモデル向けに書いた`"CRITICAL: You MUST use this tool when..."`のような強い命令文が、かえってツールの呼び出しすぎ（過剰発火）を招くと指摘する。対策として提示されているのは、"Use this tool when..."のような、より普通の言い回しに戻すことである。つまり「強く言えば言うことを聞く」という直感は、モデル世代が上がるほど成り立たなくなっている。

| 場面 | 向く書き方 |
|---|---|
| 役割・トーンの固定 | 1〜2文の短い役割設定 |
| 複数方針の並立 | XMLタグでセクション分け |
| ツール利用の頻度調整 | 命令の強さより「いつ使うか」の条件を明確化 |

## 落とし穴

1. **強い言葉で「念押し」しすぎる**：上記の通り、最新モデルでは逆効果になりうる。まず普通の指示文で試し、実際に発火不足のときだけ強める。
2. **本番と違う条件でしか試していない**：システムプロンプトの効果は、モデルのバージョンや他の指示との組み合わせで変わる。更新のたびに実際のユーザー入力に近いデータで動作確認しないと、狙った変化が起きているか分からない。
3. **変更履歴を残さない**：システムプロンプトは会話に見えない形で挙動を左右するため、「いつ・何を・なぜ変えたか」を記録していないと、不具合が起きたときに原因を特定できなくなる。プロンプトもコードと同様にバージョン管理し、変更ごとに意図をメモとして残す運用が実務的である。

## 実務への接続

業務でシステムプロンプトを使う場合、①役割・トーン、②守らせたい方針（XMLタグで区分）、③ツール利用の条件、の3層に分けて書くと見通しがよくなる。更新時は「どのモデルバージョン向けに書いたか」を明記し、モデルを切り替えたタイミングで強すぎる指示語が残っていないか点検する。チームで運用する場合は、変更履歴とテスト結果をセットで残すことで、想定外の挙動が起きたときに切り戻しやすくなる。

## 講座で使うなら

- 30 秒説明: 「AIへの『役割説明書』がシステムプロンプトです。書き方次第で、AIが指示を聞きすぎたり聞かなさすぎたりします」
- たとえ話: 新人に渡す「業務マニュアル」。強い言葉で埋め尽くすと逆に萎縮したり過剰反応したりする、というのに近い
- 演習案: 受講者が使っているAIツールのシステムプロンプト（分かる範囲で）や指示文を持ち寄り、「強すぎる命令語」がないか一緒に探させる

## 出典・参考
- [System prompts - Claude Platform Docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/system-prompts)（取得日 2026-09-04）
- [Prompting best practices - Claude Platform Docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)（取得日 2026-09-04）

## 関連
- [topics/claude-code](../../topics/claude-code.md)
- [topics/openai](../../topics/openai.md)
