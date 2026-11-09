---
type: thread
title: "AI学習と著作権をめぐる訴訟・議論（ai-copyright）"
slug: ai-copyright
created: 2026-08-24
updated: 2026-11-10
tags: [copyright, regulation]
status: active
related: [topics/anthropic.md]
---

# AI学習と著作権をめぐる訴訟・議論（ai-copyright）

## 何の流れか
著作権のある書籍・記事などをAIモデルの学習に使うことの合法性をめぐる訴訟・判例を追うストーリーライン。1976年に制定された著作権法をAI時代にどう解釈するかが判例ごとに積み上がっている段階で、企業の学習データ調達方針・講座での「AIと著作権」の説明材料になる。

## 現在地（最新の要約）
<!-- 新規作成時に 3〜5 行で埋める。以後は週次 agent が更新 -->
- 【2026-11-03】NYTなど4メディアによるBrave提訴で動きが再開し、4週間ぶりに`dormant`から`active`へ復帰
- NYTなど4メディアがBraveを提訴した訴状で、Anthropic・Perplexity・Mistral・xAI・Cohereを「盗品コンテンツの販売先」と名指し。訴訟の矛先が「AI企業」から「データ供給元（ブラウザ・検索）」まで広がったことを示す事例（11/3）
- 国内では、ライセンス作品を扱う広告配信の現場でもリスクが現実化：宅配ピザチェーン「ピザーラ」が、TikTok広告のAI自動生成・配信機能が既定で有効になっていたため無許可のAI生成広告が配信されたとして謝罪（11/6）
- 訴訟・行政府の意見表明に加え、サイト運営者側の技術的な対抗手段も増えた：Cloudflareが「検索クロールは許可、AI学習だけ拒否」を両立できるrobots.txt設定を新たに公開（Google・Appleは対応済み）。訴訟の行方を待つだけでなく、事業者自身がAI学習への同意・不同意を選別できる手段が実務レベルで整い始めている
- AI学習の合法性は「フェアユース（公正利用）」に該当するかどうかで判断が割れており、統一的な結論は出ていない。トランプ政権は9月2日、NYT対OpenAIの著作権訴訟にOpenAI寄りの意見書を提出し、「AI産業の競争力維持」を理由にフェアユースの狭い解釈を批判——司法判断だけでなく行政府の立場表明という3つ目の力学が明示的に加わった
- Anthropicは2025年、学習データを違法な海賊版サイトから調達した点を理由に著作者らへ15億ドルを支払う和解に応じた。担当判事はLLMの学習行為自体（データの入手経路ではなく）は適法と判断した
- 2026年9月、その和解金（約50万タイトル・1作品3,000ドル）の配分方法をめぐり著者らが出版社を批判。現役契約作品は著者・出版社で50-50分配だが、自費出版や版権失効済み作品でも出版社が請求するケースが複数報告され、「和解が成立した後の実務」という新しい論点が浮上した
- 2026年8月末、Sony Music・Warner Chappellら音楽出版社が「歌詞・楽譜を違法トレント経由で取得し学習に使った」としてAnthropicを新たに提訴。これを受けAnthropicは「Claude Fable 5.1」のシステムプロンプトに歌詞・詩・書籍の一節を再生成しない制約を追加したことが判明しており、訴訟が製品側の挙動にも直接影響し始めている
- Thomson Reuters対Ross Intelligenceの訴訟では、競合サービスを作る目的での学習は「変容的」と言えず著作権侵害と認定されており、学習の「目的」次第で結論が変わりうる
- 日本は法的拘束力のない「プリンシプル・コード」（2026年8月策定）で透明性・知財保護の自主的対応を促す方針を取っており、米国の訴訟ラッシュ・行政府の介入とは対照的に緩やかなアプローチが続いている

## 経緯
<!-- agent が日付順に追記。新しいものを上に -->
- 2026-11-10: ソニーAIなどの研究者が、画像生成AI14モデル（オープンウェイト3種・商用11種）を対象に既存の知的財産（有名人・アニメキャラ・企業ロゴなど201件）の再現度を調査。オープンウェイト3種は拒否率0%、商用モデルも拒否率にかかわらず全14モデルが10%以上の確率で認識可能なIPを生成し、半数近くは40%を超えた。名前を伏せた間接的な指示でも平均27〜28%の確率でIPが生成されたという。「ガードレールがある」ことと「実際にIPを生成しない」ことが別問題であることを数字で示した研究（[daily](../daily/2026-11-10.md) / [出典](https://www.itmedia.co.jp/news/article/2611/09/2000002982/)）
- 2026-11-07: 宅配ピザチェーン「ピザーラ」を運営するフォーシーズが、アニメ「Dr.STONE」とのコラボCMに関し謝罪。TikTok広告プラットフォームのAI自動生成・配信機能が有効になっていたことが原因で、製作委員会の事前監修・許諾を得ていない動画が配信されていたという。米国での訴訟ラッシュとは異なる「広告プラットフォームの既定機能が無断でAI生成物を配信した」という、ライセンス作品を扱う事業者側のリスクの実例（[daily](../daily/2026-11-07.md) / [出典](https://www.itmedia.co.jp/aiplus/article/2611/06/2000002937/)）
- 2026-11-03: New York Timesが、プライバシー重視ブラウザ「Brave」をニューヨーク連邦地裁に提訴。NYTの著作権コンテンツを無断収集し、Anthropic・Perplexity・Mistral・xAI・Cohereという名指しした顧客企業へ不正配信したと主張。同日Daily News・Chicago Tribune・Orlando Sentinelも同様の訴訟を起こした。Braveは独自クローラーで300億ページ超を索引化しサイト側がブロックできない点、有料記事の壁を回避する機能も問題視されている。4週間動きがなく`dormant`としていたが本件で`active`に戻す（[daily](../daily/2026-11-03.md) / [topics/anthropic](../topics/anthropic.md) / [出典](https://techcrunch.com/2026/11/02/new-york-times-and-other-outlets-sue-web-browser-brave-over-alleged-content-scraping/)）
- 2026-09-18: Cloudflareが、Webサイト運営者が検索エンジンのクロールを許可したまま同じクローラーによるAI学習だけを拒否できる新機能を発表。従来はGoogle・Apple・Microsoftなど「検索とAI学習を兼ねるクローラー」を拒否すると検索クロールごとブロックされていたが、robots.txtの記載でこの両立が可能に。GoogleとAppleは対応済み、Microsoftは2027年初頭までに対応予定。OpenAI・Anthropic・Meta・Amazonは元々検索用と学習用のクローラーを分けており、この機能を使わずとも学習用のみ拒否できる。訴訟・行政府の介入とは別の、サイト運営者側の技術的な対抗手段が一つ増えた形（[daily](../daily/2026-09-18.md) / [出典](https://www.itmedia.co.jp/aiplus/article/2609/17/2000001584/)）
- 2026-09-07: Anthropicの著作権和解金（15億ドル・約50万タイトル・1作品3,000ドル）の配分方法をめぐり著者らが出版社に異議。現役契約作品は50-50分配だが、自費出版・版権失効済み作品は著者全額のはずが、出版社の過大請求（例：版権失効から17年以上経過した作品へのHarperCollinsの請求）が複数報告された。Writers BewareのVictoria Strauss氏は「単純なシステムエラーを超えた体系的な問題の可能性」を指摘（[daily](../daily/2026-09-07.md) / [出典](https://techcrunch.com/2026/09/06/authors-push-back-as-publishers-and-agents-seek-share-of-anthropic-settlement/)）
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
