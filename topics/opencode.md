---
type: topic
title: "OpenCode（オープンコード）"
slug: opencode
created: 2026-10-20
updated: 2026-10-20
tags: [agent, safety, open-weights]
level: beginner
audience: [engineer, business, instructor]
related: [topics/claude-code.md]
---

# OpenCode（オープンコード）

## 一言で
Claude Codeなどと同種の、オープンソースのAIコーディングエージェント（ターミナルで動く自律コーディング支援ツール）。

## 仕組み
CLI・オープンソースのアプリ本体と、利用者がAPIキーなどを管理できるオンラインサービス「OpenCode Console」からなる。OpenAI・Anthropic・GoogleなどのAPIキーを登録して複数のモデルを切り替えて使う設計のため、キーの保存・管理方法がセキュリティ上の論点になる。

## 実務での使い方
Claude CodeやCopilot CLIと同じ「ターミナル常駐型のコーディングエージェント」の選択肢の一つ。GitHub上の人気は高く（スター数20万超）、無料で使える点が導入のハードルを下げる一方、サービス側にAPIキーを預ける運用はリスクも伴う。

## 講座で使うなら
- 30 秒説明: 「Claude Codeと同じ『ターミナルで動くAIコーディングエージェント』のオープンソース版の一つ」
- たとえ話: 複数の鍵（APIキー）を預けられる共用ロッカー——便利だが、ロッカーが破られれば鍵も盗まれる
- 演習案: 自分が使っているAIコーディングツールがAPIキーをどこに・どう保存しているかを確認させる

## この話題の流れ
<!-- agent が日付順に追記。新しいものを上に -->
- 2026-10-20: 利用者向けサービス「OpenCode Console」がハッキングされ、利用者の1.4%が影響を受けたと運営が公表。保存されていたOpenAI・Anthropic・Google宛のAPIキーが悪用され、1,000ドルを超える不正請求を受けた利用者もいた。運営は「大規模な蒸留攻撃」と説明するが、侵入経路やキーの保存方法は未解明（[daily](../daily/2026-10-20.md) / [threads/ai-safety-regulation](../threads/ai-safety-regulation.md) / [出典](https://techcrunch.com/2026/10/19/hackers-hit-ai-coding-tool-opencode-running-up-charges-on-users-ai-accounts/)）

## 関連
- [topics/claude-code](claude-code.md)
