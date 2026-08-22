---
type: topic
title: "OpenAI"
slug: openai
created: 2026-08-19
updated: 2026-08-23
tags: [openai, chatgpt, gpt]
level: beginner
audience: [engineer, business, instructor]
related: [threads/japan-ai-adoption.md, topics/openrouter.md]
---

# OpenAI

## 一言で
ChatGPT と GPT 系モデルを開発する米国の AI 企業。一般利用者・企業・開発者（API）向けに製品を展開し、モデル開発の速度と安全性の両面で業界の基準を作ってきた。

## 仕組み
- 製品ライン：ChatGPT（一般・Work・Teens など利用者層別）、API（開発者向け）、Codex（コーディング支援）など（要追記：最新のモデル名・料金体系）
- 安全面では、モデルの能力段階（「Critical」など）に応じて開発ペースや提供条件を調整する方針を明示している（2026-08-18 の発表）
- 国内展開：OpenAI Partner Network を通じて認定パートナーが中堅・中小企業の導入支援を行う（要追記：国内パートナー一覧）

## 実務での使い方
- ChatGPT / API のどれを使うかは「データの扱い（学習利用の有無）」「利用者層」「コスト」で決める（要追記：プラン比較）
- 新モデルのリリース時期は安全評価で前後しうるので、導入計画は特定モデルに依存させない
- 教育・研修用途では ChatGPT for Teens の「Study Mode へ誘導」設計が参考になる

## 講座で使うなら
- 30 秒説明: 「ChatGPT を作っている会社。一般向けアプリから企業向け API まで揃え、安全性の基準づくりでも業界をリードしています」
- たとえ話: 自動車メーカーが市販車（ChatGPT）とエンジン供給（API）の両方をやり、安全基準も自分で決めている
- 演習案: 「ChatGPT に聞く」と「API で業務システムに組み込む」の違いを、データの流れ図で描かせる

## この話題の流れ
<!-- agent が日付順に追記。新しいものを上に -->
- 2026-08-23: カリフォルニア州のAI安全法案「SB 53」の強化を要求。訓練・評価中モデルの監視要件とサイバーセキュリティ強化を提案、7月のHugging Face侵害事件を機に規制支持へ転換（[daily](../daily/2026-08-23.md)）
- 2026-08-20: ゼロデータ保持を維持したまま不正利用を検知する「Private Safety Processing」を発表 — 30 日間のデータ保持を求める Anthropic の方針への対抗策（[daily](../daily/2026-08-20.md)）
- 2026-08-19: 国内パートナー網を拡充、中堅・中小企業の AI 導入を後押し — 1 億 5,000 万ドル投資・認定コンサルタント 30 万人育成計画（[daily](../daily/2026-08-19.md)）
- 2026-08-19: 13〜17 歳向け「ChatGPT for Teens」を発表 — 丸投げ検知で Study Mode へ誘導、年齢別保護（[daily](../daily/2026-08-19.md)）
- 2026-08-19: 次期モデルのサイバー能力を理由にフロンティアモデルの強化学習を一部停止 — 安全対策を強化、「安全性が開発ペースを決める」（[daily](../daily/2026-08-19.md)）

## 関連
- [threads/japan-ai-adoption](../threads/japan-ai-adoption.md)
- [topics/claude-code](claude-code.md)（競合のコーディングエージェント文脈）
