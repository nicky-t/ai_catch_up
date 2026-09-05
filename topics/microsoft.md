---
type: topic
title: "Microsoft（マイクロソフト）"
slug: microsoft
created: 2026-09-06
updated: 2026-09-06
tags: [microsoft, guardrails, prompt-engineering]
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
- 2026-09-05: ノルウェーの研究者が、Word文書に仕込んだ白文字の指示がMicrosoft Copilotの生成物にコピーされ、社内で自己増殖する新型脅威を報告（7月28日発表の手法をITmediaが改めて紹介）。マクロ実行やシステム侵入を伴わず、通常業務で過去資料を参照しながら新規文書を作るだけで感染しうる点が特徴（[daily](../daily/2026-09-05.md) / [topics/prompt-injection](prompt-injection.md)）
- 2026-08-28: OpenAI・Anthropic・Googleなど100社超の「暴走AI」共同防衛書簡に署名。各社が投入する独自の防御ツールの一つとして「Perception」が紹介された（[daily](../daily/2026-08-28.md)）
- 2026-08-24: OpenRouterに突如登場した匿名モデル「Ox Alpha」の開発元候補として、Microsoftの未発表モデル「MAI」がコミュニティで憶測された（後にZ.aiのGLM系と判明）（[daily](../daily/2026-08-24.md) / [topics/glm](glm.md)）

## 関連
- [topics/openai](openai.md)（Copilotの基盤モデル提携）
- [topics/claude-code](claude-code.md)（コーディングエージェントの競合）
- [topics/prompt-injection](prompt-injection.md)
