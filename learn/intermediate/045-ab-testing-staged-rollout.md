---
type: learn
track: intermediate
number: 045
title: "A/Bテストと段階的ロールアウト"
date: 2026-10-02
level: intermediate
audience: [engineer, business]
tags: [evaluation, observability]
reading_minutes: 4
sources:
  - url: https://tianpan.co/blog/2026-04-09-llm-gradual-rollout-shadow-canary-ab-testing
    title: "Tian Pan — Releasing AI Features Without Breaking Production: Shadow Mode, Canary Deployments, and A/B Testing for LLMs"
    fetched: 2026-10-02
  - url: https://www.koji.so/docs/ai-staged-rollout-user-research
    title: "koji.so — Staged Rollout for AI Features: Shadow Mode, Canary, and Kill Switches"
    fetched: 2026-10-02
related: [topics/agent-harness.md, learn/intermediate/041-eval-dataset-construction.md, learn/intermediate/043-guardrails-input-output-filtering.md]
---

# 045 A/Bテストと段階的ロールアウト

!!! abstract "この記事で説明できるようになること"
    - LLM機能のリリースが従来のソフトウェアと何が違うかを説明できる
    - シャドーモード・カナリア・A/Bテストという3段階それぞれの目的と計測指標を区別できる
    - ロールバック基準を「数値が出る前」に決めておく理由を説明できる

## 仕組み

新しいプロンプトやモデルを本番に出すのは、UIのボタン1つを差し替えるのとは別物である。オフライン評価では良く見えた変更が、本番では一部のユーザーに対してだけ静かに品質を落とすことがある。原因は、同じ入力でも出力が毎回変わる非決定性、「品質」という指標が単体テストでは測れないこと、プロンプト・モデル・リトリーバルなど複数層が同時に変わりうることにある（出典: Tian Pan、2026-04-09取得）。

このリスクに対処するため、3段階に分けてリスクを小さく確認しながら広げていく方法が整理されている。

1. **シャドーモード**：本番トラフィックを現行モデルと候補モデルの両方に流すが、候補側の出力はユーザーに見せずログに残すだけ。自動評価で両者を比較する。推論コストがほぼ倍になるため、大きな変更の時だけに限定すべきとされる
2. **カナリア**：候補モデルへのトラフィックを1%→5%→20%→50%→100%のように段階的に増やし、各段階を24〜48時間以上監視する。ここで初めて「実際のユーザー」が機能を体験する
3. **A/Bテスト**：安全性を確認した後、実質的に優れているかを測る段階。50/50に分けてユーザーの選好やタスク完了度を比較してから完全昇格を判断する

（出典: Tian Pan、2026-04-09取得）

## 比較・判断基準

| 段階 | 主な目的 | 計測指標の例 |
|---|---|---|
| シャドーモード | 実データでも出力が崩れないか | トークン数・コスト差分、自動判定による品質、レイテンシ |
| カナリア | 実ユーザーの行動が変わらないか | p50/p95/p99レイテンシ、拒否率・エラー率、受け入れ・編集率、エスカレーション率 |
| A/Bテスト | 候補が本当に優れているか | 再生成リクエスト率、セッション中断率、明示的評価（星付けなど） |

（出典: Tian Pan、koji.so、いずれも2026取得）

カナリア段階では「ユーザー単位で一貫した割り当て」が必須とされる。リクエストごとにランダムで振り分けると、同じユーザーが毎回違うモデルに当たって体験が一貫しなくなるためである（出典: Tian Pan、2026-04-09取得）。

## 落とし穴

1. **シャドーモードだけで満足する**：出力の質は確認できても、ユーザーが実際にどう反応するか（編集するか・離脱するか）はシャドーモードでは測れない。カナリア段階で初めて分かる（出典: koji.so、2026-08-14取得）
2. **平均値だけを監視する**：レイテンシは平均ではなくp95・p99のような裾の値を見ないと、一部ユーザーだけに起きている劣化を見逃す（出典: Tian Pan、2026-04-09取得）
3. **ロールバック基準を数値が出てから決める**：koji.soは「もし{メトリクス}が{閾値}を{下回る/超える}なら{アクション}を取る」という形式を展開前に文書化しておくべきだと指摘する。数値が悪化し始めてから基準を話し合うと、都合よく説明したくなるインセンティブが働くため、事前登録だけが信頼できる判断基準になるという（出典: koji.so、2026-08-14取得）

## 実務への接続

業務システムにAI機能を組み込む際も考え方は同じである。(1) 社内の少人数（または一部部署）だけに先行提供するカナリア段階を設ける、(2) 「正答率が◯%を下回ったら前バージョンに戻す」のような基準を展開前に決めて関係者に共有する、(3) 平均の満足度だけでなく、個々のケースでの失敗（拒否率・エスカレーション率）も追う。学習記事041の評価データセット、043のガードレールと組み合わせると、カナリア段階で見るべき指標をより具体的に設計できる。

## 講座で使うなら

- 30秒説明: 「AI機能は、少数のユーザーで試す→徐々に割合を増やす→優劣をきちんと比較する、という3段階で慎重に広げていきます。『数値が悪くなったらどう戻すか』は展開前に決めておくのがコツです」
- たとえ話: 新しいレシピをいきなり全店舗で出すのではなく、1店舗で試食会→数店舗で試験販売→本当に美味しいか味比べ、という順で広げる飲食チェーン
- 演習案: 自社でAI機能を導入するとして、「最初に試す対象（何%・誰か）」「ロールバックする基準」を受講者自身に1つずつ具体的に書かせる

## 出典・参考
- [Tian Pan — Releasing AI Features Without Breaking Production: Shadow Mode, Canary Deployments, and A/B Testing for LLMs](https://tianpan.co/blog/2026-04-09-llm-gradual-rollout-shadow-canary-ab-testing)（取得日 2026-10-02）
- [koji.so — Staged Rollout for AI Features: Shadow Mode, Canary, and Kill Switches](https://www.koji.so/docs/ai-staged-rollout-user-research)（取得日 2026-10-02）

## 関連
- [topics/agent-harness](../../topics/agent-harness.md)
- [learn/intermediate/041](041-eval-dataset-construction.md)
- [learn/intermediate/043](043-guardrails-input-output-filtering.md)
