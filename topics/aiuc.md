---
type: topic
title: "AIUC（Artificial Intelligence Underwriting Company）"
slug: aiuc
created: 2026-09-20
updated: 2026-09-20
tags: [safety, evaluation]
level: beginner
audience: [engineer, business, instructor]
related: [topics/metr.md, threads/ai-safety-regulation.md]
---

# AIUC（Artificial Intelligence Underwriting Company）

## 一言で
AIエージェントの安全性・信頼性を独立監査した上で保険を引き受ける米国のスタートアップ。「監査＋保険」を組み合わせ、企業がAIエージェントを安心して導入できる基盤（confidence infrastructure）を目指す。

## 仕組み
- サンフランシスコ拠点。元Anthropic社員のRune Kvist氏と元METR COOのRajiv Dattani氏が創業（出典: [TechCrunch — Early Anthropic hire, former METR COO have found a way to rein in rogue AI agents](https://techcrunch.com/2026/09/15/early-anthropic-hire-former-metr-coo-have-found-a-way-to-rein-in-rogue-ai-agents/)、取得日 2026-09-16）
- サイバーセキュリティ分野のSOC 2に相当する基準「AIUC-1」を策定。データ・プライバシー、セキュリティ、安全性、信頼性、説明責任、社会的リスクの6分野にまたがり、250人以上のセキュリティ・リスク専門家およびCursor・ElevenLabs・Harveyなど主要AI企業と共同で開発、四半期ごとに更新される（出典: [AIUC公式サイト](https://aiuc.com/)、取得日 2026-09-20）
- 約5,000項目のテスト（脱獄・幻覚・データ漏えいなど）を実施し、約100ページの監査報告書を作成。監査に合格した企業には保険を提供する仕組みで、電気製品の安全規格を作ったUL（Underwriters Laboratories）の「規格＋認証＋保険」モデルを踏襲している
- 2026年9月、Ribbit Capital主導のシリーズAで4,000万ドルを調達（シード1,500万ドルと合わせ累計5,500万ドル）。KPMGが四大会計事務所として初めてAIUC-1認証を取得、ElevenLabsは同標準に裏付けられた「初のAIエージェント保険」を獲得したという

## 実務での使い方
- 「ベンダーの自己申告を鵜呑みにしない」ための第三者認証として、AIエージェント導入時の説明責任・リスク管理の材料になる
- METRのような非営利の評価機関に加え、保険という金銭的インセンティブを組み込んだ商用の認証サービスが登場している点が、導入企業のリスク移転（保険でカバーする）の選択肢として参考になる

## 講座で使うなら
- 30 秒説明: 「AIエージェントの安全性を審査した上で保険をかける会社です。電気製品の安全規格・保険と同じ発想をAIエージェントに当てはめています」
- たとえ話: 電化製品の「PSEマーク」のような安全規格＋保険をAIエージェントにも用意する動き
- 演習案: 自社でAIエージェントを導入する際、「監査（規格適合の確認）」と「保険（万一の際の補償）」のどちらをより重視するか、受講者に議論させる

## この話題の流れ
<!-- agent が日付順に追記。新しいものを上に -->
- 2026-09-16: 元METR COOのRajiv Dattani氏と元Anthropic社員Rune Kvist氏が創業した「AIUC」が、シリーズA 4,000万ドルを調達（累計5,500万ドル）。Cursor・Lovable・Harveyなどが導入済み（[daily](../daily/2026-09-16.md) / [topics/metr](metr.md) / [threads/ai-safety-regulation](../threads/ai-safety-regulation.md)）

## 関連
- [topics/metr](metr.md)
- [threads/ai-safety-regulation](../threads/ai-safety-regulation.md)
