---
type: learn
track: intermediate
number: 030
title: "Function calling / tool use の仕組みとツール定義の書き方"
date: 2026-09-17
level: intermediate
audience: [engineer, business]
tags: [tool-use, agent]
reading_minutes: 5
sources:
  - url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview
    title: "Tool use with Claude"
    fetched: 2026-09-17
related: [topics/mcp.md, topics/anthropic.md]
---

# 030 Function calling / tool use の仕組みとツール定義の書き方

!!! abstract "この記事で説明できるようになること"
    - モデルが「いつ」ツールを呼ぶかをどう判断しているか
    - ツールをJSON Schemaでどう定義するか
    - `tool_choice`での強制・並列呼び出し・strict tool useの使い分け

## 仕組み

Function calling（tool use）とは、モデルに「こういう関数（ツール）が使える」と教え、モデルが必要に応じてその関数を呼び出す形式で応答する仕組みのこと。モデル自身がコードを実行するわけではない点が重要で、実際の処理の流れは次の通り：

1. アプリ側が「ツール一覧」（名前・説明・入力スキーマ）をリクエストに含める
2. モデルはユーザーの依頼とツールの説明を照らし合わせ、ツールを呼ぶべきか判断する
3. 呼ぶ場合、モデルは自然文ではなく「このツールをこの引数で呼びたい」という構造化データ（`tool_use`ブロック）を返す
4. アプリ側（クライアントツールの場合）がその指示を実際に実行し、結果を`tool_result`としてモデルに送り返す
5. モデルはその結果を踏まえて最終的な回答を生成する

ツールには実行場所によって2種類ある。**クライアントツール**はアプリ側のコードが実行し結果を返す必要があるもの（自作の関数、bashやtext editorなど）。**サーバーツール**（Web検索・Web取得・コード実行など）はAnthropic側のインフラで実行され、開発者は結果を受け取るだけでよい。

## 比較・判断基準

ツール定義はJSON Schemaで書く。最小構成は「名前・説明・`input_schema`」の3点：

```json
{
  "name": "get_weather",
  "description": "Get the current weather for a given location.",
  "input_schema": {
    "type": "object",
    "properties": {
      "location": {"type": "string", "description": "City and state, e.g. San Francisco, CA"}
    },
    "required": ["location"]
  }
}
```

モデルがツールを呼ぶかどうかは`tool_choice`で制御できる：

| 設定 | 挙動 |
|---|---| 
| `auto`（既定） | 依頼内容とツールの説明が合致し、答えが会話中に無い場合にモデルが自律的に判断して呼ぶ |
| `any` / `tool` | 必ずいずれか（または指定した）ツールを呼ばせる。プロンプトで誘導するより確実 |
| `disable_parallel_tool_use` | 1ターンにつきツール呼び出しを1回に制限する |

複数のツールを同時に呼びたい場面（例：複数都市の天気を一度に取得）では並列ツール呼び出しが使える。また、`strict: true`をツール定義に加えると、モデルの出力が指定したスキーマに必ず一致するようになり、想定外のフィールド欠落・型違反を防げる（strict tool use）。

## 落とし穴

1. **必須パラメータの省略を勝手に補完される**：ユーザーが必要な情報（例：場所）を言わずに質問すると、モデル（特にSonnet系）が値を推測して埋めてしまうことがある。曖昧な依頼では確認を挟む設計にする
2. **ツールの説明が曖昧だと呼ばれない／余計に呼ばれる**：`auto`はツールの説明文とユーザー依頼の一致度で判断するため、説明が抽象的だと狙った場面で呼ばれなかったり、逆に不要な場面で呼ばれたりする
3. **トークンコストを見落とす**：ツール定義自体（名前・説明・スキーマ）や`tool_use`／`tool_result`ブロックも入力・出力トークンとして課金される。ツールを増やすほど、呼ばなくても定義分のコストがかかる

## 実務への接続

社内ツール（検索・DB照会・チケット発行など）をエージェントに使わせる場合、まず「クライアントツールとして自前で実行するか」「MCPサーバー経由で外部ツールとして接続するか」を選ぶことになる。ツール数が多い業務では、必要なツールを都度絞り込む仕組み（Tool Search的な考え方）がないと、コンテキストとコストの両方を圧迫する。

## 講座で使うなら

- 30秒説明: 「AIに関数の説明書を渡しておくと、必要な時にAI自身が『この関数をこの引数で呼びたい』と言ってくる。実際に関数を動かすのは人間側のプログラム」
- たとえ話: レストランで客（アプリ）がメニュー（ツール一覧）をシェフ（モデル）に見せておき、シェフが「この料理を作って」と厨房（実行環境）に指示を出す。実際に鍋を振るのは厨房で、シェフ自身は手を動かさない
- 演習案: 受講者に「天気を聞く」「予定を調べる」など身近なツールを1つ選んでもらい、そのJSON Schema（名前・説明・必須パラメータ）を紙に書き出してもらう

## 出典・参考
- [Tool use with Claude](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)（取得日 2026-09-17）

## 関連
- [topics/mcp](../../topics/mcp.md)
- [topics/anthropic](../../topics/anthropic.md)
