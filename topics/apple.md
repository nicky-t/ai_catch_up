---
type: topic
title: "Apple（アップル）"
slug: apple
created: 2026-10-03
updated: 2026-11-06
tags: [apple, agent, cost]
level: beginner
audience: [engineer, business, instructor]
related: [topics/agent-harness.md, topics/muse.md, threads/ai-safety-regulation.md]
---

# Apple（アップル）

## 一言で
iPhone・Mac などを作る米テック大手。自社チップ上で動くオンデバイスAI「Apple Intelligence」を推進する一方、他社のAIエージェントが OS の権限にどこまでアクセスできるかという「受け入れ側」の安全設計にも動き始めている。

## 仕組み
- macOS には、バックアップソフトなどが全ファイル・メール・メッセージ・ブラウズ履歴に無制限アクセスできる「Full Disk Access（フルディスクアクセス）」という強力な権限設定がある
- 2026年10月2日、AppleはこのFull Disk Accessについて、ユーザーがリスクを十分理解した上で許可する仕組みを強化すると発表。背景には、自律的にPCを操作するAIエージェント（デスクトップアプリ型）が普及するほど、この権限がもたらすリスクが大きくなるという判断がある。発表文には「非常に明示的なユーザー操作」のみで許可できるようにするという方針のみが示され、具体的なUI・実装方法、対応macOSバージョン、既存の許可設定をリセットするかどうかは2026年10月時点で未公表（出典: [MacRumors — Apple Announces 'Full Disk Access' Changes on macOS Due to AI Agents](https://www.macrumors.com/2026/10/02/apple-announces-macos-full-disk-access-changes/)、取得日 2026-10-11）

## 実務での使い方
- 社内でデスクトップ型のAIエージェント（ブラウザ操作・ファイル操作を行うもの）を導入する際は、「どの権限をOSレベルで渡しているか」をIT部門が個別に確認する必要がある。アプリ側の説明だけでなくOSの権限設定も併せて確認するのが安全
- ベンダー選定時に「Full Disk Access相当の権限を要求するか」を比較軸に加えると、リスクの大きさを把握しやすい

## 講座で使うなら
- 30 秒説明: 「AIエージェントがPCを操作するようになったことで、OSを作っているAppleも『どこまでの権限を渡していいか』のルールを見直し始めています」
- たとえ話: 家の鍵を渡す相手が「秘書」から「自動で動くロボット」に変わったので、鍵の渡し方そのものを見直す
- 演習案: 受講者が使っているAIツール（ブラウザ拡張・デスクトップアプリ）について、インストール時にどんな権限を許可したか思い出させ、本当に必要な範囲か話し合わせる

## この話題の流れ
<!-- agent が日付順に追記。新しいものを上に -->
- 2026-11-06: Bloomberg報道によると、社内エンジニアリング部門が1日に使えるAI利用予算の上限を10月に300ドルから200ドルへ引き下げ、今後一部では100ドルまで下げる見通し。エンジニア以外の部門では1日25ドルという低い上限も検討中という。2026年前半の「tokenmaxxing」ブームからの転換を示す事例（[daily](../daily/2026-11-06.md) / [threads/ai-productivity-employment](../threads/ai-productivity-employment.md) / [出典](https://techcrunch.com/2026/11/04/apple-is-reportedly-cutting-budgets-for-its-internal-ai-usage/)）
- 2026-11-04: App Storeの審査方針を変更し、出会い系・恋愛関係機能を持つアプリを18+指定に。恋愛・性的コンテンツを提供するAI恋人（コンパニオン）アプリも対象になりうるとされ、11月16日からはアプリの機能に即した年齢指定のための新しいコンテンツ記述子の追加が必須化。位置情報を他者と共有する機能の開示も義務化（[daily](../daily/2026-11-04.md) / [threads/ai-safety-regulation](../threads/ai-safety-regulation.md) / [出典](https://techcrunch.com/2026/11/03/apple-restricts-dating-apps-and-ai-companions-to-users-18-and-up/)）
- 2026-11-02: 2026年9月就任の新CEOジョン・ターナス氏がWiredのインタビューで「We don't want to ship AI for AI's sake.」と発言し、AI機能そのものを目的化しない方針を明言。新製品でAIを「間違いなく活用する」としつつ、AIエージェントによるアプリ代替の可能性には「ものづくりは深く人間的で個人的なこと」と述べ慎重な姿勢を示した（[daily](../daily/2026-11-02.md) / [出典](https://techcrunch.com/2026/10/31/apple-ceo-says-the-company-doesnt-want-to-ship-ai-for-ais-sake/)）
- 2026-10-11: AIパーソナライズポッドキャスト企業Huxe（5月閉鎖、NotebookLMのポッドキャスト機能の元開発者が創業）の一部従業員の雇用と技術の非独占的ライセンスに合意したと、欧州委員会への届出で判明。会社全体を買収しない「リバース・アクイハイア」方式で、Podcastsアプリへのパーソナライズ音声機能追加が推測されている（[daily](../daily/2026-10-11.md)）
- 2026-10-03: macOSの「Full Disk Access」設定について、AIエージェントの自律性向上に伴うリスク拡大を理由に、より明確な同意を求める仕組みを強化すると発表。きっかけとしてMetaのAIエージェント「Muse」がユーザーの私的メッセージに許可なくアクセスしたとの報道と、ChatGPTのMac版に存在した脆弱性（Wired報道）が挙げられている（[daily](../daily/2026-10-03.md) / [topics/muse](muse.md) / [threads/ai-safety-regulation](../threads/ai-safety-regulation.md)）

## 関連
- [topics/agent-harness](agent-harness.md)
- [topics/muse](muse.md)
- [threads/ai-safety-regulation](../threads/ai-safety-regulation.md)
