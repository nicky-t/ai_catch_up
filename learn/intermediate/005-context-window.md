---
type: learn
track: intermediate
number: 005
title: "コンテキストウィンドウ：長文化の歴史と「長ければ良い」が成り立たない理由"
date: 2026-08-23
level: intermediate
audience: [engineer, business]
tags: [context-window]
reading_minutes: 4
sources:
  - url: https://platform.claude.com/docs/en/build-with-claude/context-windows
    title: "Context windows - Claude Docs"
    fetched: 2026-08-23
  - url: https://developers.openai.com/api/docs/models
    title: "Models - OpenAI Developers"
    fetched: 2026-08-23
related: [topics/anthropic.md, topics/openai.md]
---

# 005 コンテキストウィンドウ：長文化の歴史と「長ければ良い」が成り立たない理由

!!! abstract "この記事で説明できるようになること"
    - コンテキストウィンドウとは何で、何がその中にカウントされるかを説明できる
    - 主要モデルのコンテキストウィンドウの規模と、なぜ大きくなってきたかを説明できる
    - 「長ければ良い」が成り立たない理由（精度低下）を踏まえて、RAG との使い分けを判断できる

## 仕組み
コンテキストウィンドウとは、モデルが1回の応答生成で参照できるテキストの上限のことで、モデルの「学習データ」とは別物である。Anthropic の定義では、システムプロンプト・会話履歴・ツール定義・画像や文書、そして生成される思考過程（thinking）や出力まで、リクエストに含まれるものはすべてこのウィンドウにカウントされる。

規模の目安として、Claude Opus 5・Claude Sonnet 5・Claude Mythos 5 などの現行モデルは API 上で100万トークンのコンテキストウィンドウを持ち（Claude Sonnet 4.5 など一部モデルは20万トークン）、OpenAI の GPT-5.6 シリーズ（Sol・Terra・Luna）も105万トークンに達している。数年前まで数千〜数万トークンが主流だったことを踏まえると、モデルが一度に扱える文章量は大きく伸びている。

## 比較・判断基準
| モデル | コンテキストウィンドウ | 最大出力 |
|---|---|---|
| Claude Opus 5 / Sonnet 5 / Mythos 5 など | 100万トークン | 12.8万トークン |
| Claude Sonnet 4.5 など一部モデル | 20万トークン | （要追記） |
| GPT-5.6（Sol / Terra / Luna） | 105万トークン | 12.8万トークン |

（出典: Anthropic・OpenAI 公式ドキュメント。数字は2026年8月時点）

大きいほど良いわけではなく、判断基準は「その業務が本当に長い文脈をまるごと必要とするか」。1回限りの長文要約なら長コンテキストが有利だが、繰り返し検索して使う知識ベースなら、後述の理由から RAG（検索拡張生成）の方が精度・コストの両面で有利なことが多い。

## 落とし穴
1. **コンテキスト・ロット（context rot）**：Anthropic が公式に使う用語で、トークン数が増えるほど精度・想起力が低下する現象。「入るから」といって不要な情報まで詰め込むと、かえって回答の質が落ちる。
2. **位置バイアス**：長い文脈の中盤に置かれた情報は、冒頭・末尾に比べて参照されにくい傾向があるとされる（"Lost in the Middle" として知られる現象）。重要な指示や事実は冒頭・末尾に置く工夫が要る。
3. **コストとレイテンシ**：長いコンテキストは処理コスト・応答時間にそのまま跳ね返る。プロンプトキャッシングを使っても、キャッシュされたトークンはウィンドウを占有し続ける。

## 実務への接続
「資料を全部貼れば読んでくれる」という発想は、精度・コストの両面で万能ではない。繰り返し参照する社内文書は RAG でその都度必要な部分だけ渡し、1回きりの長文レビューや要約には長コンテキストをそのまま使う、という使い分けが実務的。エージェントを長時間動かす場合は、Anthropic の compaction（自動要約）のような「古い履歴を圧縮する」機能の有無も選定基準になる。

## 講座で使うなら
- 30秒説明: 「AI が一度に読める文章の量の上限のこと。最近は100万トークン級まで伸びたが、量が増えても質が伸びるとは限らない」
- たとえ話: 広い会議室（長コンテキスト）を用意しても、資料を机の端から端まで積み上げれば、必要な1枚を探すのに時間がかかるのと同じ
- 演習案: 受講者に自分の業務資料を思い浮かべてもらい、「毎回全部読ませる」べきか「必要な部分だけ検索して渡す」べきかを判定させる

## 出典・参考
- [Context windows - Claude Docs](https://platform.claude.com/docs/en/build-with-claude/context-windows)（取得日 2026-08-23）
- [Models - OpenAI Developers](https://developers.openai.com/api/docs/models)（取得日 2026-08-23）

## 関連
- [topics/anthropic](../../topics/anthropic.md)
- [topics/openai](../../topics/openai.md)
