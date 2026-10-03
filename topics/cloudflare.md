---
type: topic
title: "Cloudflare（クラウドフレア）"
slug: cloudflare
created: 2026-10-04
updated: 2026-10-04
tags: [cloudflare, agent, cost]
level: beginner
audience: [engineer, business, instructor]
related: [topics/jev.md, topics/amazon.md, topics/mcp.md]
---

# Cloudflare（クラウドフレア）

## 一言で
Webサイトの高速化・保護（CDN・セキュリティ）を主力とする米国のインフラ企業。2026年はAIエージェント向けのセキュリティSkillや、判定専用AIモデルなど、エージェント時代の「裏方の部品」を次々に公開している。

## 仕組み
- コーディングエージェントをセキュリティ監査官に変える公式Skill「security-audit-skill」を2026年9月に公開し、GitHubトレンドで急拡大した実績がある
- 2026年10月、文章を生成せず「はい／いいえ」のような判定結果を確率付きで返す決定専用モデル「Clef」「Clef-flash」を公開。中央値レイテンシはClefが209.3ミリ秒、軽量版Clef-flashが38.8ミリ秒で、Function calling精度を測るBFCLで98.47%・API-Bankで91.93%を記録。自社の脅威インテリジェンスチームでの検証では、サイト分類処理がClefで2.2秒、汎用LLM「gpt-oss-120b」で4.7秒だったという（出典: [Cloudflare — Introducing Clef](https://blog.cloudflare.com/clef-decision-models)、取得日 2026-10-04）
- 強化学習（RL）によるファインチューニング基盤も同時公開し、利用者が自社データでモデルを調整できるようにした

## 実務での使い方
- 「文章を書く」ではなく「分類・判定する」だけで済む業務（スパム判定・カテゴリ分類・ルーティング振り分けなど）は、Clefのような専用モデルに切り出すとレイテンシ・コストの両面で有利になりうる
- セキュリティ監査Skillのように、Cloudflareは「自社インフラの運用で検証した仕組み」をそのままオープンソースのSkill・モデルとして公開する傾向があり、導入前の実績確認に役立つ

## 講座で使うなら
- 30 秒説明: 「Webサイトを高速化・保護する会社ですが、最近はAIエージェント向けの“裏方の部品”（セキュリティSkill・判定専用モデル）も作っています」
- たとえ話: 建物の警備会社が、AI時代には「出入りを一瞬で判定するゲート」まで作るようになった
- 演習案: 自社の業務の中で「判定・分類だけ」のタスクを1つ挙げ、Clef的な専用モデルに切り出すとレイテンシ・コストがどう変わりそうか試算させる

## この話題の流れ
<!-- agent が日付順に追記。新しいものを上に -->
- 2026-10-04: 判定専用AIモデル「Clef」「Clef-flash」を公開。9月のTypeSafe AI「Jev」、OpenAI「Decisions API」、AWS系「Strands Decider」に続き、判定特化型モデルへの参入は4社目（[daily](../daily/2026-10-04.md) / [topics/jev](jev.md)）

## 関連
- [topics/jev](jev.md)（同種の判定特化モデル）
- [topics/amazon](amazon.md)（同系統の「Strands Decider」）
- [topics/mcp](mcp.md)（過去に公開したセキュリティ監査Skillの文脈）
