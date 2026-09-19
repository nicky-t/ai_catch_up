---
type: topic
title: "Jev（TypeSafe AI）"
slug: jev
created: 2026-09-19
updated: 2026-09-20
tags: [agent, cost]
level: beginner
audience: [engineer, business, instructor]
related: [topics/openai.md, topics/google.md]
---

# Jev（TypeSafe AI）

## 一言で
米新興TypeSafe AI（創業者ディオゴ・アルメイダ氏）が開発した、文章を生成する従来のLLMとは違い、あらかじめ定義した選択肢に対する「確率・信頼度スコア」を返す新しいタイプのAIモデル。

## 仕組み
- 出力がテキストではなく確率・信頼度スコアである点が最大の特徴。ユーザーが事前に出力の選択肢を定義するため、原理的に「幻覚」が生じにくいとされる
- TypeSafe AI自身は、Jevを人間との対話用ではなく「機械が直接使うことを前提にした新しい種類のモデル（System One Models）」と位置づけ、新しいアーキテクチャ・新しいサンプラー・新しい学習アルゴリズム「RLCD（Reinforcement Learning for Calibrated Decisions）」の3点で構成されると説明。RLHF（人間のフィードバックによる強化学習）が引き起こす「モード崩壊・過信・信頼性の欠如」への対策として、文章ではなくソフトウェアが直接扱える「型付き出力（typed outputs）」と較正済みの信頼度を返す設計を採るという（アーキテクチャの詳細な仕様は非公開）（出典: [TypeSafe AI公式サイト](https://www.typesafe.ai/)、取得日 2026-09-20）
- 入力トークンの課金単位が従来LLMの百万単位ではなく十億単位になるとされ、大量の分類・判定タスクを低コストで処理できる設計とみられる
- 導入企業の実測値：Vercelは既存のOpenAI「Luna」モデルからの置き換えで「5〜18倍高速化、精度も向上」と報告。Bryo AIはメール分類タスクでGoogleの「Gemini」と比較し「Geminiがわずかに高精度だが10〜20倍高コスト」（Jev側が10〜20倍安価）と評価（出典: [TechCrunch — A new kind of AI model from a ChatGPT inventor is thrilling developers](https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/)、取得日 2026-09-19）

## 実務での使い方
- 「文章を書かせる」のではなく「Yes/No判定」「カテゴリ分類」「エージェントの出力が正しいかの検証」など、選択肢が決まっているタスクに向く
- 汎用LLM1本で全工程をこなす設計から、判定・分類のステップだけを専用モデルに切り出す設計への移行例として参考になる（要追記：日本語タスクでの検証事例）

## 講座で使うなら
- 30 秒説明: 「文章を書くAIではなく、『この分類は合っていますか』に確率で答える専門のAIモデルです」
- たとえ話: 何を聞いても長文で答える顧問より、YES/NOと自信の度合いだけを即答してくれる査定士
- 演習案: 自分の業務の中で「分類・判定」だけの作業を1つ挙げ、それを専用モデルに切り出すとしたら何が変わるかを議論させる

## この話題の流れ
<!-- agent が日付順に追記。新しいものを上に -->
- 2026-09-19: TypeSafe AIが新型モデル「Jev」を発表。Vercelが既存のOpenAI「Luna」から置き換えて5〜18倍高速化、Bryo AIがGoogleの「Gemini」比10〜20倍安価と報告（[daily](../daily/2026-09-19.md)）

## 関連
- [topics/openai](openai.md)（比較対象のLunaモデル）
- [topics/google](google.md)（比較対象のGeminiモデル）
