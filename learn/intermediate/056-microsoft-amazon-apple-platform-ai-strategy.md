---
type: learn
track: intermediate
number: 056
title: "Microsoft・Amazon・Apple：プラットフォーム企業のAI戦略"
date: 2026-10-13
level: intermediate
audience: [engineer, business]
tags: [microsoft, amazon, apple, adoption]
reading_minutes: 5
sources:
  - url: https://www.aboutamazon.com/news/devices/alexa-plus-available-free-prime-members-us
    title: "Alexa+ now available to everyone in the US"
    fetched: 2026-10-13
  - url: https://www.apple.com/apple-intelligence/
    title: "Apple Intelligence"
    fetched: 2026-10-13
  - url: https://github.blog/2021-06-29-introducing-github-copilot-ai-pair-programmer/
    title: "Introducing GitHub Copilot: your AI pair programmer"
    fetched: 2026-10-13
related: [topics/microsoft.md, topics/amazon.md, topics/apple.md]
---

# 056 Microsoft・Amazon・Apple：プラットフォーム企業のAI戦略

!!! abstract "この記事で説明できるようになること"
    - 学習055で見た「OpenAI・Anthropic・Google」の思想軸とは別に、既存プラットフォーム企業3社がAIをどう位置づけているかを説明できる
    - 3社の戦略の違いを「どこで動かすか」「誰の基盤モデルに乗るか」という2軸で比較できる
    - 自社の導入検討で、ベンダーの戦略の違いがどんな制約につながるかを判断できる

## 仕組み

OpenAI・Anthropic・Googleは「基盤モデルをどう作るか」で差別化するのに対し、Microsoft・Amazon・Appleは手持ちの巨大なユーザー基盤・業務システム・デバイスに「AIをどう組み込むか」で差別化している。3社の力点はそれぞれ違う。

- **Microsoft：既存ソフトウェアへの統合＋自社モデルの並行開発**。Word・Excel・TeamsにAIを組み込む「Microsoft 365 Copilot」が主力で、基盤モデルはOpenAI・Anthropic・自社開発の複数を併用する「マルチモデル」構成（[topics/microsoft](../../topics/microsoft.md)）。GitHub Copilotはこの統合戦略の最初の成功例で、2021年6月の技術プレビュー発表時点からコード生成に特化したOpenAI Codexを基盤にしていた（出典: [GitHub Blog — Introducing GitHub Copilot](https://github.blog/2021-06-29-introducing-github-copilot-ai-pair-programmer/)、取得日 2026-10-13）。2026年10月には、文章を生成せず選択肢ごとの確率を返す「判断特化」モデル「Microsoft-Decision-1」も自社開発でFoundryに投入しており、「統合」だけでなく専用モデルの自社開発にも手を広げている
- **Amazon：クラウド（AWS）という基盤の提供者**。自社のAIアシスタント「Alexa+」はAmazon Nova（自社モデル）とAnthropicのモデルを組み合わせた構成で、Prime会員は無料・非会員は月額19.99ドルで提供される（出典: [Amazon公式 — Alexa+ now available to everyone in the US](https://www.aboutamazon.com/news/devices/alexa-plus-available-free-prime-members-us)、取得日 2026-10-13）。それ以上に収益の軸になっているのはAWSで、OpenAIなど他社AI企業の学習・推論基盤を提供する「土台としてのAI活用」が特徴（[topics/amazon](../../topics/amazon.md)）
- **Apple：オンデバイス処理とプライバシーを前面に出した差別化**。「Apple Intelligence」は端末上での処理を基本とし、より大きなモデルが必要な場合のみ「Private Cloud Compute（PCC）」というサーバー側処理に送る。Apple自身は、PCCがデータを保存しない・リクエスト処理以外に使わない・プライバシーの約束を検証可能にすると説明している（出典: [Apple公式 — Apple Intelligence](https://www.apple.com/apple-intelligence/)、取得日 2026-10-13）。開発者向けには「Foundation Models」フレームワークでオンデバイスモデルを無料で呼び出せる一方、サーバー側機能には1日あたりの利用上限がある

## 比較・判断基準

| 観点 | Microsoft | Amazon | Apple |
|---|---|---|---|
| AIの主戦場 | 既存オフィスソフト・業務システム | クラウド基盤（AWS）＋Alexa+ | 端末（iPhone/Mac）上 |
| 基盤モデル | OpenAI・Anthropic・自社開発の併用 | 自社Nova＋Anthropic、他社モデルの受け入れ基盤 | 自社開発中心（詳細非公開） |
| データの扱い | テナント単位の契約（企業ごとに個別） | AWS契約に準拠 | 原則オンデバイス、必要時のみPCCでサーバー処理 |
| 収益源 | ソフトウェアのサブスク（席課金） | クラウド使用料・デバイス販売 | デバイス販売＋一部サブスク |
| 向く用途 | 既存Office業務の効率化 | 自社でAI基盤を持たず他社AIを使う企業への提供 | 個人のプライバシーを重視する用途 |

選定の判断軸はシンプルに「どこにデータを置きたいか」「既存のどの基盤に乗っているか」の2点に絞ると比較しやすい。Office中心の業務ならMicrosoft、クラウドインフラから考えるならAmazon、端末内処理を重視するならAppleという整理になる。

## 落とし穴

1. **「マルチモデル」を強みと見て、実際にどのモデルが動いているかを確認しない**。Microsoft 365 Copilotのように複数ベンダーのモデルを併用する製品では、機能ごとに基盤モデルが異なる場合があり、障害・脆弱性発生時の影響範囲を把握しにくい
2. **オンデバイス処理の「プライバシー保護」を無条件に信頼する**。Appleの説明は自社の公式な立場であり、PCCの「検証可能性」は第三者機関による継続的な外部監査を伴う主張かどうかを個別に確認する必要がある
3. **クラウド提供者（Amazon）を「中立な基盤」と思い込む**。AWSは他社AI企業の基盤でありながら、自社のAlexa+やAmazon Adsという競合サービスも展開しており、利害が完全に中立とは限らない

## 実務への接続

- ベンダー選定（学習053）の比較軸に「既存のどのシステムに統合されているか」を加えると、導入後の定着コストを見積もりやすい
- 複数ベンダーのAIを併用する企業は、学習049（セキュリティとデータ取り扱い）の観点から、機能ごとにどのモデル・どのクラウドにデータが渡るかを棚卸ししておくと、障害対応がしやすい

## 講座で使うなら

- 30 秒説明: 「OpenAIやAnthropicは『AIモデルそのもの』で勝負していますが、Microsoft・Amazon・Appleは『自分たちが元から持っている基盤（オフィスソフト・クラウド・端末）にAIをどう組み込むか』で勝負しています」
- たとえ話: 新しい発電方式を開発する会社（OpenAI等）と、既存の家に新しい発電方式を配線し直す会社（Microsoft等）の違い
- 演習案: 受講者が勤務先・自宅で使っているAI機能を1つ挙げさせ、それがどの会社の「既存基盤」に組み込まれているかを特定させる

## 出典・参考
- [Amazon公式 — Alexa+ now available to everyone in the US](https://www.aboutamazon.com/news/devices/alexa-plus-available-free-prime-members-us)（取得日 2026-10-13）
- [Apple公式 — Apple Intelligence](https://www.apple.com/apple-intelligence/)（取得日 2026-10-13）
- [GitHub Blog — Introducing GitHub Copilot: your AI pair programmer](https://github.blog/2021-06-29-introducing-github-copilot-ai-pair-programmer/)（取得日 2026-10-13）

## 関連
- [topics/microsoft](../../topics/microsoft.md)
- [topics/amazon](../../topics/amazon.md)
- [topics/apple](../../topics/apple.md)
- [learn/intermediate/055](055-openai-anthropic-google-philosophy-product-lines.md)
