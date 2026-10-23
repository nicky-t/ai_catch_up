---
type: topic
title: "ChatGPT Work"
slug: chatgpt-work
created: 2026-10-24
updated: 2026-10-24
tags: [openai, productivity, case-study]
level: beginner
audience: [engineer, business, instructor]
related: [topics/openai.md]
---

# ChatGPT Work

## 一言で
OpenAIが企業向けに提供するChatGPTのプラン・製品群。ログインが必要なWebサイトの操作代行や音声エージェント機能など、一般ユーザー向けのChatGPTにはない業務特化機能を備える。

## 仕組み
- 一般のChatGPT（個人向け）とは別に、企業の業務利用を想定したプラン・機能群として提供される
- ログインが必要なWebサイトの操作にも対応し、ユーザーが自分でログインした後の作業をAIが代行できる。ID・パスワードはモデルに送信されない設計（2026-08-27既報）
- モバイルアプリでは音声コマンドで書類作成・メール下書き・Slackメッセージ要約などを指示できる「Work」タブを搭載（2026-09-24既報）
- 2026年10月、AIエージェントがユーザーに代わってログインする仕組み「1Password for Agents」の対応エージェントの一つに選ばれた（[topics/claude-duet](claude-duet.md)と同様の位置づけ）

## 実務での使い方
- 非エンジニアの業務（データ分析・資料の多言語化・ダッシュボード作成など）にも使いやすい設計で、「AI導入はエンジニア向け」という前提を見直す材料になる
- ログイン必須のWebサイト操作を任せる場合は、認証情報の扱い（モデルに送信しない設計かどうか）を導入前に確認する

## 講座で使うなら
- 30 秒説明: 「ChatGPTの企業向け版。ログインが必要なサイトの操作代行や音声での指示にも対応しています」
- たとえ話: 個人用の便利な相談相手（ChatGPT）に、会社の業務道具一式（Work）を持たせたようなもの
- 演習案: 自分の業務のうち「ログインが必要なサイトでの定型作業」を1つ挙げ、代行を任せる場合に確認すべき認証情報の扱いを考えさせる

## この話題の流れ
<!-- agent が日付順に追記。新しいものを上に -->
- 2026-10-24: Uberが全従業員約3万人にChatGPT Workを展開すると発表。今年初めの約1,000人での試験導入では参加者の約8割が非エンジニアで、データ分析・研修資料の多言語化・ダッシュボード作成に使われた。OpenAIはUberとの統合作業に緊密に協力したとコメント（[daily](../daily/2026-10-24.md) / [topics/openai](openai.md) / [出典](https://techcrunch.com/2026/10/22/uber-puts-all-30000-employees-on-chatgpt-work/)）

## 関連
- [topics/openai](openai.md)
