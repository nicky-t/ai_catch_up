---
type: learn
track: intermediate
number: 044
title: "モデル更新への追従：バージョン固定と回帰テスト"
date: 2026-10-01
level: intermediate
audience: [engineer, business]
tags: [evaluation, api]
reading_minutes: 4
sources:
  - url: https://platform.claude.com/docs/en/about-claude/model-deprecations
    title: Anthropic — Model deprecations
    fetched: 2026-10-01
  - url: https://developers.openai.com/api/docs/deprecations.md
    title: OpenAI — Deprecations
    fetched: 2026-10-01
related: [topics/anthropic.md, topics/openai.md, learn/intermediate/020-eval-driven-prompt-improvement.md]
---

# 044 モデル更新への追従：バージョン固定と回帰テスト

!!! abstract "この記事で説明できるようになること"
    - モデルIDを「バージョン固定」する意味と、固定しないとどんなリスクがあるかを説明できる
    - 主要2社（Anthropic・OpenAI）のモデル廃止（deprecation）通知の仕組みと猶予期間を説明できる
    - バージョン更新のたびに何を確認すればよいか、最低限の運用手順を組み立てられる

## 仕組み

API経由でモデルを使う場合、呼び出し方には大きく2種類ある。

- **エイリアス指定**（例：`gpt-5`、`claude-sonnet-latest`）：常に「現時点の推奨版」を指す。プロバイダー側が中身を無断で差し替えるため、ある日突然、出力の癖やコストが変わりうる
- **スナップショット固定**（例：`gpt-5-2025-08-07`、`claude-sonnet-4-5-20250929`）：日付入りの具体的なモデルIDを指定する。中身は変わらないので、テスト済みの挙動が保証される

OpenAIは日付入りのスナップショットIDを本番用に推奨しており、エイリアスは「前回検証した時点と挙動が変わりうる」リスクを伴うと説明している（出典: OpenAI Deprecations、2026-10-01取得）。

ただしスナップショット固定にも終わりがある。両社とも「いつかは廃止（deprecate）し、最終的に廃止（retire）する」ライフサイクルを運用しており、Anthropicは Active → Legacy → Deprecated → Retired の4段階でモデル状態を管理する。Deprecated になると新規には案内されなくなり、指定された廃止日を過ぎると Retired となってAPIリクエストが失敗するようになる（出典: Anthropic Model deprecations、2026-10-01取得）。

通知の猶予期間は各社で異なる：

- **Anthropic**：一般公開済みモデルの廃止は、廃止日の**少なくとも60日前**までにメールと公式ドキュメントで通知（出典: 同上）
- **OpenAI**：一般提供（GA）モデルは**少なくとも6カ月前**、チャット派生版・Codex派生版・Deep Research版などの特化モデルは**少なくとも3カ月前**、プレビューモデルは「2週間程度」という短い通知になる場合もあると明記されている（出典: OpenAI Deprecations、2026-10-01取得）

## 比較・判断基準

| 運用方法 | メリット | デメリット | 向いている場面 |
|---|---|---|---|
| エイリアス指定 | 常に最新モデルを自動で使える。更新作業が不要 | いつ挙動が変わるか予測できない。回帰の検知が難しい | 個人利用・プロトタイプ・厳密な再現性が不要な用途 |
| スナップショット固定 | 挙動・コストが変わらない。テスト結果の再現性が保たれる | 廃止期限が来たら必ず移行作業が発生する。放置すると突然リクエストが失敗する | 本番システム・業務フロー・契約上SLAがある用途 |

本番システムでは基本的にスナップショット固定一択だが、「固定して終わり」ではなく、固定した上で**廃止スケジュールを追跡する仕組み**とセットにする必要がある。

## 落とし穴

1. **エイリアスのまま本番投入する**：楽だが、プロバイダー側の更新タイミングで前触れなく出力が変わる。障害の原因調査で「モデルが変わっていた」に気づくのがよくある失敗パターン
2. **固定はしたが廃止通知を見ていない**：スナップショット固定は「更新されない」ことの保証であって「ずっと使える」ことの保証ではない。Deprecated 通知を見逃すと、Retired 後にAPIが一斉に失敗する
3. **新モデルへの切り替えを「動くかどうか」だけで判断する**：エラーが出ないことと、業務要件を満たす品質であることは別。既存の評価データセット（学習記事041参照）で新モデルを走らせ、指標が劣化していないかを確認してから切り替える

## 実務への接続

最低限の運用として、(1) 本番で使うモデルは必ず日付入りスナップショットで固定する、(2) 各プロバイダーの廃止一覧ページ（Anthropicは`model-deprecations`、OpenAIは`deprecations`）を定期的に確認するか、廃止メール通知の届く担当者を明確にする、(3) 新モデルへの切り替え前に、自社の評価データセットで回帰テストを行う、という3点を仕組み化しておくと、ある日突然APIが止まる事態を避けられる。プレビュー版モデルは通知猶予が2週間程度と短くなりうるため、本番の中核フローには使わない判断も有効である。

## 講座で使うなら

- 30秒説明: 「AIモデルにも『賞味期限』があります。日付入りのバージョンを指定しておけば急に挙動は変わりませんが、いずれ提供終了になるので、終了予定を定期的に確認する必要があります」
- たとえ話: ソフトウェアの「LTS（長期サポート）バージョン」と同じで、固定すれば安定するが、サポート終了のお知らせは自分で追いかける必要がある
- 演習案: 自社で使っているAI APIの呼び出しコードを確認させ、モデル指定がエイリアスかスナップショットか、廃止通知を受け取る担当者が決まっているかをチェックリスト化させる

## 出典・参考
- [Anthropic — Model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations)（取得日 2026-10-01）
- [OpenAI — Deprecations](https://developers.openai.com/api/docs/deprecations.md)（取得日 2026-10-01）

## 関連
- [topics/anthropic](../../topics/anthropic.md)
- [topics/openai](../../topics/openai.md)
- [learn/intermediate/020](020-eval-driven-prompt-improvement.md)
