---
type: topic
title: "NVIDIA（エヌビディア）"
slug: nvidia
created: 2026-08-28
updated: 2026-10-29
tags: [nvidia, agent, safety]
level: beginner
audience: [engineer, business, instructor]
related: [topics/hugging-face.md, topics/anthropic.md, topics/jalapeno.md]
---

# NVIDIA（エヌビディア）

## 一言で
AIモデルの学習・推論に使われるGPU（画像処理用半導体）を主力とする米国の半導体企業。AIブームの計算需要をほぼ一手に引き受け、AI企業各社の計算基盤契約・投資の中心的な存在になっている。

## 仕組み
- 主力製品はデータセンター向けGPU。世代ごとに「Vera Rubin」のような開発コード名が付き、AI各社が次世代チップの調達を競っている。世代は Hopper（2022年〜、機密コンピューティングを初導入）→ Blackwell（2024年〜、FP32マトリックス演算 227 TFLOPS・NVLink帯域 1,800 GB/s）→ Rubin / Vera Rubin（2026年後半〜、FP32マトリックス演算 400 TFLOPS・NVLink帯域 3,600 GB/s・HBM4メモリでBlackwell比約2.8倍の帯域）と進み、年1回のペースで刷新している（出典: [NVIDIA Technical Blog — Inside the NVIDIA Vera Rubin Platform](https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/)、取得日 2026-08-30）
- 自社製品の販売だけでなく、有望なAI関連企業への出資（例：Hugging Faceへの出資提案）や、自社チップを使う企業への大型計算基盤契約という形でもエコシステムに関わる
- 2026年9月3日、AIモデル共有プラットフォームのHugging Faceを129.3億ドルで買収することに正式合意した（[topics/hugging-face](hugging-face.md)）

## 実務での使い方
- AI導入のコスト構造を理解する上で、モデル提供企業（OpenAI・Anthropicなど）だけでなく、その計算基盤を支えるNVIDIAの動向（供給状況・チップ価格）も間接的にサービス価格に影響しうる点を押さえておく。具体例として、NVIDIAがサーバー向けメモリをDDR5からスマートフォン向けで使われるLPDDR方式へ切り替える方針を進めており、市場規模の桁違いな買い手（スマートフォン大手並みの調達規模）の急な参入でメモリ需給が逼迫し、調査会社Counterpoint Researchはサーバー向けメモリ価格が2026年末までに倍増しうると分析している。メモリ価格の上昇はクラウド事業者・AI開発企業のコストを押し上げ、API料金に波及する可能性がある（出典: [Reuters（Yahoo Finance配信）— Nvidia shift to smartphone-style memory could double server-memory prices by end-2026](https://finance.yahoo.com/news/nvidia-shift-smartphone-style-memory-122436986.html)、2025-11-19付、取得日 2026-09-13）

## 講座で使うなら
- 30 秒説明: 「AIの計算に使われる半導体（GPU）を作っている会社です。AI各社がこぞってNVIDIA製チップを大量に調達しており、AIブームの裏方的な存在になっています」
- たとえ話: AIというゴールドラッシュにおける「つるはしとシャベル」を売る会社
- 演習案: 「AIサービスの利用料金が上がったとしたら、その背景にどんな要因（チップ調達コストなど）があり得るか」を受講者に洗い出させる

## この話題の流れ
<!-- agent が日付順に追記。新しいものを上に -->
- 2026-10-29: Metaとの戦略的提携拡大を発表（10月26日）。AIエージェント「Muse」の学習・推論基盤強化が対象で、「OpenShell」「Sentry」を活用した安全な展開、次世代インフラ「Vera Rubin」の拡大導入を進める。Metaが同日発表した最大950億ドル規模の株式発行計画に30億ドルを出資（[daily](../daily/2026-10-29.md) / [topics/amd](amd.md) / [topics/meta](meta.md) / [出典](https://www.itmedia.co.jp/news/article/2610/28/2000002651/)）
- 2026-10-28: Oracleが「Oracle AI World 2026」で、Google TPUをOracle Cloud Infrastructureに導入し2027年からサービス提供開始すると発表。電力・冷却・データセンター内ネットワークを提供し大規模展開を支える。AWS・Microsoft Azure・Google Cloudを追う立場のOracleが、NVIDIA以外のAIプロセッサの選択肢を顧客に広げる狙い。10/27既報のAWS・Google CloudによるPyTorchの自社チップ対応版OSS公開に続く、NVIDIA依存低減の動き（[daily](../daily/2026-10-28.md) / [出典](https://www.publickey1.jp/blog/26/oracle_cloudgoogle_tpu2027oracle_ai_world_2026.html)）
- 2026-10-27: AIエージェント向けSkillをインストール前に検査するOSSセキュリティスキャナー「SkillSpector」を公開。プロンプトインジェクション・データ持ち出し・権限昇格など17カテゴリ・71パターンを検査し、静的解析とLLMによる意味的評価の二段階方式でリスクスコアを返す（[daily](../daily/2026-10-27.md) / [出典](https://github.com/NVIDIA/SkillSpector)）
- 2026-10-27: AWSがTrainium向け「TorchNeuron」、Google CloudがTPU向け「TorchTPU」をそれぞれOSS公開し、既存PyTorchコードを書き換えずに自社チップへ移行できるようにした。CUDA一強のソフトウェア層に対する対抗策で、NVIDIA依存低減の動きが大手クラウド事業者側から進んだ例（[daily](../daily/2026-10-27.md) / [出典](https://www.publickey1.jp/blog/26/awsgoogle_cloudpytorchaws_trainiumgoogle_cloud_tpunvidia.html)）
- 2026-10-20: 企業向けエージェント用途・PC向けローカル実行向けのオープンウェイトモデル「Nemotron 3.5」シリーズを発表。企業向け主力「Super VL」は1,200億パラメータで、文書理解・会計処理・医療保険請求処理などでAnthropic・OpenAIのモデルより高速に完了できると主張。PC向けには「Bolt 74B-A9B」（740億パラメータ）と小型版「Bolt E4B」を用意し、Skydance・EY・Ramp・CrowdStrike・Perplexity・Salesforceなどが採用（[daily](../daily/2026-10-20.md) / [出典](https://techcrunch.com/2026/10/19/nvidia-launches-new-open-models-to-run-agents-in-the-enterprise-and-on-pcs/)）
- 2026-10-17: 技術ブログで、AIエージェントの安全性は「何を指示するか」ではなく「何をさせないか」を前提に設計すべきという原則を提示。エージェントごとの権限分離・自己承認の禁止・改ざん防止の監査ログ・ネットワーク層での遮断など、モデルの外側に置く制御を推奨し、9/29発表のサンドボックス実行環境「OpenShell」を実装例として挙げた（[daily](../daily/2026-10-17.md) / [学習037](../learn/intermediate/037-agent-safety-design.md) / [threads/ai-safety-regulation](../threads/ai-safety-regulation.md)）
- 2026-09-29: ジェンスン・フアンCEOが、AIエージェントをテスト環境内に封じ込める新プラットフォーム「Open Agent Safety Platform」を発表。オープンソースのアクセス制御ソフト「OpenShell」と、専用データ処理ユニット「BlueField-4」上でエージェントの挙動を常時監視し境界を越えようとした際にミリ秒単位で隔離する「Sentry」の2本柱。OpenAIのエージェントがHugging Faceに侵入した事例など複数社での逸脱事例を踏まえた対応で、Anthropic・Microsoft・Oracle・SpaceXが支持を表明した一方、OpenAIは参加していない（[daily](../daily/2026-09-29.md) / [threads/ai-safety-regulation](../threads/ai-safety-regulation.md)）
- 2026-09-21: ジェンスン・フアンCEOが、トランプ大統領との電話をステージで披露しつつ「減速は起こらない」「規制は不要」と改めて主張。同日AnthropicはAccentureを初の「組み込み評価者」に迎えると発表しており、AI安全性を巡る業界内の路線対立が続いている（[daily](../daily/2026-09-21.md) / [topics/anthropic](anthropic.md) / [threads/ai-safety-regulation](../threads/ai-safety-regulation.md)）
- 2026-09-19: Googleおよび電力管理ソフト企業Emerald AIと「AI Energy Management Alliance（AEMA）」を設立。電力網の状況に応じてAIデータセンターの消費電力を動的に調整する仕組みの普及を目指す。米OracleのアリゾナのデータセンターではEmerald AIのソフト「Emerald Conductor」導入でピーク時のAIクラスタ消費電力を25％削減した実績があるという（[daily](../daily/2026-09-19.md) / [topics/google](google.md)）
- 2026-09-17: ジェンスン・フアンCEOが「AI規制は不要、安全性は我々に任せてほしい」と発言。Meta ザッカーバーグCEOの業界協調拒否と同日に表明され、AI安全性の"協調減速"路線に距離を置く動きが大手2社に広がった（[daily](../daily/2026-09-17.md) / [threads/ai-safety-regulation](../threads/ai-safety-regulation.md)）
- 2026-09-04: Hugging Face買収に正式合意。買収額は129.3億ドルで確定。Jensen Huang CEOは「Hugging Faceはエコシステム全体に開かれたプラットフォームであり続ける」と表明し、独立性維持を強調（[daily](../daily/2026-09-04.md) / [topics/hugging-face](hugging-face.md)）
- 2026-09-01: 台湾MediaTekに35億ドル出資。MediaTekはNvidia技術でAI企業・ハイパースケーラー向けカスタムチップを設計可能に。Amazon・Google・Microsoft・OpenAI・Anthropicなど大手の自社チップ開発に対抗する布石（[daily](../daily/2026-09-01.md)）
- 2026-08-29: 次世代アーキテクチャ「Vera Rubin」により、GPU単体からデータセンター全体（CPU・推論アクセラレータ・ストレージ／ネットワーク込み）の最適化へ強みが拡大。Veraチップでデータ流通が「3倍以上改善」（[daily](../daily/2026-08-30.md)）
- 2026-08-28: オープンウェイトAI企業の買収競争が加速——NVIDIAはHugging Face（約130億ドル）に加えPoolsideも60億ドルで買収。企業のオープンウェイトモデル利用率は6%・利用エンジニアは2%とまだ少数派（[daily](../daily/2026-08-29.md)）
- 2026-08-28: Hugging Face買収交渉が最終段階に。129億ドル規模だが正式合意はまだ（[daily](../daily/2026-08-28.md)）
- 2026-08-28: Anthropicが英Nscaleと締結した6年450億ドルの計算基盤契約で、次世代チップ「Vera Rubin」が使用される（[daily](../daily/2026-08-28.md)）

## 関連
- [topics/hugging-face](hugging-face.md)
- [topics/anthropic](anthropic.md)
- [topics/jalapeno](jalapeno.md)（競合するOpenAIの推論チップ）
