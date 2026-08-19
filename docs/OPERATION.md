# AI Catch-up 運用設計書

> 最終更新: 2026-08-19（仕様詰め 2回目まで反映）

## 目的

- AI による業務効率化支援・講師活動に向けて、毎日 AI の知識を積み上げる
- 情報は **資産として蓄積・検索可能** にする
- **人間が介入しなくても自動で増え続ける** 仕組みにする
- 「日々の最新情報」と「基礎・過去の情報」を同時並行で取得する

## 決定事項

| 項目 | 決定 |
|---|---|
| 自動実行 | Claude Code のクラウド定期実行（routine）。Mac が閉じていても動く |
| 資産の置き場 | GitHub リポジトリ `nicky-t/ai_catch_up`（**public**） |
| 閲覧（資産・検索） | GitHub Pages（MkDocs Material）— スマホでサイト内検索・ダークモード対応 |
| 閲覧（毎朝の習慣化） | Gmail で自分宛にダイジェスト配信（claude.ai で Gmail コネクタ接続が必要） |
| 実行時刻 | 毎朝 6:00 JST（= 21:00 UTC 前日） |
| 1日の分量 | 読了 10〜15分：ニュース 5〜10 件 × 3〜4 行 ＋ 学習記事 1 本 ＋ 講座ネタ 1 個 |
| 学習トラック初期設定 | 中級 1本/日 で開始。初心者・実践トラックはカリキュラムのみ用意（OFF） |
| 「講師目線」欄 | **重要・注目のニュースのみ**に付ける（参考には付けない） |
| フィードバックループ | あり（`feedback.md`） |
| 週次クイズ | あり（週まとめに確認クイズ 5 問） |
| モデル | Sonnet で開始、品質次第で Opus へ |
| 立ち上げ手順 | ローカル試走 → クラウド試走 → 初週は GitHub アプリで品質確認 → Pages・メール有効化 |

## 全体像（3層）

```
[① 自動収集・生成]  毎朝 6:00 JST にクラウド agent が起動
        │  config/ と feedback.md を読む → RSS・Web から新着収集 → 日本語で要約
        │  → Markdown 生成（daily / topics / learn / threads）→ git push
        ▼
[② 資産]  GitHub リポジトリ（Markdown＋frontmatter）
        │  push をトリガーに GitHub Actions が MkDocs Material でサイトをビルド
        ▼
[③ 閲覧]  GitHub Pages（検索・俯瞰・関連記事） ＋ Gmail（毎朝のダイジェスト）
```

## ディレクトリ構成

| パス | 内容 | 更新 |
|---|---|---|
| `config/tracks.yaml` | 学習トラックの ON/OFF と 1日あたり本数。**ここを編集するだけで切替** | 随時（人間） |
| `config/taxonomy.yaml` | 統制タグ（カテゴリ: model / company / tool / technique / business / policy / research…）と既存タグ一覧 | 週次（agent 提案→採用） |
| `config/sources.yaml` | 情報源リスト（RSS を一次、Web 検索を補助） | 随時 |
| `daily/YYYY-MM-DD.md` | 日次ダイジェスト（今日の3行／ニュース／今日の学習／講座ネタ） | 毎日 |
| `topics/<slug>.md` | 恒久ページ。**3段構成**（一言で／仕組み／実務での使い方）＋「この話題の流れ」（日付順の関連ニュース）＋「講座で使うなら」 | 毎日追記 |
| `threads/<slug>.md` | ストーリーライン（例: エージェント競争、AI規制の動き）。複数週にまたがる文脈 | 随時追記 |
| `learn/beginner/`, `learn/intermediate/`, `learn/practice/`, `learn/instructor/` | 各トラックの `CURRICULUM.md`（進捗付き）と記事。トラックごとにテンプレートが異なる | 毎日（ON のトラックのみ） |
| `weekly/YYYY-Www.md` | 週まとめ＋講座ネタ Top3＋確認クイズ 5 問 | 週 1 |
| `timeline.md` | AI 史の年表 | 週次 |
| `feedback.md` | 人間からの 1 行フィードバック。agent が毎朝読んで反映し、反映済みは `feedback_log.md` へ移す | 随時（人間） |
| `index.md` | 全体目次（自動生成） | 毎日 |
| `docs/` | 運用設計・agent プロンプト（`PROMPT_daily.md`, `PROMPT_weekly.md`）・テンプレート・良例 | 随時 |

### frontmatter（全記事共通）

```yaml
date: 2026-08-19
type: daily | topic | thread | learn | weekly
tags: [agent, anthropic]        # taxonomy.yaml に存在するもののみ
level: beginner | intermediate | advanced   # learn / topic
audience: [engineer, business, instructor]
importance: high | medium | low  # ニュース単位
sources:
  - url: https://...
    title: ...
    fetched: 2026-08-19
related: [topics/memory.md, threads/agent-race.md]
```

## 学習トラック（汎用性）

- トラックは `config/tracks.yaml` で管理。例：
  ```yaml
  tracks:
    intermediate: { enabled: true,  per_day: 1 }
    beginner:     { enabled: false, per_day: 1 }
    practice:     { enabled: false, per_day: 1 }
    instructor:   { enabled: false, per_day: 1 }
  ```
- 各トラックの `CURRICULUM.md` に順番と進捗（todo/done）を持つ。agent は先頭の todo を消化する
- テンプレート：初心者＝たとえ話＋図解 ／ 中級＝仕組み＋比較＋落とし穴 ／ 実践＝手順＋コピペ可能なプロンプト＋チェックリスト ／ 講師＝教え方・演習設計・FAQ
- `topics/` は 3 段構成なので、同じページが初心者にも実務者にも使える

## グルーピング・関連付け

| 仕組み | 内容 |
|---|---|
| 統制タグ | agent は `taxonomy.yaml` のタグのみ使用。新タグは `_proposed_tags` に提案 → 週次で採用 |
| トピックページ＝ハブ | ニュース中の固有名詞・概念は必ず `topics/` へリンク。トピック側に「この話題の流れ」を自動追記 |
| ストーリーライン | `threads/` に複数週の文脈を蓄積。講座の「最近の流れ」に直結 |
| 関連記事の自動表示 | Pages ビルド時に共通タグ数で「関連記事」を生成＋ agent が `related:` を明示 |
| 週次整理 | 重複統合・タグ揺れ修正・頻出トピックの昇格・`index.md` 再生成 |
| 検索 | Pages のサイト内検索（日本語）＋ ローカル Claude Code での意味検索 |

## 表示形式

- **日次ダイジェスト**：「今日の3行」→ ニュースカード（重要度バッジ：重要／注目／参考、カテゴリチップ、3〜4行要約、講師目線ブロック［重要・注目のみ］、出典・関連リンク）→ 今日の学習カード → 今日の講座ネタ
- MkDocs Material の admonition・バッジ・タグ・カード・ダークモード・サイト内検索を使用
- **メール**：同構造の簡略 HTML メール。各項目から Pages へリンク。件名 `[AI Catch-up] YYYY-MM-DD ダイジェスト`

## 品質ルール（agent に課す）

1. **WebFetch で実際に取得した URL 以外を出典にしない**。取得できなければ「未検証」と明記
2. 情報源は `sources.yaml` の RSS を一次、Web 検索を補助
3. 既存 `daily/` と `daily/_seen_urls.txt` を参照して重複除外
4. 記事本文の転載はしない（要約のみ・引用は短く・出典リンク必須・画像は保存しない）
5. `topics/` の既存ページがあれば新規作成せず追記
6. タグは `taxonomy.yaml` から。全記事に frontmatter
7. 要約は日本語＋固有名詞は原語併記
8. `feedback.md` を毎朝読み、反映した項目は `feedback_log.md` へ移す

## 懸念と対策

| 懸念 | 対策 |
|---|---|
| 誤情報・幻覚 | 品質ルール 1・2。良例・悪例を `docs/examples/` に残し few-shot 化 |
| クラウド agent の Web アクセス | routine の許可ツールに WebFetch / WebSearch を明示。ローカル試走→クラウド試走で確認 |
| 実行失敗に気づけない | メール未着で気づく＋ GitHub Actions で「当日の daily が無ければ通知」。初週は run log を確認 |
| 資産の散らかり | 週次整理 routine ＋ 統制タグ ＋ topics / threads が索引 |
| コスト | 日次 1 回＋週次 1 回。初週に実測 |
| 品質のブレ | Sonnet で開始 → 必要なら Opus。プロンプトはリポジトリ管理で履歴を残す |

## 実装ステップ

- [ ] 1. GitHub に public リポジトリ `ai_catch_up` を作成し、初期構成（config / docs / テンプレート）を push
- [ ] 2. `config/taxonomy.yaml`・`config/sources.yaml`・4 トラックの `CURRICULUM.md`（中級のみ ON）を作成
- [ ] 3. `docs/PROMPT_daily.md` を作成し、**ローカルで 1 回試走**して品質確認・調整
- [ ] 4. クラウド routine（日次 21:00 UTC, Sonnet, WebFetch/WebSearch 許可）を作成し、クラウド試走。初週は GitHub アプリで確認
- [ ] 5. MkDocs Material ＋ GitHub Actions で Pages を有効化（関連記事・タグ・日本語検索）
- [ ] 6. claude.ai で Gmail コネクタを接続し、routine にメール配信を追加
- [ ] 7. `docs/PROMPT_weekly.md` と週次 routine（週まとめ・クイズ・年表・タグ整理・index 再生成）を追加
- [ ] 8. 失敗検知の GitHub Actions を追加
