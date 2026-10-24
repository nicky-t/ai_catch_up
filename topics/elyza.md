---
type: topic
title: "ELYZA（イライザ）"
slug: elyza
created: 2026-10-03
updated: 2026-10-25
tags: [japan-company, open-weights]
level: beginner
audience: [engineer, business, instructor]
related: [threads/japan-ai-adoption.md]
---

# ELYZA（イライザ）

## 一言で
KDDI傘下で、日本語に強いAIモデルの開発を手がける国内AI企業。国立情報学研究所（NII）が公開する国産基盤モデル「LLM-jp-4」をベースに、追加学習したモデルを無料公開している。

## 仕組み
- 2026年10月2日、LLM-jp-4をベースに日本語処理能力を重点的に強化した2つのモデル（ELYZA-Thinking-1.0-llm-jp-4-33b、ELYZA-Thinking-1.0-llm-jp-4-32b-a3b）をHugging Face上で公開。ライセンスはApache 2.0で商用利用も可能
- 一部のベンチマークでは、ベースとなったLLM-jp-4よりも新しいNIIの「LLM-jp-4.1」系列を上回るスコアを記録したという
- この公開は、ELYZA社内の新しい研究組織「ELYZA RSI Research」が掲げる「再帰的自己改善（RSI：AIを使ってAI自身を段階的に改良していく）」という目標に向けた準備段階の成果と位置づけられている
- RSIへの道筋は4段階で説明されている：①Human-only（基盤モデルを1〜2日・少ない計算資源で学習できる仕組みの構築）②Human-in-the-loop（対話タスクを人が関与しながら評価するベンチマークの構築、人はAIエージェントへの方針提示と最終確認を担当）③Human-on-the-loop（AIがボトルネックを特定・改善する循環を繰り返し、ほぼ全自動でハーネスを改善できる段階。問い合わせ対応タスクで性能が人手に近い水準まで向上し、プロセス全体が61.9%改善、トークンコストが3分の1に低下したという）④Closed loop（記事では詳細未記載）。ハーネス改善の具体的なアルゴリズム・評価指標までは出典に記載がない（出典: [MONOist — 2026年のAI開発最前線](https://monoist.itmedia.co.jp/mn/articles/2610/07/news019_2.html)、取得日2026-10-25）

## 実務での使い方
- 国産オープンウェイトモデルを「日本語の精度」と「商用利用のライセンスの明確さ」の両方で評価したい場合の選択肢の一つになる
- 自社でホスティングしてデータを外に出さない運用をしたい企業（金融・医療など）にとって、国産モデルは選定理由になりやすい

## 講座で使うなら
- 30 秒説明: 「KDDI系の会社が、国立情報学研究所の日本語モデルをさらに強化して無料公開しました。商用利用もできます」
- たとえ話: 国産の素材（LLM-jp-4）を仕入れて、日本語の味付けを追加して店に出す
- 演習案: 受講者に「自社でモデルを動かす（オープンウェイト）」と「API越しに使う（GPT・Claude等）」のどちらが向いているかを、データの扱いとコストの観点で比較させる

## この話題の流れ
<!-- agent が日付順に追記。新しいものを上に -->
- 2026-10-25（週次整理・要追記対応）: RSIへの道筋を4段階（Human-only→Human-in-the-loop→Human-on-the-loop→Closed loop）で説明する記事を確認。第3段階では問い合わせ対応タスクのプロセス全体が61.9%改善、トークンコストが3分の1に低下したという（[出典](https://monoist.itmedia.co.jp/mn/articles/2610/07/news019_2.html)、取得日2026-10-25）
- 2026-10-03: LLM-jp-4ベースの強化モデル2種をApache 2.0ライセンスでHugging Face上に無料公開。一部ベンチマークでNIIの新しい「LLM-jp-4.1」を上回るスコアを記録。社内研究組織「ELYZA RSI Research」による「再帰的自己改善」に向けた準備段階の成果と位置づけ（[daily](../daily/2026-10-03.md) / [threads/japan-ai-adoption](../threads/japan-ai-adoption.md)）

## 関連
- [threads/japan-ai-adoption](../threads/japan-ai-adoption.md)
