---
type: topic
title: "Preferred Networks（PFN）"
slug: pfn
created: 2026-11-06
updated: 2026-11-06
tags: [japan-company, open-weights]
level: beginner
audience: [engineer, business, instructor]
related: [topics/plamo.md, threads/japan-ai-adoption.md]
---

# Preferred Networks（PFN）

## 一言で
海外モデルを基にせず一から基盤モデルを開発している国産AI企業。自社ブランド「PLaMo」シリーズを汎用・翻訳特化など複数ラインで展開している。

## 仕組み
- フラグシップの汎用LLM「PLaMo」シリーズ（[topics/plamo](plamo.md)）と、翻訳特化の「PLaMo Translate」シリーズを別ラインで開発
- 翻訳特化モデルは小型サイズでもオンデバイス実行を重視し、スマートフォン・ノートPCでの動作を想定して設計されている
- 独自の「PLaMoコミュニティライセンス」で重みを公開し、一定の売上規模以下の企業・個人には商用利用も認めている

## 実務での使い方
- 行政・教育など「オンプレミス要件が強い」分野での採用例が多い（[threads/japan-ai-adoption](../threads/japan-ai-adoption.md)参照）
- 翻訳特化モデルはクラウド接続やコストの制約がある現場（オフライン端末での多言語対応など）で選択肢になりうる
- ベンチマークの比較対象（どのモデルと比べて「最高水準」なのか）を確認してから導入判断に使う

## 講座で使うなら
- 30 秒説明: 「海外の大手モデルを土台にせず、日本の会社が一から作っている国産AIモデルの会社です」
- たとえ話: 海外製の汎用工具に対する、国内メーカーの専用工具（翻訳など特定作業に特化）
- 演習案: 受講者に「PLaMo 3 Translate」の性能主張（TranslateGemma・Hy-MT2との比較）の比較対象・母数を確認させる

## この話題の流れ
<!-- agent が日付順に追記。新しいものを上に -->
- 2026-11-06: 翻訳特化LLM「PLaMo 3 Translate」をオープンウェイトで公開。0.8B・2B・8B・31Bの4サイズで、スマートフォン・ノートPCでのオンデバイス実行に対応。最小の0.8Bモデルでも、Googleの「TranslateGemma」・Tencentの「Hy-MT2」を上回る翻訳性能と主張。重みはHugging Faceで公開、「PLaMoコミュニティライセンス」下で直近事業年度の売上10億円以下の企業・個人は商用利用可能（[daily](../daily/2026-11-06.md) / [threads/japan-ai-adoption](../threads/japan-ai-adoption.md) / [出典](https://www.itmedia.co.jp/aiplus/article/2611/05/2000002900/)）

## 関連
- [topics/plamo](plamo.md)
- [threads/japan-ai-adoption](../threads/japan-ai-adoption.md)
