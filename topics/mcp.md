---
type: topic
title: "MCP（Model Context Protocol）"
slug: mcp
created: 2026-08-23
updated: 2026-08-28
tags: [mcp, agent, tool-use]
level: beginner
audience: [engineer, business, instructor]
related: [topics/a2a-protocol.md, topics/claude-code.md]
---

# MCP（Model Context Protocol）

## 一言で
AI アシスタントが外部のデータ源・ツール・業務システムに接続するための共通規格。Anthropic が 2024 年 11 月に発表したオープンプロトコルで、「AI アプリケーションのための USB-C」と説明される。

## 仕組み
- AI アプリケーション（Claude・ChatGPT など）が、ローカルファイルやデータベースといった**データ源**、検索エンジンや計算ツールなどの**ツール**、専用プロンプトなどの**ワークフロー**に接続できるようにする標準。接続先ごとに個別実装する代わりに、MCP に対応したサーバーを 1 つ作れば複数の AI アプリケーションから使い回せる（出典: [modelcontextprotocol.io/introduction](https://modelcontextprotocol.io/introduction)、取得日 2026-08-23）
- 2024 年 11 月 25 日に Anthropic が発表。情報がサイロ化・古いシステムに閉じ込められている問題と、接続先ごとに個別実装が必要な煩雑さの解消を狙った（出典: [anthropic.com/news/model-context-protocol](https://www.anthropic.com/news/model-context-protocol)、取得日 2026-08-23）
- Claude・ChatGPT・VS Code・Cursor・MCPJam など幅広いクライアント・サーバーが対応する「エコシステム」として広がっている
- エージェント同士の連携規格である A2A（Agent2Agent Protocol）とは役割が異なる。「MCP はエージェントとツールの接続」「A2A はエージェントとエージェントの接続」という整理ができる（[topics/a2a-protocol](a2a-protocol.md)）

## 実務での使い方
- CAD（PTC の Onshape 向け FeatureScript MCP Server）のような業務特化ソフトにも広がっており、「自社の業務ソフトが MCP に対応しているか」が AI 統合のしやすさを左右する（[daily 2026-08-20](../daily/2026-08-20.md)）
- 複数ベンダーのエージェントを組み合わせる設計では、独自の連携層を作らず MCP（ツール接続）＋ A2A（エージェント間連携）に寄せると、将来のツール・エージェントの差し替えが楽になる
- Claude Code も MCP に対応しており、Google Drive・Jira・Slack などの外部ツールを標準規格で追加できる（[topics/claude-code](claude-code.md)）

## 講座で使うなら
- 30 秒説明: 「AI が外部のツールやデータにつながるための共通の差し込み口です。USB-C のように、1 回作れば色々な AI アプリで使い回せます」
- たとえ話: 家電ごとに専用の変換プラグを用意する代わりに、USB-C 1 本で何にでもつながる状態
- 演習案: 自分の業務でよく使うツール（カレンダー・チャット・社内システム）を挙げ、「MCP サーバーがあったら AI に何をさせたいか」を書き出させる

## この話題の流れ
<!-- agent が日付順に追記。新しいものを上に -->
- 2026-08-28: Agentic AI Foundationが新ロードマップを公開。エージェント向けメッセージング・HTTP通信への統一・エージェントのアイデンティティ管理などが柱（[daily](../daily/2026-08-28.md)）
- 2026-08-20: PTC が CAD「Onshape」に「FeatureScript MCP Server」を搭載、AI から自然言語でカスタム CAD 機能を生成できるように（[daily](../daily/2026-08-20.md)）
- 2026-08-19: Google が A2A のガバナンスを Agentic AI Foundation（AAIF）へ移管。AAIF は MCP も擁する中立団体となり、「エージェント標準（A2A）」と「ツール標準（MCP）」が同じ団体に揃った（[daily](../daily/2026-08-19.md)）
- 2026-08-19: Google / Kaggle のエージェント実践ガイド（無料公開）が MCP による相互運用を章立てで扱う（[daily](../daily/2026-08-19.md)）

## 関連
- [topics/a2a-protocol](a2a-protocol.md)
- [topics/claude-code](claude-code.md)
