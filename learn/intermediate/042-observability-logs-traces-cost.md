---
type: learn
track: intermediate
number: 042
title: "オブザーバビリティ：ログ・トレース・コスト可視化"
date: 2026-09-29
level: intermediate
audience: [engineer, business]
tags: [observability, agent, cost]
reading_minutes: 4
sources:
  - url: https://code.claude.com/docs/en/monitoring-usage
    title: "Claude Code — Monitoring usage"
    fetched: 2026-09-29
  - url: https://github.com/open-telemetry/semantic-conventions-genai
    title: "OpenTelemetry Semantic Conventions for Generative AI"
    fetched: 2026-09-29
related: [topics/claude-code.md]
---

# 042 オブザーバビリティ：ログ・トレース・コスト可視化

!!! abstract "この記事で説明できるようになること"
    - 「ログ」「トレース」「メトリクス」がそれぞれ何を見える化する仕組みか
    - AIエージェント運用で、この3つをどう使い分けるか
    - ログを取っていても異常に気づけない、というよくある落とし穴

## 仕組み

AIエージェントの運用を「見える化」する手段は、大きく3種類に分けられる。

- **ログ**：個々の出来事の記録。「いつ・誰が・どのプロンプトを送り、どのツールが呼ばれたか」を1件ずつ残す
- **トレース**：1回のリクエストが、ユーザーのプロンプト→API呼び出し→ツール実行→応答、とどう流れたかの経路。複数のツール呼び出しをまたいで「どこで時間がかかったか」を追える
- **メトリクス**：集計値。トークン数・コスト・レイテンシなどを時系列やモデル別に集計し、傾向を把握する

Claude Codeは、この3種類をOpenTelemetry（OTel）という業界標準規格でまとめて出力できる。`CLAUDE_CODE_ENABLE_TELEMETRY=1` で有効化し、メトリクスは `claude_code.token.usage`（トークン数）・`claude_code.cost.usage`（セッションごとのコスト）・`claude_code.lines_of_code.count`（変更行数）などを出力、ログは `claude_code.user_prompt`（プロンプト）・`tool_decision` / `tool_result`（ツール実行の可否と結果）などのイベントを出力する。トレース機能はベータ扱いで、`CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1` を追加すると、1回のリクエストがモデル呼び出し・トークン数・レイテンシ（最初の1トークンが返るまでの時間）・ツール実行時間まで一本の経路として追跡できる（出典: [Claude Code — Monitoring usage](https://code.claude.com/docs/en/monitoring-usage)、取得日 2026-09-29）。

これを個別ツールの独自仕様でなく標準規格で行う狙いは、監視基盤（Datadog・Grafana・社内ダッシュボードなど）を乗り換えずに複数のAIツールを横断して同じ形式で観測できるようにすること。OpenTelemetryのGenAI向け拡張は、LLM・エージェント・MCPクライアントなど生成AI特有のspan・メトリクス・イベントを標準化するプロジェクトとして、業界横断で開発が進んでいる（出典: [OpenTelemetry Semantic Conventions for Generative AI](https://github.com/open-telemetry/semantic-conventions-genai)、取得日 2026-09-29）。

## 比較・判断基準

| 種類 | 向いている用途 | 向いていない用途 |
|---|---|---|
| ログ | 「あの時何が起きたか」の事後調査、不正利用の監査 | 全体傾向の把握（1件ずつ見るには量が多すぎる） |
| トレース | 「なぜこのリクエストは遅い／高コストだったか」の原因特定 | 大量アクセスの常時監視（負荷が大きい） |
| メトリクス | コストの予算管理、異常な急増の検知、ダッシュボード表示 | 個別の異常な挙動の原因特定（集計値だけでは分からない） |

3つは排他ではなく、多くの場合「メトリクスで異常を見つけ、トレースで原因の見当をつけ、ログで詳細を確認する」という順で組み合わせて使う。

## 落とし穴

1. **プロンプト内容をそのままログに残し、機密情報が監視基盤に漏れる**：Claude Codeでは `OTEL_LOG_USER_PROMPTS` や `OTEL_LOG_TOOL_CONTENT` のようにプロンプト本文・ツール出力の記録は既定でオフになっており、必要な範囲だけ明示的に有効化する設計になっている。何でも記録すればよいわけではない。
2. **メトリクスだけ見て、コスト増の原因を追わない**：「先月よりコストが増えた」という数字は見えても、原因（モデル変更か、キャッシュが効いていないのか、特定チームの利用が増えたのか）はトレースやログを見ないと分からない。
3. **ベータ機能をそのまま本番の意思決定に使う**：トレース機能のようにベータ表記のものは仕様変更の可能性がある。本番のコスト管理はメトリクス、原因調査の補助としてトレースを使う、という役割分担が安全。

## 実務への接続

複数チームでAIエージェントを使い始めると、「誰がどれだけ使っているか」が見えないまま予算超過に気づく、というのはよくある失敗パターンだ。Claude Codeでは管理者が `managed settings` でOTLPの送信先を固定でき、開発者側が勝手に監視をオフにしたり送信先を変えたりできないようにする運用も可能。組織全体でAIツールを導入する際は、個々のプロンプトの巧拙よりも先に「利用状況とコストがどこで確認できるか」を決めておくと、後からの説明責任（なぜこの予算になったか）が格段に楽になる。

## 講座で使うなら

- 30 秒説明: 「AIをどれだけ使ったか・何が起きたかを、後から確認できる形で記録・集計する仕組みです。車のダッシュボードのように、走行記録（ログ）・1回の運転経路（トレース）・燃費計（メトリクス）に分けて考えます」
- たとえ話: 家計簿の「レシート（ログ）」「1回の買い物の道のり（トレース）」「月次の支出グラフ（メトリクス）」
- 演習案: 受講者が使っているAIツールについて、今月のトークン数・コストをどこで確認できるか（あるいはできないか）を書き出させ、確認できない場合はどんな仕組みがあれば確認できるかを考えさせる

## 出典・参考
- [Claude Code — Monitoring usage](https://code.claude.com/docs/en/monitoring-usage)（取得日 2026-09-29）
- [OpenTelemetry Semantic Conventions for Generative AI](https://github.com/open-telemetry/semantic-conventions-genai)（取得日 2026-09-29）

## 関連
- [topics/claude-code](../../topics/claude-code.md)
