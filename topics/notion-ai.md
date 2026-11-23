---
type: topic
title: "Notion AI"
slug: notion-ai
created: 2026-11-24
updated: 2026-11-24
tags: [notion-ai, privacy]
level: beginner
audience: [engineer, business, instructor]
related: [topics/fireworks-ai.md, threads/ai-safety-regulation.md]
---

# Notion AI

## 一言で
ドキュメント・ノート管理ツール「Notion」に組み込まれたAI機能。文書の自動要約・質問応答（「Insights」機能など）を担うが、裏側の推論処理は委託先企業が担っている。

## 仕組み
- Notion本体に組み込まれた形で提供され、利用者からは裏側でどの企業のAIがどう動いているかが見えにくい
- チャット記録・要約処理の一部は、推論処理を請け負う外部の「AI基盤企業」（Fireworks AIなど）に委託されている（[topics/fireworks-ai](fireworks-ai.md)）
- 2026年10月以降、委託先Fireworks AIが2カ月連続でセキュリティ侵害を受け、Notion AI経由のチャット記録漏えいが複数回にわたって報じられている

## 実務での使い方
- 業務でNotion AIを使う企業は、Notion自体との契約だけでなく「委託先の委託先」まで含めたサプライチェーンリスクを把握しておく必要がある
- 社内の機密情報・顧客情報をNotion AIで扱う際は、委託先のインシデント対応・情報開示の実績も導入判断の材料になる

## 講座で使うなら
- 30 秒説明: 「Notionに組み込まれたAI機能ですが、裏側の推論処理は別の会社に委託されていることがあります」
- たとえ話: 店舗（Notion）が注文を受け、実際の調理（推論処理）は裏の厨房（Fireworks AIなど委託先）が担当している構図
- 演習案: 受講者が普段使うSaaSのAI機能について「裏側のモデル提供元・委託先まで把握しているか」を書き出させる

## この話題の流れ
<!-- agent が日付順に追記。新しいものを上に -->
- 2026-11-23（続報）: メルカリが、業務で使う「Notion AI」のチャット記録の一部が外部に流出した可能性があると公表。委託先Fireworks AIでは10月・11月と2カ月連続でセキュリティ侵害が確認されており、記事では2種類の攻撃が確認されたと説明されている（[daily](../daily/2026-11-24.md) / [topics/fireworks-ai](fireworks-ai.md) / [出典](https://kn.itmedia.co.jp/kn/article/2611/23/2000003393/)）
- 2026-11-12（続報）: 国内でもSecureNavi・LRM・フェイガーの3社がNotion経由の情報漏えいの恐れを発表（[daily](../daily/2026-11-13.md) / [topics/fireworks-ai](fireworks-ai.md) / [出典](https://www.itmedia.co.jp/aiplus/article/2611/12/2000003140/)）
- 2026-11-12: 委託先Fireworks AIへの不正アクセスにより、Notionの「Insights」機能のAIチャット記録が漏えいした恐れがあると発表（全ワークスペースの1%未満が対象）（[daily](../daily/2026-11-12.md) / [topics/fireworks-ai](fireworks-ai.md) / [出典](https://www.itmedia.co.jp/aiplus/article/2611/11/2000003104/)）

## 関連
- [topics/fireworks-ai](fireworks-ai.md)
- [threads/ai-safety-regulation](../threads/ai-safety-regulation.md)
