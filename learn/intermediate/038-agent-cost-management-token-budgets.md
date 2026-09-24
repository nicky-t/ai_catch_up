---
type: learn
track: intermediate
number: 038
title: "エージェントのコスト管理とトークン予算"
date: 2026-09-25
level: intermediate
audience: [engineer, business]
tags: [agent, cost, claude-code]
reading_minutes: 4
sources:
  - url: https://code.claude.com/docs/en/costs
    title: "Manage costs effectively - Claude Code Docs"
    fetched: 2026-09-25
  - url: https://platform.claude.com/docs/en/build-with-claude/effort
    title: "Effort - Claude Platform Docs"
    fetched: 2026-09-25
related: [topics/claude-code.md, topics/anthropic.md]
---

# 038 エージェントのコスト管理とトークン予算

!!! abstract "この記事で説明できるようになること"
    - 「トークン予算」と「effort（努力度）」の違いを説明できる
    - コストが膨らむ典型パターンと、下げるための具体的な打ち手を挙げられる
    - チーム導入時のコスト見積もり方（レート制限のサイジング表）を使える

## 仕組み
エージェントのコストは「モデル料金 × トークン数」で決まるが、トークン数を左右する主なレバーは3つある。

1. **モデル選択**：Sonnet はコーディングの大半をこなしつつ Opus より安い。複雑な設計判断だけ Opus に切り替え、サブエージェントの単純作業は Haiku を指定する、という使い分けが基本
2. **拡張思考（extended thinking）**：既定でON。思考トークンは出力トークンとして課金され、モデルによっては1リクエストで数万トークン規模になる。`MAX_THINKING_TOKENS`環境変数で固定予算モデルの上限を下げられるが、適応的思考（adaptive reasoning）モデルはこの値を無視し、代わりに「effort」で制御する
3. **effort（努力度）パラメータ**：`low`/`medium`/`high`/`xhigh`/`max`の5段階。**重要なのは「厳密なトークン予算ではなく振る舞いの指示」**という点で、effortを下げても難しい問題では相応に考え続ける。下げると起きるのは「同じ問題への思考量が減る」「ツール呼び出しが減り前置きの説明が減る」こと。Claude Opus 5.5は既定が`medium`（他モデルは`high`）で、思考自体はOFFにできない

Claude Code側では、コンテキストサイズ（会話履歴の長さ）がコストに直結する。プロンプトキャッシュで会話履歴の再送コストは下がるが、キャッシュ有効期間（サブスクリプションは1時間、APIキー既定は5分）を超えて再開すると全文が再処理される。エンタープライズ実績では1人あたり平均約13ドル／稼働日、150〜250ドル／月で、90%のユーザーは30ドル／稼働日を下回るという。

## 比較・判断基準

| 状況 | 選ぶべき打ち手 |
|---|---|
| 単純なチャット・分類タスク | effort `low`、モデルはSonnet/Haiku |
| 通常のコーディング・エージェント作業 | effort既定（`high`。Opus 5.5は`medium`） |
| 30分超の長時間エージェントタスク | effort `xhigh`（対応モデルのみ）＋大きめの`max_tokens` |
| チーム導入前 | 小規模パイロットでベースライン計測→本展開 |
| API利用でチーム規模拡大 | 人数に応じてTPM/RPMを下げる（例：1〜5人なら1人200〜300k TPM、100〜500人なら1人15〜20k TPM） |

organizationの規模が大きくなるほど「全員が同時にエージェントを使う」割合が下がるため、1人あたりのレート制限は下げてよい、という考え方がAnthropicの公式サイジング表の根拠になっている。

## 落とし穴
1. **effortを下げれば必ず安く速くなるという誤解**：effortは振る舞いの信号であり、厳密な予算ではない。難しい問題では下げても相応に思考する
2. **セッション中にトップレベルのeffortを変えるとキャッシュが切れる**：一部モデルはメッセージ単位でeffortを変えられる「per-message effort」がキャッシュを保ったまま切り替えられるが、対応しないモデルでは次のリクエストからキャッシュが最初からになり、コストが跳ねる
3. **長時間セッションを放置してコンテキストが肥大化**：`/clear`せずに無関係な作業を続けたり、スケジュールタスクやクロスセッションメッセージが待機中のセッションを毎回フルコンテキストで起動させたりすると、活動していないのに課金が積み上がる

## 実務への接続
- 新規導入時は「まず小さなパイロットチームで実測→本展開」の順で、想定コストを見積もる
- コスト超過に気づいたら、まず「長時間セッションが`/clear`されていないか」「既定モデルがOpusのままか」を確認する（この2つが想定外コストの典型原因）
- MCPサーバーは使っていないものを`/mcp`で無効化し、CLIツール（`gh`・`aws`等）で代替できる場合は優先する（ツール一覧がコンテキストを消費するため）

## 講座で使うなら
- 30 秒説明: 「effortは車のアクセルの踏み込み具合。トークン予算はガソリンの残量。踏み込みを弱めても急な上り坂（難しい問題）ではやっぱりガソリンを使う」
- たとえ話: 効率重視のタクシー運転手（effort低）と丁寧な運転手（effort高）の違い。どちらも渋滞（難問）では時間もガソリンも余分にかかる
- 演習案: 受講者の所属チームの人数を仮定し、公式のTPM/RPMサイジング表から必要な合計トークン予算を計算させる（例：200人なら1人20k TPM×200人＝400万TPM）

## 出典・参考
- [Manage costs effectively - Claude Code Docs](https://code.claude.com/docs/en/costs)（取得日 2026-09-25）
- [Effort - Claude Platform Docs](https://platform.claude.com/docs/en/build-with-claude/effort)（取得日 2026-09-25）

## 関連
- [topics/claude-code](../../topics/claude-code.md)
- [topics/anthropic](../../topics/anthropic.md)
