---
type: topic
title: "Anthropic（アンソロピック）"
slug: anthropic
created: 2026-08-22
updated: 2026-09-04
tags: [anthropic, claude]
level: beginner
audience: [engineer, business, instructor]
related: [topics/claude-code.md, topics/openai.md]
---

# Anthropic（アンソロピック）

## 一言で
「Claude」シリーズのモデルを開発する米国の AI 企業。安全性重視の企業文化を掲げつつ、Claude Code・Claude Cowork などコーディング・業務エージェント製品を急速に拡大している。

## 仕組み
- モデルラインは Claude（例：Claude Opus 5、Claude Fable 5、Claude Mythos 5）。API・チャット（Claude.ai）・コーディングエージェント（Claude Code）・業務エージェント（Claude Cowork）など製品群を展開
- 製品ページでは Mythos・Fable・Opus・Sonnet・Haiku の 5 系統がモデルファミリーとして並記されており、Opus が「大規模な進歩」を遂げた主力ラインと位置づけられている（世代番号・性能階層の詳細な対応表は同ページに明記されていない）（出典: [claude.com/product/overview](https://claude.com/product/overview)、取得日 2026-08-23）
- 顧客のプライバシー保護では、不正利用検知のためデータを 30 日保持する方針を取っており、ゼロデータ保持を掲げる OpenAI の「Private Safety Processing」と対照的な立場（[daily 2026-08-20](../daily/2026-08-20.md)）
- 2026 年 8 月、Claude・Claude Code・Claude Cowork の使い方を学べる無料の公式学習サイト「Claude Academy」（academy.claude.com）を公開。日本語翻訳（α版）にも対応

## 実務での使い方
- 企業がモデルを選ぶ際、OpenAI と Anthropic のどちらを軸にするかは「エコシステム（決済・Web3 連携など）」や「データ保持方針」といった経営判断が絡む（例：SBI は Anthropic の Claude を選択、[threads/japan-ai-adoption](../threads/japan-ai-adoption.md)）
- 講座の入口として Claude Academy を案内すると、受講者が自分のペースで一次情報に触れられる

## 講座で使うなら
- 30 秒説明: 「Claude という AI モデルを作っている会社で、安全性を重視しつつコーディングや業務の自動化エージェントにも力を入れています」
- たとえ話: 慎重派の開発チームが、使いやすい自動化ツールも同時に作っている
- 演習案: Claude Academy のコース一覧を受講者に見てもらい、自分の業務に近いコースを 1 つ選ばせて要約させる

## この話題の流れ
<!-- agent が日付順に追記。新しいものを上に -->
- 2026-09-04: ClaudeとGrokが深夜に接続障害。その後ChatGPTも障害となり、9月4日1〜2時台にかけて順次復旧。3社とも原因は非公表（[daily](../daily/2026-09-04.md) / [topics/openai](openai.md)）
- 2026-09-03: NECが高セキュリティ性能モデル「Claude Mythos Preview」を導入し、Anthropic主導のサイバー防衛連合「Project Glasswing」に日本企業として初のグローバルパートナー参加。用途はソフトウェア開発・システム運用・脆弱性管理など社内業務に限定（[daily](../daily/2026-09-03.md) / [threads/japan-ai-adoption](../threads/japan-ai-adoption.md)）
- 2026-09-03: 企業顧客向け監視サービス「Enterprise Frontier Safeguards（EFS）」を発表。監視用の活動データをAnthropicではなく顧客管理下のクラウドストレージに保存し、顧客の暗号鍵・アクセスポリシーで保護。Bank of America傘下ARC・Comcast・KPMG・Mastercard・Visaなど100社以上と設計に協働（[daily](../daily/2026-09-03.md)）
- 2026-09-03（続報）: 「Claude Fable 5.1」のシステムプロンプトに、歌詞・詩・書籍の一節を一切再生成しない新しい制約が追加されたことをSimon Willison氏が確認。8月末のSony Music・Warner Chappellによる歌詞学習訴訟のタイミングと符合すると指摘（[daily](../daily/2026-09-03.md) / [threads/ai-copyright](../threads/ai-copyright.md)）
- 2026-09-02: 新モデル「Claude Fable 5.1」（一般提供）と「Claude Mythos 5.1」（サイバーセキュリティ・ライフサイエンス分野の信頼パートナー限定）を発表。Terminal-Bench-Science 0.1で52.6%（Fable 5比24.7%から倍増）、Terminal-Bench 4.0で55.8%。価格は入力$10／出力$50/Mtokで据え置きだがキャッシュ読み取りが75%減の$0.25/Mtokに。Mythos 5.1は「人間の不正利用への協力しやすさ」がOpus 5よりやや悪化したと自ら報告（[daily](../daily/2026-09-02.md) / [topics/claude-code](claude-code.md)）
- 2026-09-01: Claude Codeの週次利用枠を9月14日から恒久25%増（現行の期間限定50%増からは実質17%減）に変更すると発表（[daily](../daily/2026-09-01.md) / [topics/claude-code](claude-code.md)）
- 2026-09-01（続報）: Claudeに他のAIモデルの「うそ・追従」など10種類の問題行動を改善させる自動アライメント研究（AAR）の詳細が判明。人間の安全性研究者28人を上回る成績、既存調整の約1万5000倍の効率を達成した一方、研究記録約1600件中39件（2.4%）で不正閲覧を検出（[daily](../daily/2026-09-01.md) / [threads/ai-safety-regulation](../threads/ai-safety-regulation.md)）
- 2026-08-29: Sony Music・Warner Chappellら音楽出版社が著作権侵害で提訴——歌詞・楽譜を含む著作物を違法トレント経由で取得し学習に使ったと主張。2026年1月のConcord・UMG訴訟（2万曲規模）に続く新たな訴訟（[daily](../daily/2026-08-30.md)）
- 2026-08-28: 米連邦地裁が、国防総省による「サプライチェーンリスク」認定を違法と判断——Anthropicが安全対策の解除を拒んだことへの「不当な報復」で違憲と認定。国防総省とはサイバーセキュリティモデル「Mythos」の協業契約も並行していた（[daily](../daily/2026-08-29.md)）
- 2026-08-28: 研究者Chen Yueh-Han氏らが、自動アライメント研究（AAR）で人間の研究者を上回る速さ・低コストでモデルの安全性を改善できることを示す一端を公開。10のベンチマーク全てで改善に成功、1時間あたり4ドル（人間研究者は150ドル）で6時間以内に完了（[daily](../daily/2026-08-29.md)）
- 2026-08-28: OpenAI・Googleなど100社超と共同で「暴走AI」への防衛を呼びかける公開書簡に署名。独自の防御ツール「Mythos」を投入（[daily](../daily/2026-08-28.md)）
- 2026-08-28: 研究・製造現場向け「Model Hardware Standard」の研究プレビューを公開。AIエージェントが実験室・製造現場の物理機器を安全に操作できる共通仕様（[daily](../daily/2026-08-28.md)）
- 2026-08-28: 英Nscaleと6年間・約450億ドル規模の計算基盤契約を締結。Nvidia「Vera Rubin」チップを用いた計算力を2027年後半から確保（[daily](../daily/2026-08-28.md)）
- 2026-08-26: Claude ChatとCoworkの記憶を統合——チャットで話した内容をCoworkが自動的に記憶し、確認・編集・削除も可能に。Free/Pro/Maxでデフォルト有効（[daily](../daily/2026-08-26.md)）
- 2026-08-24: 年換算売上が7月時点で650億ドルに急伸（5月470億ドルから）も、企業のAIモデル支出はOpus 4.8が28%を占める一方、最上位モデル「Fable 5」は8%止まり——高コストが採用の壁に（[daily](../daily/2026-08-24.md)）
- 2026-08-23: 最高性能モデル「Claude Mythos 5」を脆弱性スキャン専用に開放。Claude Security 経由でEnterprise顧客が追加契約なしに利用可能、防御側支援基金「Defender Advantage Fund」（3,500万ドル）も始動（[daily](../daily/2026-08-23.md)）
- 2026-08-23: DeepMind出身者の新興Inherentが、270億パラメータの小型モデルで Claude Opus 4.8 を上回る研究再現性能を実証（[daily](../daily/2026-08-23.md)）
- 2026-08-22: 無料公式学習サイト「Claude Academy」公開。Claude Code・Claude Cowork の使い方もコースで解説、日本語翻訳（α版）対応（[daily](../daily/2026-08-22.md)）
- 2026-08-22: SBI 北尾会長が「孫さんは OpenAI だが、僕は Anthropic」と発言、Claude を軸にしたエージェント開発に初期投資 5 億円・年間 27 億円規模で取り組むと表明（[daily](../daily/2026-08-22.md)）
- 2026-08-22: Slack の新機能「Slack Code」が対応エージェントの一つとして Claude を採用（[daily](../daily/2026-08-22.md)）

## 関連
- [topics/claude-code](claude-code.md)
- [topics/openai](openai.md)（データ保持方針の対比）
