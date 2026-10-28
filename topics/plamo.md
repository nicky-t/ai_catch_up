---
type: topic
title: "PLaMo（プラモ）"
slug: plamo
created: 2026-10-24
updated: 2026-10-29
tags: [japan-company, adoption]
level: beginner
audience: [engineer, business, instructor]
related: [threads/japan-ai-adoption.md]
---

# PLaMo（プラモ）

## 一言で
Preferred Networks（PFN）が海外モデルを基にせず一から開発した国産LLM。行政・教育・採用などオンプレミス需要の強い分野でニッチな採用が広がっている。

## 仕組み
- 海外の大規模言語モデルをベースにせず、PFNが独自に一から開発
- 行政分野ではデジタル庁の「源内」や約800自治体が使う「QommonsAI」で採用。オンプレミス利用（自社・自組織の環境内で動かす）の需要も多い（2026-10-23既報）
- 教育分野では小論文添削AI「ろんじろう」、採用分野ではAI面接「タレスカAI面接」でも利用されている

## 実務での使い方
- オンプレミス要件・データの海外送信を避けたい要件がある場合、国産モデルが選択肢になりうる
- モデル自体に任せる部分とアプリケーション側で作り込む部分を分けて設計するという考え方は、他のモデル選定でも参考になる
- 用途によっては海外モデルと使い分ける（PLaMoに一本化しない）運用も現実的な選択肢

## 講座で使うなら
- 30 秒説明: 「海外モデルを使わず、ゼロから作られた国産AI。行政や教育など、データを外に出したくない分野で使われています」
- たとえ話: 輸入車ではなく国内で一から設計された車。燃費やブランド力では一歩劣っても、保守部品の調達や仕様の細かい調整がしやすい
- 演習案: 自分の業務でオンプレミス要件が発生しそうな場面（個人情報・機密情報を扱う業務）を1つ挙げ、海外モデルと国産モデルどちらが向くか判断させる

## この話題の流れ
<!-- agent が日付順に追記。新しいものを上に -->
- 2026-10-29: フラグシップモデル「PLaMo 3.1 Prime」を発表。「PLaMo Chat」・API・オンプレミスで提供開始。ハルシネーション関連8ベンチマークで前モデルから平均約15%改善、35種のベンチマークの安全性スコアはQwen 3.8 27B・gpt-oss-120B・Gemma 4 31B等を上回り最高だったが、STEM・コーディング・Web検索を伴う回答は競合モデルを下回る。API「Standardプラン」は100万トークンあたり入力60円・出力250円（[daily](../daily/2026-10-29.md) / [threads/japan-ai-adoption](../threads/japan-ai-adoption.md) / [出典](https://www.itmedia.co.jp/aiplus/article/2610/28/2000002652/)）
- 2026-10-24: PFNがCEATEC 2026で活用事例を展示。デジタル庁「源内」・約800自治体の「QommonsAI」（行政）、小論文添削AI「ろんじろう」（教育）、AI面接「タレスカAI面接」（採用）での採用例を紹介し、モデルに任せる部分とアプリケーション側の作り込みを分ける設計の重要性を指摘（[daily](../daily/2026-10-24.md) / [threads/japan-ai-adoption](../threads/japan-ai-adoption.md) / [出典](https://www.itmedia.co.jp/aiplus/article/2610/23/2000002368/)）

## 関連
- [threads/japan-ai-adoption](../threads/japan-ai-adoption.md)
