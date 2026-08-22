---
type: topic
title: "Anthropic（アンソロピック）"
slug: anthropic
created: 2026-08-22
updated: 2026-08-23
tags: [anthropic, claude]
level: beginner
audience: [engineer, business, instructor]
related: [topics/claude-code.md, topics/openai.md]
---

# Anthropic（アンソロピック）

## 一言で
「Claude」シリーズのモデルを開発する米国の AI 企業。安全性重視の企業文化を掲げつつ、Claude Code・Claude Cowork などコーディング・業務エージェント製品を急速に拡大している。

## 仕組み
- モデルラインは Claude（例：Claude Opus 5、Claude Fable 5、Claude Mythos 5）。API・チャット（Claude.ai）・コーディングエージェント（Claude Code）・業務エージェント（Claude Cowork）など製品群を展開
- 製品ページでは Mythos・Fable・Opus・Sonnet・Haiku の 5 系統がモデルファミリーとして並記されており、Opus が「大規模な進歩」を遂げた主力ラインと位置づけられている（世代番号・性能階層の詳細な対応表は同ページに明記されていない）（出典: [claude.com/product/overview](https://claude.com/product/overview)、取得日 2026-08-23）
- 顧客のプライバシー保護では、不正利用検知のためデータを 30 日保持する方針を取っており、ゼロデータ保持を掲げる OpenAI の「Private Safety Processing」と対照的な立場（[daily 2026-08-20](../daily/2026-08-20.md)）
- 2026 年 8 月、Claude・Claude Code・Claude Cowork の使い方を学べる無料の公式学習サイト「Claude Academy」（academy.claude.com）を公開。日本語翻訳（α版）にも対応

## 実務での使い方
- 企業がモデルを選ぶ際、OpenAI と Anthropic のどちらを軸にするかは「エコシステム（決済・Web3 連携など）」や「データ保持方針」といった経営判断が絡む（例：SBI は Anthropic の Claude を選択、[threads/japan-ai-adoption](../threads/japan-ai-adoption.md)）
- 講座の入口として Claude Academy を案内すると、受講者が自分のペースで一次情報に触れられる

## 講座で使うなら
- 30 秒説明: 「Claude という AI モデルを作っている会社で、安全性を重視しつつコーディングや業務の自動化エージェントにも力を入れています」
- たとえ話: 慎重派の開発チームが、使いやすい自動化ツールも同時に作っている
- 演習案: Claude Academy のコース一覧を受講者に見てもらい、自分の業務に近いコースを 1 つ選ばせて要約させる

## この話題の流れ
<!-- agent が日付順に追記。新しいものを上に -->
- 2026-08-23: 最高性能モデル「Claude Mythos 5」を脆弱性スキャン専用に開放。Claude Security 経由でEnterprise顧客が追加契約なしに利用可能、防御側支援基金「Defender Advantage Fund」（3,500万ドル）も始動（[daily](../daily/2026-08-23.md)）
- 2026-08-23: DeepMind出身者の新興Inherentが、270億パラメータの小型モデルで Claude Opus 4.8 を上回る研究再現性能を実証（[daily](../daily/2026-08-23.md)）
- 2026-08-22: 無料公式学習サイト「Claude Academy」公開。Claude Code・Claude Cowork の使い方もコースで解説、日本語翻訳（α版）対応（[daily](../daily/2026-08-22.md)）
- 2026-08-22: SBI 北尾会長が「孫さんは OpenAI だが、僕は Anthropic」と発言、Claude を軸にしたエージェント開発に初期投資 5 億円・年間 27 億円規模で取り組むと表明（[daily](../daily/2026-08-22.md)）
- 2026-08-22: Slack の新機能「Slack Code」が対応エージェントの一つとして Claude を採用（[daily](../daily/2026-08-22.md)）

## 関連
- [topics/claude-code](claude-code.md)
- [topics/openai](openai.md)（データ保持方針の対比）
