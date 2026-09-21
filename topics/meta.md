---
type: topic
title: "Meta（メタ）"
slug: meta
created: 2026-09-03
updated: 2026-09-22
tags: [meta, speech, agent]
level: beginner
audience: [engineer, business, instructor]
related: [topics/openai.md, topics/anthropic.md, topics/google.md]
---

# Meta（メタ）

## 一言で
Facebook・Instagram・WhatsAppなどを運営する米国のテクノロジー企業。「Meta Superintelligence Labs」を中心にAIモデルの開発を進め、Llamaファミリーのオープンウェイトモデルに加え、音声・マルチモーダルの新モデルも展開している。

## 仕組み
- AI開発部門「Meta Superintelligence Labs」が、対話・コーディング（Muse Code）・音声認識（Muse Voice Transcribe）など複数の製品ラインを開発
- Llamaファミリーはオープンウェイトモデルとしてライセンス配布されており、企業が自社環境で動かす選択肢を提供している。「Llama 4 Community License」では、ライセンシー（関連企業含む）の月間アクティブユーザーが直前の暦月で700万人を超える場合、Metaから別途ライセンスを取得する必要がある。無償利用は禁止ではないが一定規模を超えると事前承認が必要で、"Built with Llama" の表示義務・無保証・間接損害の免責も定められている（出典: [Llama 4 Community License Agreement](https://developer.meta.com/ai/llama4/license/)、取得日 2026-09-06）
- 2026年9月、初のリアルタイム音声認識モデル「Muse Voice Transcribe」を発表。ストリーミング音声認識・話者分離・発話終了検知を単一モデルで処理する設計

## 実務での使い方
- オープンウェイトのLlamaは、社外にデータを出したくない企業が自社インフラで動かす選択肢になる（要追記：導入事例）
- Muse Voice Transcribeのような低遅延・低コストの音声認識は、会議の議事録作成や複数話者インタビューの文字起こしなど、話者識別が必要な業務の自動化に使える

## 講座で使うなら
- 30 秒説明: 「SNSでおなじみのMetaが、無料で使えるAIモデル（Llama）と、会議の文字起こしのような実務ツール（Muse Voice Transcribe）の両方を出している会社です」
- たとえ話: 誰でも使える基礎部品（オープンウェイトモデル）と、すぐ使える完成品アプリ（音声認識ツール）の両方を用意している
- 演習案: 自社の会議の議事録作成にかかっている時間を書き出させ、自動文字起こしツールでどこまで削減できそうか試算させる

## この話題の流れ
<!-- agent が日付順に追記。新しいものを上に -->
- 2026-09-22: Amazonが、Museによる自社サイトでの買い物代行をブロック。「無許可のAIエージェントによる継続的アクセスは利用規約違反」とのエラーが表示されるようになった。Amazonは自社の基盤モデル・推論プラットフォームを持ち競合ツールを受け入れる法的義務がない上、誤発注時の顧客・販売者対応への実務上の懸念も背景（[daily](../daily/2026-09-22.md) / [topics/amazon](amazon.md)）
- 2026-09-22: 米国・カナダ限定ながら、公開後最初の12日間でiOSダウンロード180万件（ChatGPT初期の130万件を上回る）、米国内の日次アクティブユーザーも64万2,000人（ChatGPT同時期の23万1,000人超）に達したとTechCrunchが報道。全世界・両OS合算では280万インストールで米App Storeで総合1位に浮上（[daily](../daily/2026-09-22.md) / [topics/openai](openai.md)）
- 2026-09-19: パーソナルAIエージェント「Muse」をMacに拡大。ファイル管理・メッセージ送受信・カレンダー操作・メモ作成などパソコン上の作業を代行できるようになった。機密性の高い操作には事前許可が必要な設計（[daily](../daily/2026-09-19.md)）
- 2026-09-17: ザッカーバーグCEOが、AI業界協調による開発速度制限に異を唱えるXの投稿。各社には「自らのモデルを安全に訓練できるペースで開発を進める責任がある」とし、独立評価者の活用は推奨しつつ業界横断の協調は求めない立場を示した。Anthropic・OpenAIが主導した"協調減速"論への公然たる異論（[daily](../daily/2026-09-17.md) / [threads/ai-safety-regulation](../threads/ai-safety-regulation.md)）
- 2026-09-16: 「WhatsApp Business Tools MCP」サーバーを公開。Claude・Cursor・Codex・ChatGPTなどのAIコーディングエージェントに、アカウント作成・電話番号認証・Cloud API登録・メッセージテンプレートの作成編集・Webhookテストまでを会話形式で任せられる（[daily](../daily/2026-09-16.md) / [topics/mcp](mcp.md)）
- 2026-09-11（続報）: 米国限定提供のパーソナルAIエージェント「Muse」が、9月10日時点で米App Store総合2位に浮上。iOSダウンロード数は8万3,000件超だが、Google PlayではProductivityカテゴリ338位と低迷。Threadsの初日430万ダウンロードと比べると立ち上がりは緩やか（[daily](../daily/2026-09-11.md)）
- 2026-09-09: パーソナルAIエージェント「Muse」（Muse Sparkモデル搭載）を米国で提供開始。メール送信・旅行予約・請求書見直し・フォーム入力・買い物代行などをこなし、Web・iOS・Android・WhatsAppに対応（将来はAIグラスにも展開予定）。無料プランのほかPower（月20ドル）・Maximum（月100ドル）を用意。2011年以降複数回のFTC和解歴やCambridge Analytica事件、直近の18億ドル規模の集団訴訟和解という文脈のなか、消費者の信頼を得られるかが焦点（[daily](../daily/2026-09-09.md)）
- 2026-09-04: コーディング・エージェント向け新モデル「Muse Spark 1.3」を公開。DeepSWE v1.1で75.4点・MRCR（512K〜1M）で98.1点。プロンプト・出力の提供と引き換えに入出力価格を最大95%割引する「貢献者向け価格」も導入（[daily](../daily/2026-09-04.md)）
- 2026-09-03: 初のリアルタイム音声認識モデル「Muse Voice Transcribe」を発表。70以上の言語（日本語含む25言語検証済み）に対応、20人以上の話者を区別可能。単語誤り率3.1%、発話終了からの遅延0.16秒。Meta Model APIで1時間0.18ドル（[daily](../daily/2026-09-03.md)）

## 関連
- [topics/openai](openai.md)
- [topics/anthropic](anthropic.md)
- [topics/google](google.md)
