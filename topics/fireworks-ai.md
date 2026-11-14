---
type: topic
title: "Fireworks AI"
slug: fireworks-ai
created: 2026-11-15
updated: 2026-11-15
tags: [privacy]
level: beginner
audience: [engineer, business, instructor]
related: [topics/hugging-face.md, threads/ai-safety-regulation.md]
---

# Fireworks AI

## 一言で
企業がAI機能を手軽に組み込めるよう、モデルの実行・推論処理を裏側で請け負う「AI基盤企業」の一社。NotionなどのSaaSベンダーが委託先として利用している。

## 仕組み
- 自社でモデルを開発・運用するコストを避けたい企業（Notionなど）に対し、モデルの推論処理をクラウド経由で提供する「委託先」として機能する
- 利用企業のサービス（例: Notionの「Insights」機能）の裏側で動くため、利用者本人からは「どの会社のAPIが使われているか」が見えにくい

## 実務での使い方
- AI機能を外部委託する際、自社が直接契約していない「委託先の委託先」まで把握できているかを確認する必要がある（サプライチェーンリスク）
- 2026年10月・11月と2カ月連続でセキュリティ侵害が報じられており、委託先選定時にはインシデント対応・情報開示の実績も確認材料になる

## 講座で使うなら
- 30 秒説明: 「AI機能を使うサービスの裏側で、実際にモデルを動かしている“下請け”のような会社の一つ」
- たとえ話: 店舗（Notion）が注文を受けて、実際の調理（推論処理）は裏の厨房（Fireworks AI）に委託している構図
- 演習案: 受講者が普段使うAIツールについて「裏側のモデル提供元まで把握しているか」を書き出させる

## この話題の流れ
<!-- agent が日付順に追記。新しいものを上に -->
- 2026-11-12: 委託先Fireworks AIへの不正アクセスにより、Notionの「Insights」機能のAIチャット記録が漏えいした恐れがあると発表（全ワークスペースの1%未満が対象）（[daily](../daily/2026-11-12.md) / [出典](https://www.itmedia.co.jp/aiplus/article/2611/11/2000003104/)）
- 2026-11-12: 国内でもSecureNavi・LRM・フェイガーの3社がNotion経由の情報漏えいの恐れを発表。Fireworksにとっては10月に続き2カ月連続の侵害（[daily](../daily/2026-11-13.md) / [出典](https://www.itmedia.co.jp/aiplus/article/2611/12/2000003140/)）
- 2026-11-10: Hugging Face政策責任者が、AI基盤企業Fireworksでの顧客データ・モデル重みへの不正アクセスをオープンソースAIへの逆風の一例として挙げる（[daily](../daily/2026-11-10.md) / [出典](https://techcrunch.com/2026/11/10/cyberattacks-threaten-to-make-open-source-ai-a-little-less-open-hugging-face-exec-warns/)）

## 関連
- [topics/hugging-face](hugging-face.md)
- [threads/ai-safety-regulation](../threads/ai-safety-regulation.md)
