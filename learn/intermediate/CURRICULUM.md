---
track: intermediate
level: intermediate
status_legend: "[ ] todo / [x] done（done の行末に記事パスを追記）"
---
# 中級カリキュラム（60 本）

前提：ChatGPT / Claude 等を日常的に使っており、プロンプト・トークン・RAG・エージェントという言葉は知っている。
ねらい：「仕組みを説明できる」「業務導入で判断できる」「各社を比較して語れる」状態にする。

## A. LLM の仕組みを説明できる（12）
- [x] 001 Transformer と自己注意：なぜ文脈が効くのかを図で説明する → learn/intermediate/001-transformer-self-attention.md
- [x] 002 トークナイザー：日本語が不利になる理由とコストへの影響 → learn/intermediate/002-tokenizer-japanese-cost.md
- [x] 003 事前学習・SFT・RLHF：3 段階で何が変わるか → learn/intermediate/003-pretraining-sft-rlhf.md
- [x] 004 推論時のパラメータ：temperature / top-p / max tokens を実務でどう決めるか → learn/intermediate/004-inference-parameters.md
- [x] 005 コンテキストウィンドウ：長文化の歴史と「長ければ良い」が成り立たない理由 → learn/intermediate/005-context-window.md
- [x] 006 幻覚（ハルシネーション）の発生メカニズムと分類 → learn/intermediate/006-hallucination-mechanism.md
- [x] 007 推論モデル（reasoning models）：思考過程を出すモデルは何が違うか → learn/intermediate/007-reasoning-models.md
- [x] 008 マルチモーダル：画像・音声・動画を扱う仕組みと実務の使いどころ → learn/intermediate/008-multimodal.md
- [x] 009 埋め込み（embeddings）とベクトル検索：意味の近さをどう測るか → learn/intermediate/009-embeddings-vector-search.md
- [x] 010 蒸留・量子化・小型モデル：ローカル LLM が現実的になった背景 → learn/intermediate/010-distillation-quantization-small-models.md
- [x] 011 スケーリング則と学習データ枯渇問題 → learn/intermediate/011-scaling-laws-data-exhaustion.md
- [x] 012 オープンウェイト vs クローズド：ライセンス・性能・運用の比較軸 → learn/intermediate/012-open-weight-vs-closed.md

## B. プロンプト設計を体系化する（8）
- [x] 013 プロンプトの構造化：役割・制約・手順・出力形式・例の 5 要素 → learn/intermediate/013-prompt-structure-5-elements.md
- [x] 014 Few-shot と例示の選び方：効く例と効かない例 → learn/intermediate/014-fewshot-example-selection.md
- [x] 015 Chain-of-Thought と「考えさせる」設計の現在地（推論モデル時代の再評価） → learn/intermediate/015-chain-of-thought-reasoning-design.md
- [x] 016 出力フォーマット制御：JSON / 構造化出力 / スキーマ指定 → learn/intermediate/016-output-format-control.md
- [ ] 017 システムプロンプトの設計と運用（バージョン管理・テスト）
- [ ] 018 プロンプトインジェクション：攻撃パターンと防御の基本
- [ ] 019 長文入力の扱い：要約・分割・位置バイアス（lost in the middle）
- [ ] 020 プロンプト改善のループ：評価セットを作って回す

## C. RAG と知識接続（8）
- [ ] 021 RAG の全体像：検索→生成のパイプラインと失敗ポイント
- [ ] 022 チャンキング戦略：サイズ・重なり・構造を意識した分割
- [ ] 023 ハイブリッド検索とリランキング
- [ ] 024 RAG の評価：検索精度と回答品質を分けて測る
- [ ] 025 社内文書検索の現実：権限・更新・PDF 表の地獄
- [ ] 026 長文コンテキスト vs RAG：どちらを選ぶかの判断基準
- [ ] 027 GraphRAG・構造化知識との組み合わせ
- [ ] 028 ナレッジベース運用：陳腐化・重複・責任者問題

## D. エージェントとツール利用（10）
- [ ] 029 エージェントとは何か：ループ・ツール・状態・停止条件
- [ ] 030 Function calling / tool use の仕組みとツール定義の書き方
- [ ] 031 MCP（Model Context Protocol）：何を標準化したのか
- [ ] 032 計画・実行・振り返り：エージェント設計パターン
- [ ] 033 マルチエージェント：分業させる価値と失敗のしかた
- [ ] 034 メモリ：短期・長期・外部記憶の設計
- [ ] 035 コーディングエージェント（Claude Code 等）：何が自動化され、何が人に残るか
- [ ] 036 ブラウザ操作・コンピュータ操作エージェントの現在地
- [ ] 037 エージェントの安全設計：権限・承認・サンドボックス・監査ログ
- [ ] 038 エージェントのコスト管理とトークン予算

## E. 評価・品質・運用（8）
- [ ] 039 LLM-as-a-judge：AI の出力を AI で評価する設計と落とし穴
- [ ] 040 ベンチマークの読み方：何を測っていて何を測っていないか
- [ ] 041 評価データセットの作り方：業務タスクをどう切り出すか
- [ ] 042 オブザーバビリティ：ログ・トレース・コスト可視化
- [ ] 043 ガードレール：入出力フィルタと業務ルールの実装
- [ ] 044 モデル更新への追従：バージョン固定と回帰テスト
- [ ] 045 A/B テストと段階的ロールアウト
- [ ] 046 SLA・レイテンシ・可用性：業務システムに組み込むときの要件

## F. 業務導入の実務（8）
- [ ] 047 ユースケース発掘：効く業務・効かない業務の見分け方
- [ ] 048 ROI の出し方：工数削減をどう測り、どう報告するか
- [ ] 049 セキュリティとデータ取り扱い：学習利用・保存・越境の論点
- [ ] 050 社内ガイドライン設計：禁止事項より「使い方」を示す
- [ ] 051 PoC から本番へ：失敗パターンと乗り越え方
- [ ] 052 チェンジマネジメント：現場に定着させる方法
- [ ] 053 ベンダー・ツール選定：自社開発 / SaaS / プラットフォームの比較軸
- [ ] 054 料金体系の理解：トークン課金・席課金・従量とコスト試算

## G. 各社・エコシステムを比較して語る（6）
- [ ] 055 OpenAI / Anthropic / Google の思想と製品ラインの違い
- [ ] 056 Microsoft・Amazon・Apple：プラットフォーム企業の AI 戦略
- [ ] 057 オープンウェイト陣営（Meta / Mistral / 中国勢）と日本語モデル
- [ ] 058 国内動向：政府方針・日本企業の導入状況・国産モデル
- [ ] 059 規制と著作権：EU AI Act・日本のガイドライン・実務への影響
- [ ] 060 AI と雇用・スキル：業務効率化の先にある役割の変化
