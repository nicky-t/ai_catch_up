---
type: topic
title: "Claude Code（クロードコード）"
slug: claude-code
created: 2026-08-19
updated: 2026-09-20
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
- 2026-09-20: バージョン2.1.278を公開。Claude API・Enterprise利用者およびBedrock/Vertex/Foundry/ゲートウェイ経由で、「自動モード」の判定をローカル分類器からサーバー側分類器に切り替え、分類器のオーバーヘッド課金を回避できるようにした（[daily](../daily/2026-09-20.md)）
- 2026-09-20: 今日の現場ネタで、Anthropic公式の知識労働者向けプラグイン集「knowledge-work-plugins」を紹介。営業・マーケティング・法務・財務など11分野のプラグインを`claude plugin marketplace add`経由でインストールでき、Slack・HubSpot・Notionなど外部ツール連携済み（GitHubスター25.1k・本日+280）（[daily](../daily/2026-09-20.md) / [topics/agent-harness](agent-harness.md)）
- 2026-09-19: ITmedia（@IT）が、Claude利用時にありがちな「念のため」の過剰な確認・制約指示がトークンを浪費する6つのアンチパターン（確認基準の曖昧さ・過度な制限・モデル固有設定の誤解・モデルバージョン間の非互換・キャッシング未活用・古いシステム指示の蓄積）を紹介（[daily](../daily/2026-09-19.md)）
- 2026-09-19: 今日の現場ネタで、エージェント・ハーネス「ECC」がClaude Codeのプラグインマーケットプレイス経由でインストール可能になったことを紹介（GitHubスター262k・本日+965）（[daily](../daily/2026-09-19.md) / [topics/agent-harness](agent-harness.md)）
- 2026-09-18: ITmedia（@IT）が、コストが想定より膨らむ主な原因（プロンプトキャッシュの理解不足、ファイル参照時の不要な内容の読み込み、複数タスクを1セッションで実行した際のコンテキスト保持）と対策（`/clear`・`/model`・`/effort`の事前設定・`/compact`の活用）を紹介（[daily](../daily/2026-09-18.md)）
- 2026-09-18: 今日の現場ネタで、ログイン済みブラウザをそのままAIエージェントに操作させるSkill「BrowserSkill」（Tencent）を紹介（GitHubスター4,032・本日+1,350）（[daily](../daily/2026-09-18.md)）
- 2026-09-16: バージョン2.1.271〜273を公開。LLMゲートウェイ識別用のリクエストヘッダー追加、リモートコントロールセッションのバックグラウンドでの「フォーク」機能、危険なコマンド・サブシェル検知の権限チェック強化などを追加（[daily](../daily/2026-09-16.md)）
- 2026-09-16: 今日の現場ネタで、著名エンジニアAddy Osmani氏が公開する本番品質エンジニアリング向けSkill集「agent-skills」を紹介（GitHubスター94.7k・本日+386）。仕様策定→計画→実装→テスト→レビュー→出荷の6フェーズに対応する9個のスラッシュコマンドを持つ（[daily](../daily/2026-09-16.md)）
- 2026-09-14: 今日の現場ネタで、静的解析とSnyk Agent Scanで安全性を検証済みのSkillを集めたオープンソースレジストリ「agent-skills」を紹介（GitHub Trending本日+215スター、累計5,600超。`npx @tech-leads-club/agent-skills` でインストール）（[daily](../daily/2026-09-14.md)）
- 2026-09-12: 今日の現場ネタで、仕様設計→TDD→サブエージェント並列→2段階レビューを強制するSkillフレームワーク「Superpowers」を紹介（GitHub Trending本日+731スター、Claude Code公式マーケットプレイス対応）（[daily](../daily/2026-09-12.md) / [topics/agent-harness](agent-harness.md)）
- 2026-09-12: 2026年8月7日付で自動実行モードをデフォルト化したと報道。1,053人の有資格テスターの評価で危険コマンド遮断率がAI側89%・人間側13.6%だったことが根拠（[daily](../daily/2026-09-12.md)）
- 2026-09-11: バージョン2.1.268を公開。`gateway.yaml`の`pricing:`設定によるClaude apps gateway料金連携、WebFetchの300秒タイムアウト化、サードパーティAnthropic互換エンドポイントでのHTTP 400不具合修正などを追加（[daily](../daily/2026-09-11.md)）
- 2026-09-11: 今日の現場ネタで、352プロバイダーをローカルで束ねる無料AIゲートウェイ「OmniRoute」を紹介（GitHub Trending本日+591スター）（[daily](../daily/2026-09-11.md) / [topics/openrouter](openrouter.md)）
- 2026-09-10: バージョン2.1.263〜267を公開。`maxEffortLevel`設定による全プロバイダー横断のエフォートレベル制限、LLMゲートウェイ認証失敗の修正、テレメトリへの`user.email`／`user.groups`追加、`--plugin-dir`によるプラグインフォルダ対応、ツール結果1GBキャップなどを追加（[daily](../daily/2026-09-10.md)）
- 2026-09-10: 今日の現場ネタで、回答を行動優先・前置きなしの簡潔な形式に変えるSkill「i-have-adhd」を紹介（GitHub Trending本日+4,624スター）（[daily](../daily/2026-09-10.md)）
- 2026-09-09: 今日の現場ネタで2件紹介。使い捨てVMでClaude Code・Codexを分離実行するRust製CLI「coop」（GitHub 180スター）と、ツール出力をサンドボックス化してコンテキスト消費を削減するMCPサーバー「context-mode」（GitHub Trending本日+652スター、累計21,340）（[daily](../daily/2026-09-09.md)）
- 2026-09-07: Spotifyのエンジニアが公開したプラグイン「Portal」が、ファイル一括読み込みやテスト・ボイラープレート生成を安価なモデルへ委譲することでトークン使用量を最大90%削減できると報告（HN 266pt）（[daily](../daily/2026-09-07.md)）
- 2026-09-06: バージョン2.1.259〜2.1.261を公開。組織がHTTP/SSE MCPサーバーをユーザーに提供できる「managedMcpServers」設定、無人実行用の`--permission-prompts none`オプション、会話横に変更内容を表示する差分パネル、`/skill-doctor`の未使用スキル確認機能などを追加（[daily](../daily/2026-09-06.md)）
- 2026-09-06: GitHub TrendingでClaude Code向けSkillパック「humanlayer/skills」（本日+408スター）とローカルモデル実行ツール「Magnitude」（本日+686スター）が急上昇（[daily](../daily/2026-09-06.md)）
- 2026-09-04: GitHub Trendingで、コーディングエージェント向けSkill集「mattpocock/skills」（本日+1,576スター）と、過剰実装を防ぐ「ponytail」（本日+2,138スター）が急上昇（[daily](../daily/2026-09-04.md)）
- 2026-09-02: バージョン2.1.257で新モデル「Claude Fable 5.1」（`claude-fable-5-1`）を追加。複合コマンド実行時の権限確認スキップ、シンボリックリンク経由の権限外読み取りなど権限すり抜けの脆弱性7件を修正（[daily](../daily/2026-09-02.md) / [topics/anthropic](anthropic.md)）
- 2026-09-01: 週次利用枠を9月14日から恒久25%増（125）に変更すると発表——5月13日から適用中だった期間限定の50%増（150）からは実質17%減。オープンソースの統合ハーネスツール「ECC」（68エージェント・286スキル）がGitHubで24万スター超に成長（[daily](../daily/2026-09-01.md) / [topics/agent-harness](agent-harness.md)）
- 2026-08-31: バージョン2.1.251で、権限チェック後のシンボリックリンク差し替えやプラグインのパストラバーサルなど複数のセキュリティ問題を修正（Auto Modeの脆弱性とは別系統）。JetBrainsがQwenベースのローカル版コーディングエージェント「Junie Local」を投入し、社内テストでClaude Sonnet 4.5相当の性能と比較された（[daily](../daily/2026-08-31.md) / [topics/qwen](qwen.md)）
- 2026-08-28: セキュリティ研究者Johann Rehberger氏が、Auto ModeへのZIP展開を悪用したプロンプトインジェクション攻撃を報告（成功率約80%）。侵害を検知しても、Auto Modeが復旧コマンドの実行をブロックしてしまう問題も判明（[daily](../daily/2026-08-29.md)）
- 2026-08-28: Agent Skill「archify」がGitHub Trendingで急上昇（本日+4,260スター）。コードやシステム構成からアーキテクチャ図・シーケンス図などをエージェントに生成させられる（[daily](../daily/2026-08-28.md)）
- 2026-08-24: JSランタイム「Bun」v1.4（Zig→Rust移植）のリリース作業にClaude Codeが活用された（[daily](../daily/2026-08-24.md)）
- 2026-08-21: 開発者 Boris Cherny が講演で、システムプロンプトを「アブレーション」で再構築し80%削減できたと紹介（[daily](../daily/2026-08-21.md)）
- 2026-08-19: 週次利用枠「50% 増」を 8 月 31 日まで延長 — 恒久化したいが容量逼迫のため（[daily](../daily/2026-08-19.md)）

## 関連
- [topics/cursor](cursor.md)
- [topics/openai](openai.md)（Codex との競合）
- [topics/mcp](mcp.md)（外部ツール連携の標準）
