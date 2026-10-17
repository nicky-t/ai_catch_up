---
type: topic
title: "SB Intuitions（Sarashina）"
slug: sb-intuitions
created: 2026-10-14
updated: 2026-10-18
tags: [japan-company]
level: beginner
audience: [engineer, business, instructor]
related: [threads/japan-ai-adoption.md, topics/elyza.md]
---

# SB Intuitions（Sarashina）

## 一言で
ソフトバンクの子会社（東京都港区）で、日本語に強い大規模言語モデル「Sarashina」シリーズの研究開発を手がける国内AI企業。

## 仕組み
- 2026年10月13日、「Sarashinaサービス」の無償β版を公開。Webチャット（対話・翻訳の体験）と、6モデルを呼び出せるAPIを一般公開した
- APIで使える6モデル：文章生成・対話の「Sarashina3 mini」、単純タスクの大量高速処理向け「Sarashina3 nano」、文書検索・RAG向け埋め込みの「Sarashina3 embedding」、検索結果の精度向上「Sarashina3 rerank」、入力テキストの安全性判定「Sarashina3 guard」、日英・英日翻訳「Sarashina3 translate」
- 日本語向けに設計したトークナイザにより、同じ文章を米国モデルの半分のトークン数で表せるという
- Googleアカウントでログインすれば事前申し込みなしで誰でも無料で利用できる。一定時間あたりのリクエスト数に上限があり、β版の終了時期は未定。公式リリースでも正式版（有料プラン等）の提供時期・料金への言及はなく、現時点では無償β版のみが確認できる状態（出典: [PR TIMES — SB Intuitionsプレスリリース](https://prtimes.jp/main/html/rd/p/000000002.000141057.html)、取得日 2026-10-18）。利用データはAIモデル・サービスの品質向上目的で活用される場合があるとも明記されている

## 実務での使い方
- 自社システムへの組み込み前に、日本語タスクでの精度・トークン効率を無料で検証できる
- 翻訳・安全性判定・検索精度向上まで含めた6モデル構成のため、RAGパイプラインを国産モデルだけで試作する際の比較対象になる

## 講座で使うなら
- 30 秒説明: 「ソフトバンクの子会社が、日本語に強いAIモデル『Sarashina』を無料で試せるサービスを始めました。チャットだけでなくAPIも使えます」
- たとえ話: 海外製の辞書をそのまま使うのではなく、日本語の語感に合わせて作り直した辞書を無料で配っている
- 演習案: 受講者に「同じ文章を日本語モデルと海外モデルでトークン数を比べる」演習を行わせ、コスト差を体感させる

## この話題の流れ
<!-- agent が日付順に追記。新しいものを上に -->
- 2026-10-14: 「Sarashinaサービス」の無償β版を公開。チャットと6モデルのAPIを一般開放し、日本語向けトークナイザで米国モデルの半分のトークン数を実現すると説明（[daily](../daily/2026-10-14.md) / [threads/japan-ai-adoption](../threads/japan-ai-adoption.md)）

## 関連
- [topics/elyza](elyza.md)
