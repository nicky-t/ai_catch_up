---
type: topic
title: "Microsoft（マイクロソフト）"
slug: microsoft
created: 2026-09-06
updated: 2026-09-15
tags: [microsoft, guardrails, prompt-engineering, safety]
level: beginner
audience: [engineer, business, instructor]
related: [topics/openai.md, topics/claude-code.md, topics/prompt-injection.md]
---

# Microsoft（マイクロソフト）

## 一言で
Windows・Office・Azure・GitHubなどを展開する米国のテクノロジー企業。OpenAIとの提携でCopilotブランド（Microsoft 365 Copilot、GitHub Copilotなど）の製品群にAIを組み込む一方、自社開発モデル「MAI」やサイバー防御ツール「Perception」も進める。

## 仕組み
- 「Microsoft 365 Copilot」はWord・Excel・Teamsなど既存のOffice製品に統合されたAIアシスタント。ドキュメントを読み込んで要約・生成・返信案作成などを行う
- 「GitHub Copilot」は、GitHubがOpenAIと共同開発したコーディング支援ツール。2021年6月29日に技術プレビューとして発表され、GPT-3よりコード生成能力を高めた「OpenAI Codex」を基盤に、行・関数単位のコード補完やテスト作成支援を提供した（[GitHub Blog — Introducing GitHub Copilot](https://github.blog/2021-06-29-introducing-github-copilot-ai-pair-programmer/)、取得日 2026-09-06）
- OpenAIとの提携とは別に、未発表の自社開発モデル「MAI」の存在がコミュニティで憶測されている（[daily 2026-08-24](../daily/2026-08-24.md)）
- AIを悪用したサイバー攻撃への対抗策として、独自の防御ツール「Perception」を投入している（[daily 2026-08-28](../daily/2026-08-28.md)）

## 実務での使い方
- Word・Excelなど外部から受け取った文書をCopilotに読み込ませる前に、白文字など視認しづらい箇所に埋め込まれた指示（間接的プロンプトインジェクション）がないか確認する運用が重要（[topics/prompt-injection](prompt-injection.md)）
- 複数のAIベンダー（OpenAI・Google・自社モデル）を併用する製品構成のため、社内でどのモデルがどの機能に使われているかを棚卸ししておくと、障害・脆弱性発生時の影響範囲を把握しやすい

## 講座で使うなら
- 30 秒説明: 「WordやExcelでおなじみのMicrosoftが、OpenAIとの提携でCopilotというAI機能を組み込んでいる会社です。自社製AIの開発も並行して進めています」
- たとえ話: 使い慣れた文房具（Office）に、外部から借りてきた優秀な助手（OpenAIのモデル）と自社育成の助手（MAI）を両方机に座らせている状態
- 演習案: 受講者に「Word文書をAIに読み込ませる前に確認すべきこと」を3つ挙げさせる

## この話題の流れ
<!-- agent が日付順に追記。新しいものを上に -->
- 2026-09-15: 自社開発AIモデル向けの「行動規範」を発表。サイバー攻撃・核兵器関連・ディープフェイク作成を絶対的な禁止事項とし、「適応的・欺瞞的・自己強化的なメカニズムで人間の監視を回避してはならない」と規定。複数の「制御不能なAIエージェント事件」の発生を受けた対応とみられる（[daily](../daily/2026-09-15.md) / [threads/ai-safety-regulation](../threads/ai-safety-regulation.md)）
- 2026-09-08: Microsoft 365 Copilotが「GPT-6 Astra」（OpenAI、9月4日〜）と「Claude Fable 5.1」（Anthropic、9月1日〜）に対応。前者はCopilot Cowork・Copilot Studioでの大きめタスク処理向け、後者はM365内のファイル・メッセージを文脈参照する「Work IQ」機能と組み合わせて使う（[daily](../daily/2026-09-08.md) / [topics/openai](openai.md) / [topics/anthropic](anthropic.md)）
- 2026-09-08: 福島県庁がM365 Copilotを約6,000人規模に本格展開。試行段階（100アカウント）では効率化実感80%・品質向上実感70%だったが、本格展開後は利用が個人差で二極化。入力ルールの明確化や成功事例の共有で定着を図る（[daily](../daily/2026-09-08.md) / [threads/japan-ai-adoption](../threads/japan-ai-adoption.md)）
- 2026-09-05: ノルウェーの研究者が、Word文書に仕込んだ白文字の指示がMicrosoft Copilotの生成物にコピーされ、社内で自己増殖する新型脅威を報告（7月28日発表の手法をITmediaが改めて紹介）。マクロ実行やシステム侵入を伴わず、通常業務で過去資料を参照しながら新規文書を作るだけで感染しうる点が特徴（[daily](../daily/2026-09-05.md) / [topics/prompt-injection](prompt-injection.md)）
- 2026-08-28: OpenAI・Anthropic・Googleなど100社超の「暴走AI」共同防衛書簡に署名。各社が投入する独自の防御ツールの一つとして「Perception」が紹介された（[daily](../daily/2026-08-28.md)）
- 2026-08-24: OpenRouterに突如登場した匿名モデル「Ox Alpha」の開発元候補として、Microsoftの未発表モデル「MAI」がコミュニティで憶測された（後にZ.aiのGLM系と判明）（[daily](../daily/2026-08-24.md) / [topics/glm](glm.md)）

## 関連
- [topics/openai](openai.md)（Copilotの基盤モデル提携）
- [topics/claude-code](claude-code.md)（コーディングエージェントの競合）
- [topics/prompt-injection](prompt-injection.md)
