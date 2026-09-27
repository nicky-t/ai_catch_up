---
type: learn
track: intermediate
number: 041
title: "評価データセットの作り方：業務タスクをどう切り出すか"
date: 2026-09-28
level: intermediate
audience: [engineer, business]
tags: [evaluation]
reading_minutes: 4
sources:
  - url: https://platform.claude.com/docs/en/test-and-evaluate/develop-tests
    title: "Anthropic — Develop test cases"
    fetched: 2026-09-28
  - url: https://developers.openai.com/cookbook/examples/evaluation/getting_started_with_openai_evals
    title: "OpenAI Cookbook — Getting Started with OpenAI Evals"
    fetched: 2026-09-28
related: [topics/llm-as-a-judge.md]
---

# 041 評価データセットの作り方：業務タスクをどう切り出すか

!!! abstract "この記事で説明できるようになること"
    - 業務タスクを評価用の「テストケース」にどう切り出すかを説明できる
    - テストケース数の目安とエッジケースを混ぜる理由を説明できる
    - 自動採点とLLM判定（LLM-as-a-judge）をどう使い分けるか判断できる

## 仕組み

評価データセットづくりは、①成功基準の定義 → ②評価タイプの選択 → ③テストケースの収集 → ④採点（自動 or LLM判定） → ⑤分析、という手順で進む。

最初の関門は①だ。「良い回答ができている」のような曖昧な基準では評価にならない。Anthropicの公式ガイドは「精度85%以上」「毒性のある回答が1万試行中0.1%未満」のように、**数値化できる基準**を先に決めることを勧めている（出典: Anthropic「Develop test cases」）。

②では、タスクの性質によって採点方法を変える。分類・SQL生成のように正解が1つに決まるタスクは「完全一致」で機械的に採点できるが、トーンや要約の質のように正解が1つに決まらないタスクは、別のLLMに採点させる「LLM判定（LLM-as-a-judge、[topics/llm-as-a-judge](../../topics/llm-as-a-judge.md)）」が使われる。

③のテストケース数について、Anthropicのガイドは評価タイプ別に目安を示している。完全一致（分類タスク）は1,000件以上、要約評価（ROUGE-L）は200件以上、LLM判定によるトーン評価は100件以上といった具合だ。一方、OpenAIのCookbookが例に使うSQL生成タスクでは、実行デモは25件、参考にした公開ベンチマーク「Spider」は194件と、実務の検証段階ではもっと少ない件数からでも始められることが分かる（出典: OpenAI Cookbook「Getting Started with OpenAI Evals」）。**「まず小さく作って回し、失敗を見つけたら増やす」で始めて問題ない。**

## 比較・判断基準

| 評価タイプ | 向いているタスク例 | テストケース数の目安 |
|---|---|---|
| 完全一致 | 分類・SQL生成など正解が1つに決まるタスク | 1,000件以上（小規模パイロットは100〜500件） |
| ROUGE-L | 要約 | 200件以上 |
| コサイン類似度 | 表現は違うが同じ意味の応答の一貫性評価 | 50グループ（各3〜5問） |
| LLM判定（リカートスケール） | トーン・スタイルなど段階評価が必要なもの | 100件以上 |
| LLM判定（二値分類） | 安全性・プライバシー違反の有無など | 500件以上 |

（出典: Anthropic「Develop test cases」）

## 落とし穴

1. **件数不足で本番のエラーを検出できない**：件数を絞りすぎると、実際の入力に含まれる例外パターンを一度も評価しないまま「合格」してしまう
2. **エッジケースを混ぜ忘れる**：皮肉・誤字・言語混在・空入力・極端に長い入力など、実務で必ず出会う「ひっかけ」を最初から一定比率（目安15〜20%）で混ぜないと、平時は高得点でも本番でつまずく
3. **生成と評価に同じモデルを使う**：LLM判定を使う場合、テストケースを作ったモデルと採点するモデルが同じだと、自分の出力を甘く評価しやすい（自己評価バイアス）。採点は別モデルに任せるのが基本

## 実務への接続

社内業務のタスクを評価データセット化する手順は次のようになる：①過去の対応ログ・問い合わせ履歴から実例をサンプリングする、②カテゴリ（定型／例外／クレーム対応など）に分ける、③正解（期待する出力）を人間がラベル付けする、④エッジケース（皮肉・誤字・長文・無関係な入力など）を意図的に追加する。100〜500件程度の小規模パイロットから始めれば、AI導入の判断材料として十分な精度感がつかめる。

## 講座で使うなら

- 30 秒説明: 「AIの出来を確かめるための問題集を作る作業です。標準的な問題だけでなく、ひっかけ問題（皮肉・誤字・長文など）も混ぜておくのがポイントです」
- たとえ話: 入試の過去問集を作るとき、素直な問題だけでなく、受験生が間違えやすい応用問題や紛らわしい選択肢も混ぜておくのと同じ
- 演習案: 受講者の業務で「AIに任せたい判断」を1つ挙げ、それを10件のテストケース（正解付き）に書き出させる。うち2件は必ずエッジケース（例外的な入力）にする

## 出典・参考
- [Anthropic — Develop test cases](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)（取得日 2026-09-28）
- [OpenAI Cookbook — Getting Started with OpenAI Evals](https://developers.openai.com/cookbook/examples/evaluation/getting_started_with_openai_evals)（取得日 2026-09-28）

## 関連
- [topics/llm-as-a-judge](../../topics/llm-as-a-judge.md)
