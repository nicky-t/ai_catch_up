---
type: topic
title: "NVIDIA（エヌビディア）"
slug: nvidia
created: 2026-08-28
updated: 2026-11-27
tags: [nvidia, agent, safety]
level: beginner
audience: [engineer, business, instructor]
related: [topics/hugging-face.md, topics/anthropic.md, topics/jalapeno.md, threads/nvidia-leadership-crisis.md]
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
- 2026-11-26: 製造パートナーのDell・Super Microに、マレーシア・シンガポール・タイ・インドネシア向けサーバー出荷の一時停止を通知（WSJ報道）。背景は、これらの国のデータセンターを中国企業が遠隔利用してNVIDIA製チップにアクセスする「抜け穴」を米商務省が11月初めに規制強化で塞いだこと。シンクタンクInstitute for Progressは、こうした遠隔利用データセンターが中国のAI計算能力の約24%を担うと推定（[daily](../daily/2026-11-27.md) / [出典](https://techcrunch.com/2026/11/26/nvidia-hits-pause-on-chip-shipments-to-southeast-asia/)）
- 2026-11-25: S&P Global Ratingsが、ジェンスン・フアンCEOの解任・復帰をめぐる企業統治懸念（経営陣の監督の弱さ・key man risk）を理由に、格付け（現在AA）をAA-へ引き下げる可能性を検討と発表。審査は90日以内に終える見込みで投資適格は維持される見通しだが、NVIDIAが保証する新興AIクラウド事業者の債務コストにも波及しうる（[daily](../daily/2026-11-27.md) / [threads/nvidia-leadership-crisis](../threads/nvidia-leadership-crisis.md) / [出典](https://techcrunch.com/2026/11/25/sp-considers-nvidia-credit-downgrade-over-governance-and-key-man-risks/)）
- 2026-11-26: 復帰後初の全社集会で「自分は行動規範に違反した。誰も例外ではない」と発言。違反の具体的内容は不明。専門家は、行動規範違反の放置は企業文化への影響（士気・信頼の低下）が大きく、CEOと会社が一体化している企業ほど対応が難しいと指摘（[daily](../daily/2026-11-26.md) / [threads/nvidia-leadership-crisis](../threads/nvidia-leadership-crisis.md) / [出典](https://techcrunch.com/2026/11/25/jensen-huang-broke-nvidias-code-of-conduct-and-his-employees-may-not-forget-it/)）
- 2026-11-23: 取締役会が一転し、11月12日に辞任したジェンスン・フアン氏をCEOに復帰させると発表。トランプ大統領が取締役会に電話をかけ復帰を後押ししたと報じられ、大統領自身も「不正の証拠はない」と復帰を支持する一方、対中輸出規制を巡る調査は継続するよう要求。フアン氏は来週上院で証言する予定で、復帰後は本社で社員に迎えられた（[daily](../daily/2026-11-24.md) / [threads/nvidia-leadership-crisis](../threads/nvidia-leadership-crisis.md) / [出典](https://techcrunch.com/2026/11/23/nvidia-reverses-course-and-brings-jensen-huang-back-as-ceo/)）
- 2026-11-21: 決算説明会で、米政権の対中規制強化に合わせ中国向けH200チップの販売を停止すると発表（暫定CEOコレット・クレス氏）。好調な受注パイプラインを示したが株価は下落。取締役会は改めてフアン前CEOの復帰計画がないと明言したが、これは「1週間半前には全面的信頼を表明していた」立場からの転換とされ、復帰要求署名運動も続いている（[daily](../daily/2026-11-22.md) / [threads/nvidia-leadership-crisis](../threads/nvidia-leadership-crisis.md) / [出典](https://techcrunch.com/2026/11/21/a-tale-of-two-nvidias/)）
- 2026-11-19: TechCrunchが経緯全体を時系列でまとめた記事を公開。確定事実として、フアン氏が11月8日の社内メッセージで不貞を認め辞任したこと、取締役会が独立調査を開始したこと、17日に取締役会長が復帰を検討していないと明言したこと、同日Microsoft CEOサティア・ナデラ氏が暫定CEOコレット・クレス氏への信頼を表明したことなどを確認。一方「交際相手が中国のスパイだった」「3人目の交際相手がいた」といった主張は匿名情報源による報道にとどまり公式には未確認（[daily](../daily/2026-11-20.md) / [threads/nvidia-leadership-crisis](../threads/nvidia-leadership-crisis.md) / [出典](https://techcrunch.com/2026/11/19/nvidia-ceo-jensen-huangs-affair-with-alleged-chinese-spy-a-timeline/)）
- 2026-11-17: 取締役会長Harvey C. Jones氏が決算説明会で、辞任したフアン氏からの復帰の申し出を受けつつ「取締役会は全会一致で辞任を受理し、CEOへの復帰は想定していない」と明言。同日SECが開示内容を巡る民事調査を開始したとWSJが報道。フアン氏退任以降、株価は10%超下落した一方、第3四半期売上高は1,158億ドル（前年同期比103%増）と過去最高を記録（[daily](../daily/2026-11-19.md) / [threads/nvidia-leadership-crisis](../threads/nvidia-leadership-crisis.md) / [出典1](https://techcrunch.com/2026/11/17/nvidia-says-it-doesnt-plan-to-reappoint-jensen-huang-as-ceo/) / [出典2](https://techcrunch.com/2026/11/17/sec-reportedly-investigating-nvidia-amid-huang-exit/)）
- 2026-11-16: 米商務省が、D:5グループ22カ国（中国・ロシア・イラン・北朝鮮等）の企業が海外データセンターを遠隔利用して輸出規制を回避することを防ぐ暫定規則を導入。1,200万TPP超（H100/H200約750基相当）のデータセンターへのAIチップ輸出・再輸出・移転にライセンスが必要になり、仲介業者経由の間接アクセスも対象。既存事業者は90日以内にライセンス取得が必要（[daily](../daily/2026-11-17.md) / [出典](https://techcrunch.com/2026/11/16/us-tightens-ai-chip-export-controls-to-deter-chinese-companies-from-accessing-compute-remotely/)）
- 2026-11-14（2件）: フアン前CEOの復帰を求める署名活動が土曜時点で11万5千人超（現従業員5,965人・元従業員1,108人・株主63,063人含む、イーロン・マスク氏ら著名経営者も賛同）。一方でセキュリティ関連の人事を巡り「セキュリティ部門はフアン氏の交際関係や調査をどこまで把握していたか」が問われている。最高セキュリティ責任者David Reber氏は8月に退任（本人は若年性パーキンソン病と説明）、その約2.5カ月後にフアンCEOが退任した（[daily](../daily/2026-11-16.md) / [threads/nvidia-leadership-crisis](../threads/nvidia-leadership-crisis.md) / [出典1](https://techcrunch.com/2026/11/14/elon-musk-other-tech-execs-sign-petition-calling-on-nvidia-to-reinstate-jensen-huang/) / [出典2](https://techcrunch.com/2026/11/14/where-was-nvidias-security-team/)）
- 2026-11-14: フアンCEO退任を受け、アジア各国政府が反応。中国外務省は「スパイ」報道を否定し輸出規制への反対を改めて表明（Reuters推定で中国のAI計算案件約30億ドル超が規制対象チップに依存）。韓国はGPU26万個の供給継続を確認、台湾は海外本部計画への影響は限定的と説明、日本の経産省は「影響を注視する」とコメント（[daily](../daily/2026-11-15.md) / [出典](https://techcrunch.com/2026/11/14/asian-governments-react-to-nvidia-ceo-jensen-huangs-exit/)）
- 2026-11-13: フアンCEO退任を受け、VC・AIスタートアップへの資金供給縮小の懸念が拡大。NVIDIAは今年105件の資金調達ラウンドに参加（PitchBook調べ、Reflection AIへ8億ドル等）しており、主要な投資判断はフアン氏自身が下していたと投資家が証言。暫定CEOのコレット・クレス氏は「より慎重」との見方から、出資先の選別強化・小口化が懸念されている（[daily](../daily/2026-11-15.md) / [出典](https://techcrunch.com/2026/11/13/jensen-huangs-departure-blasts-big-hole-in-ai-startup-funding-vcs-and-founders-say/)）
- 2026-11-12: 取締役会が、ジェンスン・フアンCEOの社長・CEO・取締役からの即時辞任を発表。中国のスパイとされる人物と社内の部下の双方と関係を持っていたとの報道を受けたもので、同社に後継者計画はなかった。CFOのコレット・クレス氏（2013年9月入社、前職Microsoft 13年・Cisco 3年）が暫定CEOに就任。フアン氏が主導してきたオープンウェイトモデル擁護・業界自主規制（Open Agent Safety Platform）・「AIは道具」論の最大の発信者が消えることで、AI業界の方向性に広範な影響が及ぶ可能性がある（[daily](../daily/2026-11-13.md) / [出典](https://techcrunch.com/2026/11/12/jensen-huang-is-out-at-nvidia-who-is-colette-kress-his-interim-replacement/)）
- 2026-11-11: 米下院が、ジェンスン・フアンCEOとシンガポール企業Megaspeedの元幹部アリス・フアン氏との関係を巡り、同CEOへの召喚状発行を準備中とBloombergが報道。下院共和党のMast・Moolenaar・Crawford議員が非公開の合同説明会出席を求める書簡を送付済みで、応じるか否かの回答期限は11月11日中。応じなければ下院外交委員会が召喚状を発行する可能性が高いという（[daily](../daily/2026-11-12.md) / [出典](https://techcrunch.com/2026/11/11/congress-to-call-jensen-huang-in-to-answer-for-alleged-chinese-spy-affair/)）
- 2026-11-10: ジェンスン・フアンCEOが、11日開催予定のElevenLabsサミットへの登壇を取りやめた（ElevenLabsが発表）。Anthropic CEOフォーラムを含む他の登壇予定も取りやめている。関連報道ではYale大学の専門家が、フアン氏が今後もCEOにとどまれるかを「50-50」と見積もっていると伝えた（[daily](../daily/2026-11-10.md) / [出典](https://techcrunch.com/2026/11/09/jensen-huang-pulls-out-of-elevenlabs-summit-amid-nvidia-controversy/)）
- 2026-11-09: 取締役会が、CEOジェンスン・フアン氏とシンガポールの半導体企業Megaspeedの元幹部アリス・フアン氏との不適切な関係を巡り独立調査を開始すると発表。米情報機関の覚書は同氏が中国国家安全部からフアンCEOを探るよう勧誘されたと主張。フアンCEOは社内メッセージで不倫関係を認め謝罪し、取締役会は機密漏えいの可能性を「no reason to believe」としつつ同氏への信頼を示した（[daily](../daily/2026-11-09.md) / [出典](https://techcrunch.com/2026/11/08/nvidia-says-its-investigating-ceo-jensen-huangs-relationship-with-possible-chinese-spy/)）
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
