---
type: topic
title: "DeepSeek（ディープシーク）"
slug: deepseek
created: 2026-09-11
updated: 2026-09-18
tags: [deepseek, open-weights]
level: beginner
audience: [engineer, business, instructor]
related: [topics/openrouter.md, topics/qwen.md, topics/glm.md]
---

# DeepSeek（ディープシーク）

## 一言で
中国発のAIラボ。オープンウェイトの大規模言語モデルを低価格・高性能で提供し続け、欧米の主要ラボとの価格・性能競争の震源地の一つになっている。

## 仕組み
- モデルはMoE（Mixture of Experts、専門家混合）アーキテクチャを採用し、パラメータ規模の割に推論コストを抑える設計を特徴とする
- API料金は「キャッシュヒット時」「キャッシュミス時」で入力価格が分かれ、ピーク・オフピークでも変動する時間帯別料金制を採用。ピーク時間帯は毎週月〜金曜のUTC 01:00〜04:00・06:00〜10:00で、それ以外はオフピーク（オフピーク料金はピークの半額）。現行の主力モデルは、軽量版「DeepSeek-Flash」がオフピークで入力0.003ドル（キャッシュヒット時）／0.15ドル（キャッシュミス時）・出力0.6ドル（100万トークンあたり）、上位版「DeepSeek-V4-Pro」がオフピークで入力0.022ドル／0.66ドル・出力1.98ドルと、モデルの格に応じて価格帯が分かれる（出典: [DeepSeek API Docs — Models & Pricing](https://api-docs.deepseek.com/quick_start/pricing)、取得日 2026-09-13。過去の改定の全履歴は公式ドキュメントに記載がなく未確認）
- モデル・重み（ウェイト）を公開するオープンウェイト路線を取り、OpenRouterなど他社サービス経由でも広く使われている（[topics/openrouter](openrouter.md)）

## 実務での使い方
- 低コストでフラッグシップ級の性能をうたうモデルは、コスト重視のバッチ処理・大量トークンを消費する用途で検討価値がある（要追記：日本語性能・実務での比較検証）
- 料金改定が頻繁なため、コスト試算は契約時点の料金表を都度確認する必要がある

## 講座で使うなら
- 30 秒説明: 「中国発のAIラボで、性能を保ちながら価格を抑えたモデルを次々出し、欧米ラボとの価格競争を引っ張っています」
- たとえ話: 高性能な自転車を大手メーカーの半額以下で出し続けるチャレンジャーブランド
- 演習案: 同じ作業をGPT系・Claude系・DeepSeek系のモデルで見積もった場合のトークン単価を比較させ、性能差とコスト差のどちらを優先するか議論させる

## この話題の流れ
<!-- agent が日付順に追記。新しいものを上に -->
- 2026-09-18: 米NSA・CISA・FBIが、中国のAI企業が米国製フロンティアAIモデルから「知識蒸留」の手法で機能を抽出し、低コストで効率的な自社モデルの開発に利用していると警告（9月8日発表）。対象としてDeepSeek・Moonshot AI・Alibaba Group・MiniMax・StepFun・Z.AIの6社を挙げ、APIプロキシの悪用やプロンプトインジェクションなどの抽出手法をMITRE ATLASフレームワークとともに列挙（[daily](../daily/2026-09-18.md) / [threads/ai-safety-regulation](../threads/ai-safety-regulation.md)）
- 2026-09-11: 552BパラメータのMoEモデル「DeepSeek-V4.1-Flash」を発表。KVキャッシュ要件を削減する改良アーキテクチャで、GPT-5.6 SolやClaude Opus 5を一部ベンチマークで上回ると主張。8月13日の値上げから一転し、オフピーク料金を入力0.003ドル（キャッシュヒット時）／出力0.6ドル（100万トークンあたり）に値下げ（[daily](../daily/2026-09-11.md)）

## 関連
- [topics/openrouter](openrouter.md)
- [topics/qwen](qwen.md)
- [topics/glm](glm.md)
