---
type: learn
track: intermediate
number: 031
title: "MCP（Model Context Protocol）：何を標準化したのか"
date: 2026-09-18
level: intermediate
audience: [engineer, business]
tags: [mcp, agent, tool-use]
reading_minutes: 5
sources:
  - url: https://modelcontextprotocol.io/introduction
    title: "What is the Model Context Protocol (MCP)?"
    fetched: 2026-09-18
  - url: https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture
    title: "Architecture overview"
    fetched: 2026-09-18
related: [topics/mcp.md, topics/claude-code.md]
---

# 031 MCP（Model Context Protocol）：何を標準化したのか

!!! abstract "この記事で説明できるようになること"
    - MCPが「ホスト・クライアント・サーバー」のどの部分の何を標準化したか
    - 「データ層」と「トランスポート層」の役割の違い
    - サーバーが提供する3つの基本要素（tools / resources / prompts）と、その発見・実行の流れ

## 仕組み

MCPは「AIアプリケーションが外部のデータ・ツールにつながる方法」を標準化したオープンプロトコルで、次の3つの登場人物で構成される。

- **MCPホスト**：Claude CodeやClaude Desktopなど、ユーザーが直接使うAIアプリケーション
- **MCPクライアント**：ホストが接続先サーバーごとに1つずつ内部に持つ、接続を維持する部品
- **MCPサーバー**：実際にデータやツールを提供するプログラム。ローカル（同一マシン上）でも、リモート（他社が運営するサービス）でも構わない

ホストは接続したいサーバーの数だけクライアントを生成し、各クライアントが1つのサーバーと専用の接続を保つ。VS Codeが「Sentry用」「ファイルシステム用」など複数のMCPサーバーに同時接続する場合、内部的には複数のクライアントが並行して動いている。

プロトコルは2つの層に分かれる。**データ層**は「何をやり取りするか」を決める部分で、JSON-RPC 2.0という汎用のメッセージ形式の上に、`tools/list`（ツール一覧取得）・`tools/call`（ツール実行）のようなMCP独自のメソッドを定義する。**トランスポート層**は「どう届けるか」を決める部分で、同一マシン内の高速なやり取りに向く**stdio**（標準入出力）と、他社サービスなどリモート接続向けの**Streamable HTTP**（HTTP POST＋必要に応じてサーバー送信イベント）の2方式がある。層を分けたことで、どちらのトランスポートを使ってもデータ層のメッセージ形式は変わらない。

サーバー側が提供できる基本要素（プリミティブ）は3種類：

| プリミティブ | 内容 | 例 |
|---|---|---|
| **Tools** | AIが呼び出せる実行可能な関数 | ファイル操作・API呼び出し・DB検索 |
| **Resources** | AIに渡す文脈データ | ファイルの中身・DBレコード |
| **Prompts** | やり取りをテンプレート化した定型文 | システムプロンプト・Few-shot例 |

クライアントはまず`tools/list`のような`*/list`系メソッドで「何が使えるか」を毎回問い合わせてから、必要なものだけを`tools/call`で実行する。この一覧取得→実行という2段階構成により、サーバー側で使えるツールが後から増減しても、クライアント側の実装を作り直す必要がない。

## 比較・判断基準

| 観点 | stdio | Streamable HTTP |
|---|---|---|
| 想定用途 | 同一マシン上のローカルサーバー（自分のファイルシステムなど） | 他社が運営するリモートサーバー（SaaS連携など） |
| クライアント数 | 通常1つのクライアントのみ接続 | 複数クライアントが同時接続できる |
| 認証 | 不要なことが多い | Bearerトークン・APIキー・OAuthなど標準的なHTTP認証を利用 |

「社内の業務システムをAIにつなぐ」場面では、まず対象システムが自社サーバー内で完結するか（stdio向き）、外部SaaS・複数拠点から呼ばれるか（HTTP向き）で選択肢が絞られる。

## 落とし穴

1. **ツールを増やしすぎるとコンテキストを圧迫する**：`tools/list`で返るツール定義（名前・説明・入力スキーマ）はすべてトークンとして消費される。接続するMCPサーバーを増やすほど、呼ばなくても定義分のコストがかかる（[learn 030](030-function-calling-tool-use.md)と同じ問題がMCP経由でも起きる）
2. **認証情報の管理が甘くなりやすい**：MCPサーバーの認証情報（APIキー・アクセストークン）管理の不備を突く「ツールポイズニング攻撃」が報告されており、`.env`への平文保存など基本的な管理ミスが実害につながる事例が指摘されている（[topics/mcp](../../topics/mcp.md)の2026-09-15の記録）
3. **サーバーを信頼する前提で設計しがち**：MCPはデータ層の仕様であり、接続先サーバーが安全かどうかは保証しない。社内向けに使う場合でも、提供元不明のMCPサーバーを安易に追加しない運用ルールが必要

## 実務への接続

社内のカレンダー・チケット管理・ドキュメント検索などをAIエージェントに使わせたい場合、個別にAPI連携コードを書く代わりに「対象システムがMCPサーバーとして提供されているか」を先に確認すると開発コストを抑えられる。逆に自社システムをAI対応させる立場なら、MCPサーバーとして1つ作れば、Claude・ChatGPTなど複数のAIアプリから使い回せるという利点がある。

## 講座で使うなら

- 30秒説明：「AIアプリ（ホスト）が外部のツールやデータ（サーバー）につながるための共通規格です。USB-Cのように、1回作れば複数のAIアプリで使い回せます」
- たとえ話：レストラン（AIアプリ）が食材卸業者（サーバー）ごとに専用の発注書フォーマットを作る代わりに、業界標準の発注書（MCP）1つで全業者とやり取りできるようにした
- 演習案：受講者の業務でよく使う社内システムを1つ挙げ、「Tools（実行させたい操作）」「Resources（読ませたいデータ）」「Prompts（定型のやり取り）」のどれに当たるか分類させる

## 出典・参考
- [What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/introduction)（取得日 2026-09-18）
- [Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture)（取得日 2026-09-18）

## 関連
- [topics/mcp](../../topics/mcp.md)
- [topics/claude-code](../../topics/claude-code.md)
