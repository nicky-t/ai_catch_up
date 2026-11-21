---
type: topic
title: "AMD（エーエムディー）"
slug: amd
created: 2026-09-30
updated: 2026-11-22
tags: [amd, nvidia]
level: beginner
audience: [engineer, business, instructor]
related: [topics/nvidia.md, topics/anthropic.md]
---

# AMD（エーエムディー）

## 一言で
GPU・CPUを手掛ける米半導体メーカー。AI向けチップ市場でNvidiaに次ぐ立場から、モデル開発企業の買収を通じてハードウェアとAIモデルの垂直統合に乗り出している。

## 仕組み
- 従来はGPU・CPUなどハードウェアの供給が事業の中心だったが、2026年9月にFei-Fei Li氏が創業した「World Labs」（空間知能・物理AIに強みを持つモデル開発企業）を82億ドルで買収すると発表。買収は規制当局の承認を前提に年内完了予定で、Li氏はAMDの執行副社長（EVP）兼チーフサイエンティストに就任する。AMDは「モデル研究・システム・コンピュートにおける緊密な協力」が必要と説明している（出典: [TechCrunch — AMD will acquire Fei-Fei Li's World Labs for $8.2 billion](https://techcrunch.com/2026/09/28/amd-will-acquire-fei-fei-lis-world-labs-for-8-2-billion/)、取得日 2026-10-04）
- Nvidiaとの競合において、GPU単体の性能競争だけでなく「どんなモデル・ワークロードを想定してチップを設計するか」という川上の技術理解を取り込む狙いがあるとされる

## 実務での使い方
- 自社のAI基盤をどのハードウェアベンダーに依存させるかを検討する際、チップメーカー自身がどのようなモデル技術を保有しているかも選定材料になりうる
- 性能面では、AIチップ「Instinct」シリーズの新型「MI400」（2026年投入予定）がFP4演算で最大40 petaflops、メモリ・帯域幅・拡張性は現行の競合製品比で50%向上するとAMDは説明（AMD自身の主張で第三者検証ではない点に留意）。1ラックに最大72GPUを搭載するプラットフォーム「Helios」との組み合わせで世代間10倍の性能向上を見込むという。前世代「MI355」は2025年6月に量産開始済みで、NvidiaのB200・GB200と競合する位置づけ
- 採用事例としては、AnthropicがAMDとの戦略的提携でMI450シリーズGPUを最大2GW導入する契約を結んでおり（2026年7月22日発表）、最初の1GW分は2027年上半期に稼働開始予定。AMDはAnthropicへ将来最大50億ドルの戦略的出資を約束している（出典: [AMD公式プレスリリース — AMD and Anthropic Announce Strategic Partnership to Deploy Up to 2 Gigawatts of AMD Instinct MI450 Series GPUs](https://ir.amd.com/news-events/press-releases/detail/1292)、取得日2026-11-15）。World Labs買収は2026年11月16日に完了。Fei-Fei Li氏はAMDの執行副社長（EVP）兼チーフサイエンティストとして会長兼CEOのリサ・スー氏に直接報告する体制となり、共同創業者のJustin Johnson氏・Ben Mildenhall氏がLi氏とともに基盤モデル研究チームを率い続け、AMDのエンジニアと協力して将来のハードウェア・ソフトウェア・コンピューティングシステムに知見を反映させる役割を担う。具体的な人員数は非公表（出典: [HPCwire — AMD Completes Acquisition of World Labs](https://www.hpcwire.com/aiwire/2026/11/16/amd-completes-acquisition-of-world-labs/)、取得日2026-11-22）

## 講座で使うなら
- 30 秒説明: 「PCやサーバー向けのチップを作っている会社で、Nvidiaのライバルにあたります。最近はAIモデルを作る会社を買収して、チップとモデルの両方を持とうとしています」
- たとえ話: エンジンだけを作っていたメーカーが、車体設計の会社を買収して自動車そのものを手掛け始めるようなもの
- 演習案: 「チップメーカーがモデル開発企業を買収する」ことのメリット・デメリットを、Nvidia（買収せず供給に専念）と比較して議論させる

## この話題の流れ
<!-- agent が日付順に追記。新しいものを上に -->
- 2026-11-22（週次整理・要追記対応）: World Labs買収が2026年11月16日に完了したと発表。Fei-Fei Li氏はAMD執行副社長（EVP）兼チーフサイエンティストとしてリサ・スーCEOに直接報告する体制になり、共同創業者2人がLi氏とともに研究チームを継続して率いる。買収額約82億ドルは9月発表時点の金額（完了発表自体には再掲なし）（[出典](https://www.hpcwire.com/aiwire/2026/11/16/amd-completes-acquisition-of-world-labs/)、取得日2026-11-22）
- 2026-11-15（週次整理・要追記対応）: AMDとAnthropicが2026年7月22日に戦略的提携を発表していたことを一次情報で確認。AMD Instinct MI450シリーズGPU（Heliosラックスケール搭載）を最大2GW導入する契約で、最初の1GWは2027年上半期稼働開始予定。AMDはAnthropicへ将来最大50億ドルの戦略的出資を約束（[出典](https://ir.amd.com/news-events/press-releases/detail/1292)、取得日2026-11-15）
- 2026-10-29: Metaとの戦略的提携拡大を発表（10月27日、現地時間）。ラックスケール基盤「Helios」の初期導入分がMetaに設置されテスト中で、Museを稼働させる専用環境にEPYCプロセッサ、学習・ランキング・レコメンドにInstinct GPUを提供。Metaが10月26日発表した最大950億ドル規模の株式発行計画に10億ドルを出資（[daily](../daily/2026-10-29.md) / [topics/nvidia](nvidia.md) / [topics/meta](meta.md) / [出典](https://www.itmedia.co.jp/news/article/2610/28/2000002651/)）
- 2026-10-25（週次整理・要追記対応）: AIチップ「Instinct」の新型「MI400」（FP4演算で最大40 petaflops、2026年投入予定）・ラックスケール基盤「Helios」（1ラック最大72GPU）の性能主張を2025年8月のDIGITIMES記事で確認。大口顧客からMI400導入への関心表明はあるが、具体的な採用企業名は同記事に記載なし（[出典](https://www.digitimes.com/news/a20250806VL202.html)、取得日2026-10-25）
- 2026-09-30: Fei-Fei Li氏が創業した「World Labs」を82億ドルで買収すると発表。Li氏はAMDの最高経営責任者補佐・最高科学者として参画する。テキスト・映像ベースのモデル提供が中心だった自社製品群に、世界モデル技術を加える狙い。買収は年内完了予定（[daily](../daily/2026-09-30.md) / [topics/nvidia](nvidia.md)）

## 関連
- [topics/nvidia](nvidia.md)
