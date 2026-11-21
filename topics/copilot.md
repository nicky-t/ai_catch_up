---
type: topic
title: "Copilot（GitHub Copilot / Microsoft 365 Copilot）"
slug: copilot
created: 2026-11-02
updated: 2026-11-22
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
- 2026年のGitHub Universeで発表された「GitHub Copilot Fusion」は、タスクの特性に応じて単一または複数のAIモデルを組み合わせる機能。実行方式はSingle（1モデルがタスク全体を完了）・Cascade（効率的なモデルが下書きを作成し、判定役モデルが承認するか上位モデルへエスカレーションするかを判断）・Critique（1モデルが下書きを作成し、複数モデルが独立・並列に批評、フィードバックを集約して元のモデルが修正）の3種。レビュー呼び出しはタスクに必要な場合のみ追加され、中間の下書きは破棄されユーザーには最終応答のみ表示される。負荷レベルはFusion Standard・High・Maxから選択（Fusion Fastはユーザー指定不可、VS Codeのインラインチャット専用）。Fusion Standardは全プラン（Free・Student・Pro・Pro+・Max・Business・Enterprise）で利用可能、Fusion High・MaxはPro+以上限定（出典: [GitHub Docs — About Copilot Fusion](https://docs.github.com/en/copilot/concepts/models/copilot-fusion)、取得日2026-11-22）

## 実務での使い方
モデルを個別に選ぶ手間を減らし、性能とコストのバランスを取りやすくする。タスクごとに最適なモデルを自動で選ばせる発想は、他社のエージェントサービスにも広がりつつある（要追記：具体的な導入事例）

## 講座で使うなら
- 30秒説明: 「人間がモデルを選ぶ」から「タスクに応じてAIが複数モデルを自動的に使い分ける」への進化の具体例
- たとえ話: 簡単な案件は1人で片付け（Single）、少し不安な案件は下書きを上司がチェックしOKならそのまま・怪しければ別の専門家に回す（Cascade）、重要な案件は下書きを複数人が独立にレビューしフィードバックをまとめて本人が直す（Critique）という、社内の案件処理フローの違いに近い
- 演習案: Single・Cascade・Critiqueの3方式を、実際の業務タスク（簡単な修正／複雑な設計／重要判断のレビュー）に当てはめて選ばせる

## この話題の流れ
<!-- agent が日付順に追記。新しいものを上に -->
- 2026-11-22（週次整理・要追記対応）: GitHub公式ドキュメントで「Copilot Fusion」のCascade・Critique方式の判定ロジックを確認。Cascadeは効率的なモデルの下書きを判定役モデルが検査し承認かエスカレーションを判断、Critiqueは複数モデルが下書きを独立・並列に批評しフィードバックを集約して元のモデルが修正する。具体的な導入企業名は文書に記載なし（要追記のまま、[出典](https://docs.github.com/en/copilot/concepts/models/copilot-fusion)、取得日2026-11-22）
- 2026-11-05: GitHub Universe 2026で「Copilot Dreaming」をパブリックプレビュー公開。コードや環境の変化で陳腐化する「AIへの指示」とCopilot Memoryが保持するリポジトリ固有ルールを、対話・PRレビューの分析結果に基づきバックグラウンドで自動整理・更新する。基調講演ではJavaアプリをSvelte/JavaScriptに書き直した例で、指示ファイルを新言語向けに書き換えるPRを自動提案した様子を紹介（[daily](../daily/2026-11-05.md) / [出典](https://www.publickey1.jp/blog/26/github_copilot_dreaminggithub_universe_2026.html)）
- 2026-11-04: GitHub Universe 2026で「Copilot Code Review Max」をパブリックプレビュー公開。既存の「Lite」「Balanced」に続く3番目のエフォートレベルで、複数のAIモデルが独立にレビューし集約エージェントが食い違いを調整する設計。ReviewBenchで重大度高い問題検出のF1スコア最高を記録したという。同カンファレンスでは、AIエージェント急増に対応しGitの書き込みロックをリポジトリ単位からブランチ単位に変更するなどのアーキテクチャ刷新も発表され、テストで毎秒7,200回の書き込み（従来比180倍）を処理（[daily](../daily/2026-11-04.md) / [出典](https://www.publickey1.jp/blog/26/githubcopilot_code_review_maxgithub_universe_2026.html)）
- 2026-11-02: GitHub Universe 2026でマルチモデル機能「GitHub Copilot Fusion」の正式リリースを発表。Single・Cascade・Critiqueの3パターンでタスクに応じてモデルを使い分け、負荷レベルはFusion Standard・High・Maxから選択（Fusion Fastは選択不可）。パブリックプレビューでは、ローカル導入したMAI Code 1.1 FlashやQwen3.8 Flash NextもFusion Standardで利用可能（[daily](../daily/2026-11-02.md) / [topics/microsoft](microsoft.md) / [出典](https://www.publickey1.jp/blog/26/githubcopilot_fusionaigithub_universe_2026.html)）

## 関連
- [topics/microsoft](microsoft.md)
