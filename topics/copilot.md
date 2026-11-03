---
type: topic
title: "Copilot（GitHub Copilot / Microsoft 365 Copilot）"
slug: copilot
created: 2026-11-02
updated: 2026-11-04
tags: [copilot, microsoft]
level: beginner
audience: [engineer, business, instructor]
related: [topics/microsoft.md]
---

# Copilot（GitHub Copilot / Microsoft 365 Copilot）

## 一言で
MicrosoftとGitHubが提供するAIアシスタント群の総称。GitHub Copilotはコード補完・チャット・エージェント機能を中心に、開発者の作業を支援する。

## 仕組み
- GitHub Copilotはコード補完・チャット型支援・エージェント機能を提供
- 2026年のGitHub Universeで発表された「GitHub Copilot Fusion」は、タスクの特性に応じて単一または複数のAIモデルを組み合わせる機能。実行方式はSingle・Cascade・Critiqueの3種、負荷レベルはFusion Standard・High・Maxから選択（Fusion Fastはユーザー指定不可）（技術詳細は要追記）

## 実務での使い方
モデルを個別に選ぶ手間を減らし、性能とコストのバランスを取りやすくする。タスクごとに最適なモデルを自動で選ばせる発想は、他社のエージェントサービスにも広がりつつある（要追記：具体的な導入事例）

## 講座で使うなら
- 30秒説明: 「人間がモデルを選ぶ」から「タスクに応じてAIが複数モデルを自動的に使い分ける」への進化の具体例
- たとえ話: （要追記）
- 演習案: Single・Cascade・Critiqueの3方式を、実際の業務タスク（簡単な修正／複雑な設計／重要判断のレビュー）に当てはめて選ばせる

## この話題の流れ
<!-- agent が日付順に追記。新しいものを上に -->
- 2026-11-04: GitHub Universe 2026で「Copilot Code Review Max」をパブリックプレビュー公開。既存の「Lite」「Balanced」に続く3番目のエフォートレベルで、複数のAIモデルが独立にレビューし集約エージェントが食い違いを調整する設計。ReviewBenchで重大度高い問題検出のF1スコア最高を記録したという。同カンファレンスでは、AIエージェント急増に対応しGitの書き込みロックをリポジトリ単位からブランチ単位に変更するなどのアーキテクチャ刷新も発表され、テストで毎秒7,200回の書き込み（従来比180倍）を処理（[daily](../daily/2026-11-04.md) / [出典](https://www.publickey1.jp/blog/26/githubcopilot_code_review_maxgithub_universe_2026.html)）
- 2026-11-02: GitHub Universe 2026でマルチモデル機能「GitHub Copilot Fusion」の正式リリースを発表。Single・Cascade・Critiqueの3パターンでタスクに応じてモデルを使い分け、負荷レベルはFusion Standard・High・Maxから選択（Fusion Fastは選択不可）。パブリックプレビューでは、ローカル導入したMAI Code 1.1 FlashやQwen3.8 Flash NextもFusion Standardで利用可能（[daily](../daily/2026-11-02.md) / [topics/microsoft](microsoft.md) / [出典](https://www.publickey1.jp/blog/26/githubcopilot_fusionaigithub_universe_2026.html)）

## 関連
- [topics/microsoft](microsoft.md)
