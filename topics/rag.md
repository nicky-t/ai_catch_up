---
type: topic
title: "RAG（検索拡張生成）"
slug: rag
created: 2026-09-09
updated: 2026-09-10
tags: [rag]
level: beginner
audience: [engineer, business, instructor]
related: [learn/intermediate/021-rag-overview-pipeline-failure-points.md, learn/intermediate/022-chunking-strategies.md, learn/intermediate/023-hybrid-search-reranking.md]
---

# RAG（検索拡張生成）

## 一言で
LLMに質問する前に、社内文書やWebなど外部の情報源から関連する文章を検索して質問文に付け加える仕組み。モデルの学習データにない・古い・社外秘の情報にも答えられるようにするための、最も広く使われている手法の1つ。

## 仕組み
- 大きく4段階（インデックス化→検索→拡張→生成）で構成される。文書を検索しやすい単位に分割する「チャンキング」、分割した文章をベクトルに変換する「埋め込み」、質問に近い文章を探す「検索」、見つけた文章を質問に足して生成する「拡張」の順で動く（詳細: [learn/intermediate/021](../learn/intermediate/021-rag-overview-pipeline-failure-points.md)）
- チャンキングの粒度（サイズ・重なり幅）が検索精度を大きく左右する。細かすぎると文脈が失われ、粗すぎると余計な情報が混ざる（詳細: [learn/intermediate/022](../learn/intermediate/022-chunking-strategies.md)）
- 検索段階では、キーワード検索（BM25）とベクトル検索を組み合わせる「ハイブリッド検索」で取りこぼしを減らし、候補を絞ってから精査する「リランキング」で最終候補の精度を上げる2段階構成が標準的（詳細: [learn/intermediate/023](../learn/intermediate/023-hybrid-search-reranking.md)）
- 「検索の失敗」（そもそも関連文章を見つけられない）と「生成の失敗」（見つけた文章はあるが正しく使えない）は別問題であり、評価も分けて行う必要がある

## 実務での使い方
- 社内マニュアル・議事録・FAQなど「頻繁に更新されるが公開されていない情報」への回答に向く
- 長文コンテキスト（モデルに全文を読ませる方式）とどちらを選ぶかは、文書量・更新頻度・コストで判断する（要追記：判断基準の詳細）
- チャンクサイズ・オーバーラップは自社の文書・想定クエリで実際に試してから決める。業界のベンチマーク値をそのまま採用しない

## 講座で使うなら
- 30 秒説明: 「AIに質問する前に、関連する社内文書を検索して一緒に渡す仕組みです。カンニングペーパーを持たせて試験に臨ませるようなイメージです」
- たとえ話: 分厚い辞典を丸暗記させる代わりに、必要なページだけを開いて渡す司書のような役割
- 演習案: 自分の業務でRAGが使えそうな「頻繁に更新されるが公開されていない文書」を1つ挙げてもらう

## この話題の流れ
<!-- agent が日付順に追記。新しいものを上に -->
- 2026-09-10: 学習記事023「ハイブリッド検索とリランキング」を公開。BM25とベクトル検索をReciprocal Rank Fusionで統合する仕組みと、クロスエンコーダーによるリランキングを組み合わせた2段階アーキテクチャを整理（[daily](../daily/2026-09-10.md)）
- 2026-09-09: 学習記事022「チャンキング戦略」を公開。チャンクサイズ・オーバーラップの目安と、測定条件によって結論が変わる点を整理（[daily](../daily/2026-09-09.md)）
- 2026-09-08: 学習記事021「RAGの全体像」を公開。インデックス化→検索→拡張→生成の4段階と、失敗しやすいポイントを整理（[daily](../daily/2026-09-08.md)）

## 関連
- [learn/intermediate/021-rag-overview-pipeline-failure-points](../learn/intermediate/021-rag-overview-pipeline-failure-points.md)
- [learn/intermediate/022-chunking-strategies](../learn/intermediate/022-chunking-strategies.md)
- [learn/intermediate/023-hybrid-search-reranking](../learn/intermediate/023-hybrid-search-reranking.md)
