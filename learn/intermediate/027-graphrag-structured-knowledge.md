---
type: learn
track: intermediate
number: 027
title: "GraphRAGと構造化知識：文章の断片をつなげる検索手法"
date: 2026-09-14
level: intermediate
audience: [engineer, business]
tags: [rag]
reading_minutes: 4
sources:
  - url: https://github.com/microsoft/graphrag/blob/main/docs/index.md
    title: "microsoft/graphrag — Documentation index"
    fetched: 2026-09-14
  - url: https://www.microsoft.com/en-us/research/project/graphrag/
    title: "Project GraphRAG - Microsoft Research"
    fetched: 2026-09-14
related: [topics/rag.md]
---

# 027 GraphRAGと構造化知識：文章の断片をつなげる検索手法

!!! abstract "この記事で説明できるようになること"
    - 通常のチャンク単位ベクトル検索RAGが苦手な質問と、GraphRAGが得意な質問の違いを説明できる
    - GraphRAGの仕組み（インデックス作成・コミュニティ検出・検索モード）を概要レベルで説明できる
    - 導入前に確認すべきコスト・更新頻度の注意点を挙げられる

## 仕組み

学習記事021で扱った通り、通常のRAGは文書をチャンク（断片）に分けて埋め込みベクトル化し、質問と似た断片を検索して渡す。この方式は「特定の1文にある事実」を探すのは得意だが、「複数の文書にまたがる情報をつなげて答える」質問には弱い。

Microsoft Researchが開発したGraphRAGは、検索前に文章から知識グラフを作っておくことでこの弱点を補う。処理は2段階に分かれる。

1. **インデックス作成**：文書を分析単位（TextUnits）に分割 → LLMでエンティティ・関係・主要な主張を抽出 → Leidenアルゴリズムによる階層的クラスタリングで、関連の強いエンティティ群を「コミュニティ」として検出 → 各コミュニティの要約をボトムアップで生成する
2. **検索**：3つのモードを使い分ける
    - **Local Search**：特定のエンティティとその隣接概念に展開して回答（従来のRAGに近い）
    - **Global Search**：コミュニティ要約を横断的に使い、データセット全体にまたがる質問に答える
    - **DRIFT Search**：Local SearchにGlobal Searchのコミュニティ情報を組み合わせたハイブリッド方式

## 比較・判断基準

| 観点 | チャンク単位のベクトル検索RAG | GraphRAG |
|---|---|---|
| 得意な質問 | 局所的な事実抽出（「Aの担当者は誰か」） | 複数情報源を横断する合成（「このデータセット全体で繰り返し出るテーマは」） |
| インデックス構築コスト | 埋め込み計算のみで比較的低コスト | エンティティ抽出・コミュニティ要約に大量のLLM呼び出しが必要で高コスト |
| 更新の容易さ | 差分の追加だけで済むことが多い | グラフ構造・コミュニティの再計算が絡み、更新コストが高い |
| 向くデータ | 頻繁に更新される文書群 | 比較的静的な文書アーカイブ |

## 落とし穴

1. **「グラフにすれば何でも精度が上がる」という誤解**：局所的な事実抽出質問なら従来のチャンクRAGで十分。GraphRAGの強みは「マルチホップ推論」「データセット全体の要約」に限られる
2. **インデックス構築コストの見落とし**：エンティティ抽出・コミュニティ要約でLLM呼び出しが大量に発生するため、更新頻度の高い文書には不向き
3. **学習記事026と同じ罠**：「新しい技術＝常に優れている」ではなく、質問の性質（局所的か横断的か）で使い分けるべき判断問題であることに変わりはない

## 実務への接続

社内ナレッジベースで「この案件の担当者は誰か」のような単発質問はチャンクRAGで十分だが、「今四半期のプロジェクト全体でどんなリスクが繰り返し指摘されているか」のような横断質問にはGraphRAGが向く。更新頻度が高い文書群には構築コストが見合いにくいため、議事録集・調査報告書群のような比較的静的なアーカイブから試すのが現実的。

## 講座で使うなら

- 30 秒説明: 「文章をバラバラの断片のまま検索する普通のRAGに対し、GraphRAGは文章から人物・組織・出来事のつながり（知識グラフ）を先に作っておいて、それを地図のように使って複数の情報をつなげて答える仕組みです」
- たとえ話: 索引だけで1ページずつ探す辞書引き（通常のRAG） vs 事前に相関図を作ってから謎を解く探偵（GraphRAG）
- 演習案: 受講者に、社内文書の中から「1件の文書だけでは答えられないが、複数の文書をつなげれば答えられる質問」を1つ考えてもらう

## 出典・参考
- [microsoft/graphrag — Documentation index](https://github.com/microsoft/graphrag/blob/main/docs/index.md)（取得日 2026-09-14）
- [Project GraphRAG - Microsoft Research](https://www.microsoft.com/en-us/research/project/graphrag/)（取得日 2026-09-14）

## 関連
- [topics/rag](../../topics/rag.md)
