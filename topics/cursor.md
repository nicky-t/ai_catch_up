---
type: topic
title: "Cursor（カーソル）"
slug: cursor
created: 2026-08-19
updated: 2026-08-30
tags: [cursor, agent, tool-use]
level: beginner
audience: [engineer, business, instructor]
related: [topics/claude-code.md]
---

# Cursor（カーソル）

## 一言で
AI を組み込んだコードエディタ（開発元 Anysphere）。チャットで指示するとコードを書き換え、エージェントとして複数ファイルにまたがる作業もこなす。2026 年 8 月には Git ホスティング「Origin」も発表し、エディタから開発基盤へ領域を広げている。

## 仕組み
- VS Code 系のエディタに LLM を統合。補完・チャット編集・エージェント実行を備える。料金は Hobby（無料・エージェント利用に制限）、Individual（$20/月、Pro／Pro+／Ultraの3段階でエージェント利用量が最大20倍まで拡大）、Teams（$40/ユーザー/月、チーム課金・クラウドエージェント）、Enterprise（要問い合わせ、請求書課金・監査ログ）の4段階（出典: [cursor.com/pricing](https://cursor.com/pricing)、取得日 2026-08-30）
- Origin：AI エージェントが大量にアクセスする規模を前提に設計した Git ホスティング。リポジトリ管理・PR の確認とマージ・CLI・Cursor との統合。GitHub リポジトリとの同期可。現在アーリーベータ（Pro / Teams / 企業プラン）
- 背景：GitHub の障害多発とエージェント負荷の増大

## 実務での使い方
- 非エンジニアでも「小さな社内ツールを作る」用途で使われる。Claude Code（ターミナル型）との比較は、GUI で差分を見たいか・自動化を重視するかで分かれる（要追記）
- 開発基盤の選定では、今後「エージェントからのアクセス量に耐えるか」が評価軸になる

## 講座で使うなら
- 30 秒説明: 「AI 付きのコードエディタ。指示すればコードを書き換え、最近はコード置き場（Git ホスティング）まで自前で始めました」
- たとえ話: ワープロに校正者が同居していたのが、いまは印刷所まで自前で持ち始めた
- 演習案: 同じ小さな改修を Cursor と Claude Code で行い、操作感と確認のしやすさを比較する

## この話題の流れ
<!-- agent が日付順に追記。新しいものを上に -->
- 2026-08-29: SpaceXによる約600億ドルでの買収後、OpenAIがモデルAPI提供を11月12日で終了すると通知。Anthropicは提供継続を表明し「より信頼できるパートナー」と位置づけ（[daily](../daily/2026-08-30.md) / [topics/openai](openai.md)）
- 2026-08-19: AI エージェント時代の Git ホスティング「Origin」を発表 — GitHub の障害・エージェント負荷を背景に（[daily](../daily/2026-08-19.md)）

## 関連
- [topics/claude-code](claude-code.md)
