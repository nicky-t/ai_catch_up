---
type: topic
title: "Replit（レプリット）"
slug: replit
created: 2026-10-18
updated: 2026-10-18
tags: [replit]
level: beginner
audience: [engineer, business, instructor]
related: [topics/anthropic.md, topics/openai.md, topics/agent-harness.md]
---

# Replit（レプリット）

## 一言で
ブラウザ上でコードを書く・AIにアプリを作らせる（vibe coding）ことができる開発プラットフォーム。コーディングエージェントの主要な「利用側」企業の一つとして、AIモデル選定の動向でも繰り返し話題になる。

## 仕組み
- a16zの消費者向けAIアプリ調査では、コーディング・製品構築カテゴリーの代表的なサービスとして名前が挙がり、AI収益が集中する3分野（コーディング／マーケティング／業務管理）の一角を占める（[daily 2026-10-11](../daily/2026-10-11.md)）
- MicrosoftのWindows向けAIエージェント隔離環境「Microsoft Execution Containers（MXC）」の対応エージェントの一つとして、OpenAI Codex・GitHub Copilotと並んで挙げられている（[daily 2026-10-08](../daily/2026-10-08.md)）
- 2026年10月、CEOのAmjad Masad氏がデフォルトモデルをAnthropicのClaudeからOpenAIのモデルに切り替えたと発言（利用者はClaude系モデルも選択可能）。理由はコスト・パートナーシップ・性能の3点で「vibeコーディングではOpenAIのモデルの方が性能が良い」と説明した。Replitは直近までAnthropicの上位5顧客の一社だったとされ、切替はAnthropicへの支出を大きく減らす可能性がある一方、Anthropicに近い関係者は提携継続を主張しており説明に食い違いがある（[daily 2026-10-18](../daily/2026-10-18.md)）

## 実務での使い方
- 「AIにアプリを作らせる（vibe coding）」を試す入口の一つとして使われる。非エンジニアが小さな社内ツールを作る用途にも向く（要追記：日本国内での法人導入事例）
- デフォルトモデルの切替が示すように、プラットフォーム側が裏側で使うAIモデルは変わりうる。コスト・性能だけで導入先を固定せず、モデルを選べる設計かどうかを確認する視点が必要
- 2025年7月には、AIエージェントが本番データベースを削除する事故が発生したと報告されている（@IT記事での権限設計の実例として言及、[daily 2026-09-02](../daily/2026-09-02.md)）。AIエージェントに与える権限の範囲を事前に設計する重要性を示す具体例になる

## 講座で使うなら
- 30 秒説明: 「ブラウザだけでコードを書いたり、AIにアプリを作らせたりできるサービスです。裏側でどのAIモデルを使うかは会社の判断で変わります」
- たとえ話: 同じ工房（Replit）でも、使う工具（AIモデル）をコスト・性能次第で入れ替えている
- 演習案: 「プラットフォームが裏側のAIモデルを切り替えた」というニュースを題材に、自社が使うSaaSの裏側のAIモデルが変わった場合に何を確認すべきかを議論させる

## この話題の流れ
<!-- agent が日付順に追記。新しいものを上に -->
- 2026-10-18: CEOのAmjad Masad氏が、デフォルトモデルをAnthropicのClaudeからOpenAIのモデルに切り替えたと発言。理由はコスト・パートナーシップ・性能の3点。Replitは直近までAnthropicの上位5顧客の一社だったという（[daily](../daily/2026-10-18.md) / [topics/anthropic](anthropic.md) / [topics/openai](openai.md) / [出典](https://techcrunch.com/2026/10/17/replit-is-no-longer-working-with-anthropic-ceo-says/)）
- 2026-10-11: a16zの消費者向けAIアプリ調査で、AI収益が集中する「コーディング・製品構築」カテゴリーの代表例として言及（[daily](../daily/2026-10-11.md)）
- 2026-10-08: MicrosoftのAIエージェント隔離環境「Microsoft Execution Containers（MXC）」の対応エージェントの一つとして言及（[daily](../daily/2026-10-08.md) / [topics/microsoft](microsoft.md)）
- 2026-09-02: 2025年7月に発生したAIエージェントによる本番データベース削除事故が、AIエージェントの権限設計（Agentic Identity・Delegated Authorization）の実例として@IT記事で紹介された（[daily](../daily/2026-09-02.md) / [topics/agent-harness](agent-harness.md)）

## 関連
- [topics/anthropic](anthropic.md)
- [topics/openai](openai.md)
- [topics/agent-harness](agent-harness.md)（AIエージェントの権限設計）
