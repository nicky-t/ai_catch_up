---
type: topic
title: "Qwen（通義千問）"
slug: qwen
created: 2026-08-25
updated: 2026-08-31
tags: [qwen, open-weights]
level: beginner
audience: [engineer, business, instructor]
related: [topics/glm.md]
---

# Qwen（通義千問）

## 一言で
中国Alibaba Cloudが開発するオープンウェイト（重み公開）のLLMファミリー。小〜中規模のモデルサイズでも高いコーディング性能を出す路線で、個人のPCでも動かせる現実的な選択肢として注目を集めている。

## 仕組み
- 2026年8月、300億パラメータ級モデル「Qwen3.8-27B」を公開。SWE-bench Pro（61.7点）やLiveCodeBench v6など複数のベンチマークでClaude Opus 4.6を上回ったと報じられているが、これらはいずれもAlibaba自身が計測・公表した数値。第三者ベンチマークのArtificial Analysis Intelligence Index（52ポイント）は測定済みだが、SWE-bench Pro等の個別スコアについては本稿執筆時点（2026-08-30）で第三者による独立検証・再現の報告は確認できていない（未検証、要継続確認）
- 同時期にMeta「Muse Glimmer」（24GB VRAM対応）、NVIDIA「Nemotron 3.5 Lightning」（3B MoE構成）など、他社からも30Bクラス前後のオープンモデルが相次いで公開された（要追記：各モデルの詳細な仕様比較）

## 実務での使い方
- パラメータ数が小さいため個人のPCやローカル環境での運用が現実的になり、API課金を抑えたいタスクの候補になる（要追記：日本語性能・商用ライセンス条件の確認）
- 「巨大モデル1つに頼る」のではなく、タスクごとに小型オープンモデルと大型クローズドモデルを使い分ける設計の選択肢が広がっている

## 講座で使うなら
- 30 秒説明: 「Alibabaが作る中国発のオープンモデルです。サイズを抑えながらコーディング性能を大きく伸ばしていて、個人のPCでも動かせるのが特徴です」
- たとえ話: 大排気量の高級車（大型クローズドモデル）に対して、燃費と取り回しの良いコンパクトカーが性能面でも追いついてきた状況
- 演習案: 「自分の業務タスクなら、大型クローズドモデルと小型オープンモデルのどちらで十分か」を受講者に判定させる

## この話題の流れ
<!-- agent が日付順に追記。新しいものを上に -->
- 2026-08-30: JetBrainsが、Qwen3.6-27Bを4ビット量子化しMac上で完結させたコーディングエージェント「Junie Local」を提供開始。社内テストではClaude Sonnet 4.5と同等の性能（[daily](../daily/2026-08-31.md) / [topics/claude-code](claude-code.md)）
- 2026-08-25: 「Qwen3.8-27B」がSWE-bench Pro等でClaude Opus 4.6超えと報告。Meta・NVIDIAなど各社の30Bクラスオープンモデル公開ラッシュの一角として紹介（[daily](../daily/2026-08-25.md)）

## 関連
- [topics/glm](glm.md)（同じくオープンウェイト路線の中国発モデル）
