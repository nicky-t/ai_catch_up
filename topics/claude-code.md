---
type: topic
title: "Claude Code（クロードコード）"
slug: claude-code
created: 2026-08-19
updated: 2026-08-21
tags: [claude-code, anthropic, agent]
level: beginner
audience: [engineer, business, instructor]
related: [topics/cursor.md]
---

# Claude Code（クロードコード）

## 一言で
Anthropic のコーディングエージェント。ターミナルやクラウドから自然言語で指示すると、コードの読解・修正・テスト・コミットまでを自律的に進める。本リポジトリの日次生成もこれで動いている。

## 仕組み
- Claude モデルがファイル操作・シェル・Web 取得などのツールを使いながらタスクをループで進める（要追記：権限モデル・MCP 連携・クラウド実行の詳細）
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
- 2026-08-21: 開発者 Boris Cherny が講演で、システムプロンプトを「アブレーション」で再構築し80%削減できたと紹介（[daily](../daily/2026-08-21.md)）
- 2026-08-19: 週次利用枠「50% 増」を 8 月 31 日まで延長 — 恒久化したいが容量逼迫のため（[daily](../daily/2026-08-19.md)）

## 関連
- [topics/cursor](cursor.md)
- [topics/openai](openai.md)（Codex との競合）
