---
type: topic
title: "Transformer（トランスフォーマー）"
slug: transformer
created: 2026-08-19
updated: 2026-08-19
tags: [paper, context-window, scaling]
level: beginner
audience: [engineer, business, instructor]
related: [learn/intermediate/001-transformer-self-attention.md]
---

# Transformer（トランスフォーマー）

## 一言で
現在の LLM（GPT / Claude / Gemini など）のほぼ全てが採用する土台の設計。「文中の各語が、他の全ての語を同時に見て、関係が強い語を重く参照する」自己注意（self-attention）が核。会議室で全員が同時に「誰の話が自分に関係あるか」を見回すイメージ。

## 仕組み
- 2017 年の論文「Attention Is All You Need」（Vaswani ら、Google）で提案。RNN / CNN を使わず注意機構のみで構成し、並列計算しやすく学習が速い
- 各トークンから Query / Key / Value の 3 ベクトルを作り、Query と Key の内積で関連度 → softmax で重み → Value の加重平均、を複数の頭（multi-head）で並列に行う
- 語順は位置エンコーディング（positional encoding）で補う
- よくある誤解：「長文を全部均等に読んでいる」「意味を理解している」。実際は統計的な重み付けで、注意計算のコストは長さの 2 乗で増える

## 実務での使い方
- 直接「使う」ものではなく、プロンプト設計・RAG・コスト見積もりの**前提知識**。重要な指示は目立つ位置に置く、文脈は絞って渡す、長文常用はコストに効く、という判断の根拠になる
- モデル比較の記事で「Transformer ベース」「アーキテクチャ改良」と出てきたときに読み解ける

## 講座で使うなら
- 30 秒説明: 「LLM は 1 語ずつ『他のどの語を見れば自分の意味が決まるか』を全語に問い合わせて理解します。だから前後の文脈で答えが変わります」
- たとえ話: 会議室で全員が同時に互いの名札（Key）を見て、関係が強い人の話（Value）を多めに聞く
- 演習案: 短い文書に「注目すべき語」を手で線で結び、AI の要約と重点を比べる

## この話題の流れ
<!-- agent が日付順に追記。新しいものを上に -->
- 2026-08-19: 中級 001 で自己注意を解説 — Q/K/V・多頭注意・位置エンコーディング・2 乗コスト（[learn](../learn/intermediate/001-transformer-self-attention.md) / [daily](../daily/2026-08-19.md)）

## 関連
- [learn/intermediate/001](../learn/intermediate/001-transformer-self-attention.md)
- 今後作成予定: topics/context-window（要追記）
