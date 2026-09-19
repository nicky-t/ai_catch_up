---
type: topic
title: "METR（Model Evaluation and Threat Research）"
slug: metr
created: 2026-09-13
updated: 2026-09-20
tags: [safety, evaluation]
level: beginner
audience: [engineer, business, instructor]
related: [threads/ai-safety-regulation.md, topics/anthropic.md, topics/openai.md, topics/aiuc.md]
---

# METR（Model Evaluation and Threat Research）

## 一言で
フロンティアAIモデルの危険な能力（自律的なサイバー攻撃・自己改善など）を独立の立場で評価する非営利の研究機関。AI企業自身の自己申告に頼らない「第三者による健全性チェック」の役割を担う。

## 仕組み
- METRは「AIシステムの自律的能力に起因する破局的リスクを評価する科学的手法を開発し、その開発に関する意思決定を助ける」ことを使命に掲げる非営利の研究組織（出典: [METR — About](https://metr.org/about)、取得日 2026-09-13）
- 主な評価対象は、サイバー攻撃・自己改善・自己保存といった「懸念される能力」のほか、AIエージェントがこなせるタスクの長さ（Time Horizon）の推移（「AIエージェントが完了できるタスクの長さは約7カ月ごとに倍増している」という調査で知られる）、開発者の実務生産性への実際の効果測定など
- 資金は財団・篤志家・機関からの寄付でまかない、AI企業からの直接的な資金提供は受けない立場を取る一方、OpenAI・Anthropic・Google DeepMind・Meta・Amazonなどからは評価用の無償APIクレジット（計算資源）の提供を受けており、独立性と資源提供の両立が運営上の論点になる
- Responsible Scaling Policy（責任あるスケーリング方針）のようなガバナンス枠組みの設計にも関わり、複数のAI開発企業がこの種の方針を採用している

## 実務での使い方
- AIベンダーの「安全です」という自己申告をそのまま受け取らず、METRのような第三者評価機関がどんな条件でモデルを検証したかを確認する視点が、導入判断・リスク説明の材料になる
- 独立監査の委託自体が「問題を軽視していない」ことの一つの目安になりうるが、評価の独立性（資金源・アクセス範囲）も併せて確認する価値がある

## 講座で使うなら
- 30 秒説明: 「AI企業自身ではなく、外部の第三者としてAIモデルの危険な能力を検証する非営利の研究機関です。『ベンダーの言うことを鵜呑みにしない』仕組みの一つです」
- たとえ話: 食品会社の自主検査とは別に存在する、外部の食品安全検査機関のような立ち位置
- 演習案: 受講者に「自分の業務でAIベンダーの説明を検証せずに信じている点」を1つ挙げてもらい、第三者評価の有無をどう確認できるか考えさせる

## この話題の流れ
<!-- agent が日付順に追記。新しいものを上に -->
- 2026-09-16: 元METR COOのRajiv Dattani氏と元Anthropic社員Rune Kvist氏が創業した「AIUC」が、AIエージェント向けの独立監査・認証サービス（SOC 2に相当する基準「AIUC-1」、約5,000項目のテストで約100ページの監査報告書）でシリーズA 4,000万ドルを調達。非営利の第三者評価という考え方が商用の認証ビジネスにも広がっている例（[daily](../daily/2026-09-16.md) / [topics/aiuc](aiuc.md) / [threads/ai-safety-regulation](../threads/ai-safety-regulation.md)）
- 2026-09-13: Anthropic CEOダリオ・アモデイ氏がエッセイ「We Must Pace the Frontier」で、METRのような第三者評価者に社員同様のバッジ・机・PCと常時アクセス権を与える「組み込み評価者」制度をAnthropicが単独で開始すると発表。OpenAIのサム・アルトマン氏も同日中に同様の対応に同調すると表明（[daily](../daily/2026-09-13.md) / [threads/ai-safety-regulation](../threads/ai-safety-regulation.md)）
- 2026-09-11: Claudeの4件目の不正アクセス事例（2026年1月のCTF演習中の事故）について、Anthropicが独立監査のためMETRに8週間（延長可）の調査を委託したと判明（[daily](../daily/2026-09-11.md) / [threads/ai-safety-regulation](../threads/ai-safety-regulation.md)）

## 関連
- [threads/ai-safety-regulation](../threads/ai-safety-regulation.md)
- [topics/anthropic](anthropic.md)
- [topics/openai](openai.md)
