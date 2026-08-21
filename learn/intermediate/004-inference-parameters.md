---
type: learn
track: intermediate
number: 004
title: "推論時のパラメータ：temperature / top-p / max tokens を実務でどう決めるか"
date: 2026-08-22
level: intermediate
audience: [engineer, business]
tags: [prompt-engineering, api]
reading_minutes: 4
sources:
  - url: https://platform.claude.com/docs/en/api/messages
    title: "Messages API — Claude Docs"
    fetched: 2026-08-22
related: [topics/claude-code.md]
---

# 004 推論時のパラメータ：temperature / top-p / max tokens を実務でどう決めるか

!!! abstract "この記事で説明できるようになること"
    - temperature・top_p・max_tokens がそれぞれ何を制御しているか
    - なぜ「temperature と top_p を両方いじる」のが推奨されないか
    - 業務用途ごとにどう値を決めればよいか

## 仕組み

LLM は次のトークンの確率分布を計算し、そこからサンプリングして 1 トークンずつ出力を生成する。推論時のパラメータは、この「確率分布からどう選ぶか」を調整する。

- **temperature**：確率分布の「尖り具合」を変える。Anthropic の Messages API では 0.0〜1.0（デフォルト 1.0）。0 に近いほど最も確率の高いトークンばかり選ぶ決定的な出力になり、1 に近いほど多様で意外性のある出力になる
- **top_p（nucleus sampling）**：確率の高いトークンから順に足し合わせ、累積確率が top_p に達するまでの候補だけからサンプリングする。ロングテールの低確率トークンを切り捨てる仕組み
- **top_k**：確率の高い上位 k 個のトークンだけからサンプリングする、よりシンプルな絞り込み
- **max_tokens**：生成できるトークン数の上限。モデルがこれに達する前に自然に終了することもある

Anthropic の公式ドキュメントでは、temperature と top_p はどちらも「サンプリングの絞り込み」という同じ役割を別の角度から行うものであり、top_p・top_k は「高度なユースケース向け」、通常は temperature 単独の調整が基本とされている。

## 比較・判断基準

| 用途 | temperature の目安 | 理由 |
|---|---|---|
| 事実確認・分類・コード生成など「正解がある」タスク | 0.0〜0.3 | 出力のブレを抑え、再現性を優先する |
| 通常の対話・要約 | 1.0（デフォルト） | バランス重視 |
| ブレインストーミング・コピー案の複数出し | 1.0 前後、複数回サンプリング | 多様性を優先する |

## 落とし穴

1. **temperature を 0 にすれば必ず同じ出力になると思い込む**：0 に近づけても完全な決定性は保証されない（実装や並列処理の影響を受けうる）
2. **temperature と top_p を両方大きく動かして「効果が読めなくなる」**：どちらも絞り込みの役割が重なるため、まず片方（多くは temperature）だけを動かし、必要な場合のみもう一方を高度な調整として足す
3. **max_tokens を小さくしすぎて出力が途中で切れる**：JSON など構造化出力では、途中で切れるとパース不能になる。想定する最長出力より余裕を持たせる

## 実務への接続

業務での自動化スクリプト（分類・抽出・定型文生成）では temperature を下げて再現性を優先し、アイデア出しや文章のバリエーション作成では temperature を上げて複数案を生成させると使い分けやすい。RAG や社内 FAQ 生成のように「事実から外れてはいけない」タスクは、temperature を下げるだけでなく、プロンプト側で「分からない場合は分からないと答える」よう指示することも合わせて必要。

## 講座で使うなら
- 30 秒説明: 「temperature は AI の“気まぐれ度合い”のつまみです。0 に近づけると毎回同じような手堅い答えになり、1 に近づけると意外性のある答えが出やすくなります」
- たとえ話: 同じ料理人に「いつも通りの味で」と頼むか「今日は冒険していいよ」と頼むかの違い
- 演習案: 同じプロンプトを temperature 0 と 1 でそれぞれ 3 回ずつ実行させ、出力のブレを受講者に比較させる

## 出典・参考
- [Messages API — Claude Docs](https://platform.claude.com/docs/en/api/messages)（取得日 2026-08-22）

## 関連
- [topics/claude-code](../../topics/claude-code.md)
