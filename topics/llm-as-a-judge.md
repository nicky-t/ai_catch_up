---
type: topic
title: "LLM-as-a-judge（LLMによる出力評価）"
slug: llm-as-a-judge
created: 2026-09-26
updated: 2026-09-26
tags: [evaluation]
level: beginner
audience: [engineer, business, instructor]
related: [learn/intermediate/039-llm-as-a-judge.md]
---

# LLM-as-a-judge（LLMによる出力評価）

## 一言で
AIの出力（要約・チャットの返答など）が良いかどうかを、人間ではなく別のAIに判定させる評価手法。

## 仕組み
- 代表的な3パターン：①Likert scale（1〜5などの尺度でトーン・共感性を採点）②binary classification（個人情報の露出などをyes/noで判定）③ordinal scale（会話の文脈活用度など順序で比較）
- 判定精度を上げる基本設計は「出力形式を数値・yes/noに絞る」「採点基準を段階ごとに明文化する」「生成に使ったモデルとは別のモデルで判定する」の3点（出典: [Anthropic公式ドキュメント](https://platform.claude.com/docs/en/build-with-claude/develop-tests)、取得日 2026-09-26）
- 判定役のLLM自身にも、先に提示した回答を高く評価しやすい「position bias」、内容より長さで「良い」と判定しやすい「verbosity bias」などの癖があることが知られている

## 実務での使い方
- プロンプトやモデルを変更するたびに大量のテストケースを自動採点し、品質の劣化（リグレッション）を検知する「継続的評価」の土台に使う
- 誤りの影響が大きい領域（契約書チェック・医療情報など）では、LLM判定は一次スクリーニングに留め、最終判断は人が行う設計にする

## 講座で使うなら
- 30 秒説明: 「AIの答え合わせを別のAIにやらせる方法です。ただし採点役のAIにも癖があります」
- たとえ話: 生徒の作文の下読みを別の採点係に任せるが、その採点係が「長い作文=良い作文」と勘違いしていないか時々チェックする必要がある
- 演習案: 受講者が使っているAIの出力を1つ選び、Likert scaleとbinary classificationのどちらで自動採点できそうか議論させる

## この話題の流れ
<!-- agent が日付順に追記。新しいものを上に -->
- 2026-09-26: 中級学習記事039「LLM-as-a-judge：AIの出力をAIで評価する設計と落とし穴」で、代表的な評価パターンと落とし穴を整理（[daily](../daily/2026-09-26.md) / [learn/intermediate/039](../learn/intermediate/039-llm-as-a-judge.md)）

## 関連
- [topics/claude-code](claude-code.md)
