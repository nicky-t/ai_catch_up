---
type: topic
title: "Amazon（アマゾン）"
slug: amazon
created: 2026-09-12
updated: 2026-09-22
tags: [amazon]
level: beginner
audience: [engineer, business, instructor]
related: [topics/openai.md]
---

# Amazon（アマゾン）

## 一言で
EC・クラウド（AWS）・広告事業を持つ米国のテクノロジー企業。自社AI（Alexa+など）に加え、広告配信網（Amazon DSP）やクラウド基盤を他社のAI事業と組み合わせる「土台としてのAI活用」が特徴。

## 仕組み
- クラウド事業のAWSは、OpenAIを含む複数のAI企業のモデル提供・実行基盤としても使われる（要追記：AWSとOpenAIのインフラ提携の詳細）
- 広告事業「Amazon Ads」は、自社ECサイトだけでなく他社サービス上での広告配信網（Amazon DSP）を持つ。2026年9月、OpenAIとの提携でChatGPT内への広告配信を開始した
- 自社AIアシスタント「Alexa+」は、Amazon Nova（自社モデル）とAnthropicのモデル両方を組み合わせた新アーキテクチャに刷新。数日にまたがる文脈を記憶した対話、飲食予約・配車手配・サービス予約の代行などエージェント的な機能、Ring連携のカメラ監視やカレンダー同期を特徴とする。料金はPrime会員なら無料、非会員は月額19.99ドル（無料の文字チャット版は機能制限あり）。刷新後は利用回数が旧Alexa比で2倍超、単純な定型リクエストからより複雑な対話への利用シフトが見られるという（出典: [Amazon公式 — Alexa+ now available to everyone in the US](https://www.aboutamazon.com/news/devices/alexa-plus-available-free-prime-members-us)、取得日 2026-09-20）

## 実務での使い方
- 広告主にとっては、Amazon DSP経由でChatGPTという新しい広告面にリーチできる選択肢が増えた。Amazon DSPのマネージドサービスとして提供され、Amazon側の担当チームがキャンペーン設定・最適化を支援し、ターゲティングにはAmazonの自社データ（ファーストパーティーデータ）を利用できる。ただし具体的な審査基準・出稿条件は現時点で公表されておらず、米国の一部広告主に限定したパイロット段階（出典: [ITmedia NEWS — Amazon、OpenAIと広告提携](https://www.itmedia.co.jp/news/article/2609/11/2000001396/)、取得日 2026-09-13）
- 自社サービスがAWS基盤上で動いている場合、他社AI連携の技術的な相性を確認しやすい

## 講座で使うなら
- 30 秒説明: 「EC・クラウド・広告と手広く事業を持つAmazonが、2026年からOpenAIとの提携でChatGPTの広告面にも進出した会社です」
- たとえ話: 街のあらゆる場所に看板を出す広告代理店が、AIチャットの回答欄という新しい看板スペースを見つけた
- 演習案: 「無料のAIチャットに広告が入ること」について、検索エンジン広告との違いを受講者に議論させる

## この話題の流れ
<!-- agent が日付順に追記。新しいものを上に -->
- 2026-09-22: Metaのパーソナルエージェント「Muse」による自社サイトでの買い物代行をブロック。「無許可のAIエージェントによる継続的アクセスは利用規約違反」とのエラーメッセージが表示されるようになった。自社の基盤モデル・推論プラットフォームを持ち競合ツールを受け入れる法的義務がない点、誤発注時の顧客・販売者対応への実務上の懸念が背景とみられる（[daily](../daily/2026-09-22.md) / [topics/meta](meta.md)）
- 2026-09-12: Amazon AdsがOpenAIと提携し、Amazon DSPの広告主がChatGPT内（Free・Goプランの成人ログインユーザー向け）に広告を出稿できる仕組みを発表。米国限定のパイロット運用（[daily](../daily/2026-09-12.md) / [topics/openai](openai.md)）

## 関連
- [topics/openai](openai.md)
- [topics/meta](meta.md)
