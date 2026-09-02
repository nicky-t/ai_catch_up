---
type: thread
title: "AI学習と著作権をめぐる訴訟・議論（ai-copyright）"
slug: ai-copyright
created: 2026-08-24
updated: 2026-09-03
tags: [copyright, regulation]
status: active
related: [topics/anthropic.md]
---

# AI学習と著作権をめぐる訴訟・議論（ai-copyright）

## 何の流れか
著作権のある書籍・記事などをAIモデルの学習に使うことの合法性をめぐる訴訟・判例を追うストーリーライン。1976年に制定された著作権法をAI時代にどう解釈するかが判例ごとに積み上がっている段階で、企業の学習データ調達方針・講座での「AIと著作権」の説明材料になる。

## 現在地（最新の要約）
<!-- 新規作成時に 3〜5 行で埋める。以後は週次 agent が更新 -->
- AI学習の合法性は「フェアユース（公正利用）」に該当するかどうかで判断が割れており、統一的な結論は出ていない
- Anthropicは2025年、学習データを違法な海賊版サイトから調達した点を理由に著作者らへ15億ドルを支払う和解に応じた。担当判事はLLMの学習行為自体（データの入手経路ではなく）は適法と判断した
- 2026年8月、Sony Music・Warner Chappellら音楽出版社が「歌詞・楽譜を違法トレント経由で取得し学習に使った」としてAnthropicを新たに提訴。2026年1月のConcord・UMG訴訟（2万曲規模）に続く音楽業界からの追加提訴で、著作権リスクは書籍だけでなく音楽分野にも広がっている
- Thomson Reuters対Ross Intelligenceの訴訟では、競合サービスを作る目的での学習は「変容的」と言えず著作権侵害と認定されており、学習の「目的」次第で結論が変わりうる
- 日本は法的拘束力のない「プリンシプル・コード」（2026年8月策定）で透明性・知財保護の自主的対応を促す方針を取っており、米国の訴訟ラッシュとは対照的に緩やかなアプローチが続いている

## 経緯
<!-- agent が日付順に追記。新しいものを上に -->
- 2026-09-03: トランプ政権が、NYT対OpenAIの著作権訴訟（米ニューヨーク州南部地区連邦地裁）にOpenAI寄りの立場を示す20ページの意見書を提出。「AI産業の競争力維持」を理由にフェアユースの狭い解釈を批判。法的拘束力はないが行政府の立場表明として注目される（[daily](../daily/2026-09-03.md) / [出典](https://techcrunch.com/2026/09/02/u-s-government-sides-with-openai-on-issue-of-training-llms-on-copyrighted-material/)）
- 2026-09-03: Anthropicが「Claude Fable 5.1」のシステムプロンプトに、歌詞・詩・書籍の一節を一切再生成しない新しい制約を追加していたことをSimon Willison氏が確認。8月末のSony Music・Warner Chappellによる歌詞学習訴訟のタイミングと符合すると指摘（[daily](../daily/2026-09-03.md) / [出典](https://simonwillison.net/2026/Sep/2/claudes-new-system-prompt/)）
- 2026-08-29: Sony Music・Warner Chappellら音楽出版社がAnthropicを提訴。歌詞・楽譜を含む著作物を違法トレント経由で取得したと主張し「意図的な海賊行為」と表現。2026年1月のConcord・UMG訴訟（2万曲規模）に続く音楽業界からの追加提訴（[daily](../daily/2026-08-30.md) / [出典](https://techcrunch.com/2026/08/29/sony-music-warner-sue-anthropic-alleging-a-brazen-campaign-of-intellectual-property-theft/)）
- 2026-08-26: 日本政府が生成AI事業者向けに「プリンシプル・コード」を策定。情報公表・権利者からの照会対応など透明性確保と知財保護を促す内容だが、法的拘束力はなく事業者の自主的対応を求めるもの（[daily](../daily/2026-08-26.md) / [出典](https://www.itmedia.co.jp/aiplus/article/2608/25/2000000767/)）
- 2026-08-24: TechCrunchが著作権のある書籍でのAI学習の合法性を整理。Anthropicの15億ドル和解（Alsup判事：データ入手経路は違法だが学習行為自体は適法）とThomson Reuters対Ross Intelligence（競合目的の学習は著作権侵害）を対比（[daily](../daily/2026-08-24.md) / [出典](https://techcrunch.com/2026/08/23/is-it-legal-to-train-ai-models-on-copyrighted-books-its-complicated/)）

## 論点・見立て
- 「データの入手経路が適法か」と「学習の目的が競合製品作りかどうか」の2軸で判断が分かれる傾向が見えてきている
- 著作権法自体が1976年制定のためAI時代を想定しておらず、判例の積み重ねが実質的なルール形成を担っている

## 関連
- [topics/anthropic](../topics/anthropic.md)
