---
type: topic
title: "A2A（Agent2Agent Protocol）"
slug: a2a-protocol
created: 2026-08-19
updated: 2026-08-19
tags: [agent, mcp, google]
level: beginner
audience: [engineer, business, instructor]
related: []
---

# A2A（Agent2Agent Protocol）

## 一言で
AI エージェント同士が「自分は何ができるか」を名刺（Agent Card）で示し合い、タスクを依頼・連携するための共通ルール。MCP が「エージェントとツール」の接続規格なら、A2A は「エージェントとエージェント」の接続規格。

## 仕組み
- Google が提案したオープンプロトコル。異なるベンダー・フレームワークのエージェントが互いの能力を発見し、タスクを委譲・連携できる
- 2026 年 3 月の 1.0 でマルチテナンシー、プロトコル交渉、複数プロトコルバインディング、署名付き Agent Card（暗号的な身元確認）が追加
- 2026 年 8 月、ガバナンスが Linux Foundation 配下から Agentic AI Foundation（AAIF）へ移管。AAIF は MCP も擁する中立団体
- 難しさ：連携先エージェントの出力を「検証すべき主張」ではなく「100% 信頼できる入力」として扱ってしまう「伝言ゲーム」のリスク

## 実務での使い方
- 複数ベンダーのエージェントを組み合わせる場合、独自の連携層を作らず A2A + MCP に寄せると将来の差し替えが楽になる
- 導入判断の軸：連携相手の身元確認（署名付き Agent Card）、権限範囲、ログ・監査、前段出力の検証ルール
- 現時点では「標準が固まりつつある段階」。業務適用は小さな連携（例：社内 FAQ エージェント → 申請エージェント）から

## 講座で使うなら
- 30 秒説明: 「MCP がツール接続の USB-C なら、A2A はエージェント同士の名刺交換と依頼状の書式です」
- たとえ話: 社外の専門家に仕事を頼むとき、相手の名刺（できること）を確認し、依頼書の書式を揃えて、納品物は自分で検収する
- 演習案: 「社内の 2 つのエージェントが連携するとき、何を信頼し何を検証するか」を表にまとめる

## この話題の流れ
<!-- agent が日付順に追記。新しいものを上に -->
- 2026-08-19: Google が A2A を Agentic AI Foundation に移管 — MCP と同じ中立団体に「エージェント標準」が集約（[daily](../daily/2026-08-19.md)）
- 2026-08-19: Google / Kaggle のエージェント実践ガイド（無料）が MCP・A2A による相互運用を章立てで扱う（[daily](../daily/2026-08-19.md)）

## 関連
- 今後作成予定: topics/mcp（要追記）
- [learn/intermediate/001](../learn/intermediate/001-transformer-self-attention.md)（個々のモデルが文脈のどこに注目するか）
