---
type: learn
track: intermediate
number: 048
title: "ROIの出し方：工数削減をどう測り、どう報告するか"
date: 2026-10-05
level: intermediate
audience: [engineer, business]
tags: [productivity, survey, evaluation]
reading_minutes: 4
sources:
  - url: https://newsroom.ibm.com/2025-10-28-Two-thirds-of-surveyed-enterprises-in-EMEA-report-significant-productivity-gains-from-AI,-finds-new-IBM-study
    title: "Two-thirds of surveyed enterprises in EMEA report significant productivity gains from AI, finds new IBM study"
    fetched: 2026-10-05
  - url: https://techcrunch.com/2026/10/04/google-froze-its-open-source-bug-bounty-program-due-to-a-significant-rise-in-ai-submissions/
    title: "Google froze its open source bug bounty program due to a 'significant rise' in AI submissions"
    fetched: 2026-10-05
related: [learn/intermediate/045-ab-testing-staged-rollout.md, learn/intermediate/047-use-case-discovery.md]
---

# 048 ROIの出し方：工数削減をどう測り、どう報告するか

!!! abstract "この記事で説明できるようになること"
    - ROIを測るときに必要な4つの要素（指標・ベースライン・コスト・比較対象）を説明できる
    - 「効果を感じる」と「ROIを達成した」が別の質問である理由を、実際の調査数字をもとに説明できる

## 仕組み

ROI（投資対効果）を「測れる形」にするには、次の4つを事前に決めておく必要がある。

1. **指標（メトリック）**：既存の業務KPI（処理件数・エラー率・対応時間・受注率など）から1つ選ぶ。「満足度が上がった気がする」のような新規の曖昧な指標は作らない
2. **ベースライン**：AI導入前、同じ指標を4〜8週間程度測っておく。「導入後に測り始める」とベースラインが無く比較できない
3. **コスト**：AIの利用料金だけでなく、導入・運用・レビューにかかる人件費も含めた「フルコスト」で見る
4. **比較対象（ホールドアウト）**：全員に一斉導入すると「AIのおかげで良くなった」のか「たまたま良くなった」のかを区別できない。チーム・期間・業務の一部を導入前のまま残し、比較する

学習記事045（A/Bテストと段階的ロールアウト）のロールアウト設計は、この4要素を仕組みとして運用する方法そのものでもある。

## 比較・判断基準

「効果を感じる」ことと「ROIが出た」ことは別の質問である。IBMがEMEA10カ国の経営幹部3,500人超に実施した調査（2025年9月実施）では、66%が「AIによる有意な生産性向上を実感している」と回答した一方、「ROI目標をすでに達成した」と答えたのは約20%にとどまった。平均42%が「今後12カ月で達成予定」と回答しており、「感じている」と「達成済み」の間に大きな差があることが分かる。また、従業員1,001〜5,000人規模の大企業では72%が生産性向上を実感しているのに対し、中小企業・公共セクターは55%と、組織の体力差も効果の出方に影響している（出典: IBM, 2025-10-28）。

| 見ている対象 | 指標の例 | 注意点 |
|---|---|---|
| 量（やった感） | AI利用率、生成件数、稼働時間削減 | 増えても業務KPIが動いていなければROIではない |
| 成果（動いたKPI） | コスト削減額、対応件数増、エラー率減、受注率変化 | ベースラインとの比較が必須 |

## 落とし穴

1. **「時間が減った」で終わる**：浮いた時間を他の収益業務に再配分するか、人員計画に反映しない限り、時間削減は財務的な成果に変換されない。「時間が減った」の先を必ず問う
2. **ベースラインを取らずに判断する**：導入後の「速くなった気がする」という感覚だけで判断すると、季節要因や他の改善と区別できない
3. **量の増加を成果と誤認する**：2026年10月、Googleはオープンソースのバグ報奨金制度を一時停止した。AI生成の報告が急増したものの大半が無効な内容で、審査側の負荷だけが増えて制度が機能不全に陥ったためだ。「AIで提出件数が増えた」ことは、それ自体では成果を意味しない典型例といえる（出典: TechCrunch, 2026-10-04）

## 実務への接続

学習記事047（ユースケース発掘）で選んだ「効く業務」について、着手前にこの4要素（指標・ベースライン・コスト・比較対象）を1枚のメモにまとめておくと、導入後の「本当に効果があったのか」という問いに答えられる。特に、現場から「楽になった」という声が上がっても、それを経営層への報告に使う前に、動いたKPIが何かを確認する一手間が要る。

## 講座で使うなら
- 30秒説明: 「『効果を感じる』と『ROIが出た』は別の質問です。指標・ベースライン・コスト・比較対象の4つを先に決めておかないと、後から『本当に効果があったのか』に答えられません」
- たとえ話: ROIを測らずに導入を続けるのは、体重を測らずに「痩せた気がする」でダイエットを続けるようなもの
- 演習案: 受講者自身の業務でAIを使っている（使う予定の）作業を1つ選び、指標・ベースライン・コスト・比較対象の4項目を実際に書き出させる

## 出典・参考
- [IBM Newsroom — Two-thirds of surveyed enterprises in EMEA report significant productivity gains from AI, finds new IBM study](https://newsroom.ibm.com/2025-10-28-Two-thirds-of-surveyed-enterprises-in-EMEA-report-significant-productivity-gains-from-AI,-finds-new-IBM-study)（取得日 2026-10-05）
- [TechCrunch — Google froze its open source bug bounty program due to a 'significant rise' in AI submissions](https://techcrunch.com/2026/10/04/google-froze-its-open-source-bug-bounty-program-due-to-a-significant-rise-in-ai-submissions/)（取得日 2026-10-05）

## 関連
- [learn/intermediate/045-ab-testing-staged-rollout](045-ab-testing-staged-rollout.md)
- [learn/intermediate/047-use-case-discovery](047-use-case-discovery.md)
- [daily/2026-10-05](../../daily/2026-10-05.md)
