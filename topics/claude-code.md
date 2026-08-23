---
type: topic
title: "Claude Code（クロードコード）"
slug: claude-code
created: 2026-08-19
updated: 2026-08-24
tags: [claude-code, anthropic, agent]
level: beginner
audience: [engineer, business, instructor]
related: [topics/cursor.md]
---

# Claude Code（クロードコード）

## 一言で
Anthropic のコーディングエージェント。ターミナルやクラウドから自然言語で指示すると、コードの読解・修正・テスト・コミットまでを自律的に進める。本リポジトリの日次生成もこれで動いている。

## 仕組み
- Claude モデルがファイル操作・シェル・Web 取得などのツールを使いながらタスクをループで進める。実行するツールごとに承認を求めるかどうかを決める権限モード（既定では危険な操作は都度確認、`acceptEdits`・`bypassPermissions` などで自動化の度合いを調整）を持つ
- MCP（Model Context Protocol）に対応し、Google Drive の設計資料を読む・Jira のチケットを更新する・Slack からデータを取る、といった外部ツール連携を標準規格で追加できる
- ターミナル・IDE 拡張・デスクトップアプリに加え、ブラウザ上でも実行できる「Claude Code on the web」（claude.ai/code）を提供。ローカルで開始したタスクをクラウドに引き継いだり、複数タスクを並列実行したりできる（出典: [code.claude.com/docs/en/overview](https://code.claude.com/docs/en/overview)、取得日 2026-08-23）
- 料金は Pro / Max / Team / Enterprise などのプランで週次の利用枠がある。2026 年 5 月 13 日〜8 月 31 日は利用枠 50% 増のキャンペーン中

## 実務での使い方
- 非エンジニアでも「定型作業の自動化スクリプト」「ドキュメント整備」に使える。利用枠は流動的なので、チーム導入時はキャンペーン値でなく通常値で見積もる
- Cursor（エディタ型）との比較は [topics/cursor](cursor.md)

## 講座で使うなら
- 30 秒説明: 「チャットで『こう直して』と頼むと、コードを読んで直してテストまでやってくれる Anthropic のエージェントです」
- たとえ話: 口頭で頼める優秀な開発アシスタント。ただし作業量（利用枠）に上限がある
- 演習案: 小さな CSV 集計スクリプトを Claude Code に書かせ、自分でレビューして 1 箇所修正を依頼する

## この話題の流れ
<!-- agent が日付順に追記。新しいものを上に -->
- 2026-08-24: JSランタイム「Bun」v1.4（Zig→Rust移植）のリリース作業にClaude Codeが活用された（[daily](../daily/2026-08-24.md)）
- 2026-08-21: 開発者 Boris Cherny が講演で、システムプロンプトを「アブレーション」で再構築し80%削減できたと紹介（[daily](../daily/2026-08-21.md)）
- 2026-08-19: 週次利用枠「50% 増」を 8 月 31 日まで延長 — 恒久化したいが容量逼迫のため（[daily](../daily/2026-08-19.md)）

## 関連
- [topics/cursor](cursor.md)
- [topics/openai](openai.md)（Codex との競合）
- [topics/mcp](mcp.md)（外部ツール連携の標準）
