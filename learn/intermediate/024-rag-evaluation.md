---
type: learn
track: intermediate
number: 024
title: "RAGの評価：検索精度と回答品質を分けて測る"
date: 2026-09-11
level: intermediate
audience: [engineer, business]
tags: [rag, evaluation]
reading_minutes: 4
sources:
  - url: https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/
    title: "Ragas — Available Metrics"
    fetched: 2026-09-11
related: [learn/intermediate/021-rag-overview-pipeline-failure-points.md, learn/intermediate/023-hybrid-search-reranking.md, topics/rag.md]
---

# 024 RAGの評価：検索精度と回答品質を分けて測る

!!! abstract "この記事で説明できるようになること"
    - RAGの「なんとなくうまくいかない」を、検索（Retrieval）側と生成（Generation）側のどちらの問題かに切り分けて考える
    - Context Precision／Context Recall／Faithfulness／Answer Relevancyという4つの代表的な指標が、それぞれ何を測っているか
    - 業務で評価を回す際によくある落とし穴

## 仕組み

RAGパイプライン（学習記事021）は「検索→生成」の2段階からなる。評価が難しいのは、最終的な回答がおかしくても、原因が検索側（そもそも正しい文書を持ってこられていない）なのか、生成側（正しい文書は持ってきたのに読み間違えている・使っていない）なのかが、回答だけを見ても分からない点にある。そこで評価指標も検索側と生成側に分けて設計する。

RAG評価フレームワークのRagas（RAG Assessment）は、代表的な指標として以下を挙げている（出典: [Ragas公式ドキュメント](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/)、取得日 2026-09-11）。

| 指標 | 測る対象 | 何を評価するか |
|---|---|---|
| Context Precision | 検索側 | 取ってきた文書のうち、実際に関連する文書がどれだけ上位に来ているか |
| Context Recall | 検索側 | 正解に必要な情報を、取ってきた文書がどれだけ網羅できているか |
| Faithfulness | 生成側 | 生成した回答が、取ってきた文書の内容に忠実か（文書にない主張をしていないか） |
| Answer Relevancy | 生成側 | 生成した回答が、ユーザーの質問にちゃんと答えているか |

この4分割の意味は、「検索は合っているのに回答が間違っている」パターンと「検索自体が外れている」パターンを区別できることにある。Faithfulnessが低いのに Context Precision/Recall が高いなら、正しい文書を渡しているのにモデルが誤読・幻覚している「生成側の問題」。逆にContext Recallが低ければ、そもそも必要な情報を検索で取れていない「検索側の問題」で、生成をいくらチューニングしても改善しない。

## 比較・判断基準

| 症状 | 疑うべき指標 | 典型的な対策 |
|---|---|---|
| 回答が的外れ・関係ない話をする | Context Recall / Precision | チャンキング（学習記事022）・ハイブリッド検索（学習記事023）の見直し |
| 文書に無い数字や事実を答える（幻覚） | Faithfulness | プロンプトで「文書にない情報は答えない」と明示、根拠文書の引用を強制 |
| 文書は合っているが質問に答えていない | Answer Relevancy | 生成プロンプトの指示を明確化、出力フォーマットの見直し |

## 落とし穴

1. **回答の「もっともらしさ」だけで良し悪しを判断する**：流暢な文章は、検索が外れていても幻覚で埋め合わせてしまえるため、人間のレビューだけでは検索側の欠陥を見逃しやすい。指標を分けて測ることで初めて気づける
2. **評価用の質問セットが本番の質問分布とずれている**：開発者が作った「答えやすい質問」だけで評価すると、実際のユーザーが聞く言い換え・曖昧な聞き方でのRecall低下を見逃す
3. **一度評価して終わりにする**：チャンキング・検索手法・プロンプトのどれか1つを変えるたびに評価が変わりうるため、変更のたびに同じ評価セットで測り直す運用が必要

## 実務への接続

- 社内文書検索で「回答が微妙」というフィードバックが来たとき、まずContext Recall（検索側）を疑うか、Faithfulness（生成側）を疑うかで、対応するチームやコストが大きく変わる。原因を切り分けずに「プロンプトを直す」だけで済ませると、検索側の問題は残り続ける
- 評価は完璧でなくてよい。少数（数十件）でも「検索側」「生成側」を分けた評価セットを持っているだけで、改修の優先順位付けが格段にしやすくなる

## 講座で使うなら

- 30 秒説明: 「RAGの回答がイマイチなとき、『そもそも正しい情報を持ってこられているか』と『持ってきた情報を正しく使っているか』を別々に測るのがRAG評価です」
- たとえ話: 料理がまずいとき、「材料が悪い（検索側）」のか「調理の仕方が悪い（生成側）」のかを切り分けないと、正しい対策が打てないのと同じ
- 演習案: 受講者が使った社内チャットボット・AI検索の「イマイチだった回答」を1つ思い出してもらい、それが検索側の問題か生成側の問題かを議論させる

## 出典・参考
- [Ragas — Available Metrics](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/)（取得日 2026-09-11）

## 関連
- [learn/intermediate/021-rag-overview-pipeline-failure-points](021-rag-overview-pipeline-failure-points.md)
- [learn/intermediate/023-hybrid-search-reranking](023-hybrid-search-reranking.md)
- [topics/rag](../../topics/rag.md)
