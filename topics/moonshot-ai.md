---
type: topic
title: "Moonshot AI（ムーンショットAI／Kimi）"
slug: moonshot-ai
created: 2026-10-11
updated: 2026-10-11
tags: [open-weights, benchmark]
level: beginner
audience: [engineer, business, instructor]
related: [topics/deepseek.md, topics/openrouter.md, threads/ai-safety-regulation.md]
---

# Moonshot AI（ムーンショットAI／Kimi）

## 一言で
チャットAI・モデル「Kimi」を開発する中国のAIラボ。DeepSeekと並び、オープンウェイト・低コストで欧米フロンティアモデルに迫る性能を示す中国系AI企業の代表格として、複数のニュースで名前が挙がる。

## 仕組み
- 主力モデルは「Kimi」シリーズ。最新の「Kimi K3」はコーディング評価SWE-bench VerifiedでOpenAI・Anthropicの上位モデルと1.2ポイント差に迫り、コストはClaude Opus 4.8の約半分・Claude Fable 5の約3分の1とされる（出典: 調査会社RedMonkの分析、[daily 2026-10-10](../daily/2026-10-10.md)）
- 2026年9月8日、米NSA・CISA・FBIが、DeepSeek・Moonshot AI・Alibaba Group・MiniMax・StepFun・Z.AIの6社について、米国製フロンティアAIモデルから「知識蒸留」の手法で機能を抽出していると警告（[daily 2026-09-18](../daily/2026-09-18.md)）
- 2026年10月2日、OpenAIは自社モデルの推論過程（protected model reasoning）を狙った組織的な「蒸留」キャンペーンを阻止したと公表し、活動の中核をMoonshot AI関連人物によるものと結論づけた（[daily 2026-10-02](../daily/2026-10-02.md)）

## 実務での使い方
- コスト重視でモデルを選定する際、Kimi K3はDeepSeekと同様に「性能はフラッグシップ級に接近・価格は大幅に低い」という比較対象になる。ただし知的財産（蒸留疑惑）・データの扱いに関する論争が継続中である点は選定時に留意が必要
- オープンモデルでの安全性検証（例: Goodfireの「inside-out」モニター）にKimi K3が検証対象として使われるなど、研究コミュニティでの参照モデルの一つになっている（[daily 2026-10-09](../daily/2026-10-09.md)）

## 講座で使うなら
- 30 秒説明: 「Kimiというチャットモデルを作る中国のAIラボ。DeepSeekと並んで、低コスト・オープンウェイトで欧米勢に迫る性能を出しています」
- たとえ話: 大手ブランドの新車が出るたびに、ほぼ同じ性能を数分の一の価格で追走するチャレンジャーメーカー
- 演習案: 「性能が近づくほど、価格以外の判断基準（データの扱い・蒸留疑惑などの論争）が重要になる」という点を、DeepSeekの価格競争の事例と比較しながら議論させる

## この話題の流れ
<!-- agent が日付順に追記。新しいものを上に -->
- 2026-10-10: 調査会社RedMonkの分析で、仲介サービスOpenRouterのトークン使用量に占める中国系モデルの割合が2025年末の約4.5%から2026年7月の1週間で約63%に急上昇したと判明。「Kimi K3」はコーディング評価SWE-bench VerifiedでOpenAI・Anthropicの上位モデルと1.2ポイント差に迫り、コストはClaude Opus 4.8の約半分・Claude Fable 5の約3分の1とされる（[daily](../daily/2026-10-10.md) / [topics/openrouter](openrouter.md)）
- 2026-10-09: 解釈可能性スタートアップGoodfireが、モデル内部の活性化信号を直接読む「inside-out」モニターをオープンモデル「Kimi K3」で検証。約1,500セッションの監視コストがprobe方式で約51ドルと、低コストAI監視（233ドル）・最上位AIモデル監視（約1万ドル）より大幅に安く、悪意あるセッションの94%を検知した（[daily](../daily/2026-10-09.md) / [threads/ai-safety-regulation](../threads/ai-safety-regulation.md)）
- 2026-10-02: OpenAIが、自社モデルの推論過程を狙った組織的な「蒸留」キャンペーンを阻止したと公表。7月1日ごろ開始、7月24〜25日には4,000超のユーザーから約1.6万件のリクエストが急増し関連クラスタは1.5万人超に及んだが、7月28日までに全面阻止。活動の中核を中国Moonshot AI（「Kimi」開発元）関連人物によるものと結論づけた（[daily](../daily/2026-10-02.md) / [topics/openai](openai.md)）
- 2026-09-18: 米NSA・CISA・FBIが、中国のAI企業6社（DeepSeek・Moonshot AI・Alibaba Group・MiniMax・StepFun・Z.AI）が米国製フロンティアAIモデルから「知識蒸留」の手法で機能を抽出していると警告（9月8日発表）。APIプロキシの悪用やプロンプトインジェクションなどの抽出手法をMITRE ATLASフレームワークとともに列挙（[daily](../daily/2026-09-18.md) / [topics/deepseek](deepseek.md) / [threads/ai-safety-regulation](../threads/ai-safety-regulation.md)）

## 関連
- [topics/deepseek](deepseek.md)
- [topics/openrouter](openrouter.md)
- [threads/ai-safety-regulation](../threads/ai-safety-regulation.md)
