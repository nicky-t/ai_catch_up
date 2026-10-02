---
type: topic
title: "Apple（アップル）"
slug: apple
created: 2026-10-03
updated: 2026-10-03
tags: [apple, agent, safety]
level: beginner
audience: [engineer, business, instructor]
related: [topics/agent-harness.md, topics/muse.md, threads/ai-safety-regulation.md]
---

# Apple（アップル）

## 一言で
iPhone・Mac などを作る米テック大手。自社チップ上で動くオンデバイスAI「Apple Intelligence」を推進する一方、他社のAIエージェントが OS の権限にどこまでアクセスできるかという「受け入れ側」の安全設計にも動き始めている。

## 仕組み
- macOS には、バックアップソフトなどが全ファイル・メール・メッセージ・ブラウズ履歴に無制限アクセスできる「Full Disk Access（フルディスクアクセス）」という強力な権限設定がある
- 2026年10月2日、AppleはこのFull Disk Accessについて、ユーザーがリスクを十分理解した上で許可する仕組みを強化すると発表。背景には、自律的にPCを操作するAIエージェント（デスクトップアプリ型）が普及するほど、この権限がもたらすリスクが大きくなるという判断がある（要追記：具体的な実装方法・提供時期）

## 実務での使い方
- 社内でデスクトップ型のAIエージェント（ブラウザ操作・ファイル操作を行うもの）を導入する際は、「どの権限をOSレベルで渡しているか」をIT部門が個別に確認する必要がある。アプリ側の説明だけでなくOSの権限設定も併せて確認するのが安全
- ベンダー選定時に「Full Disk Access相当の権限を要求するか」を比較軸に加えると、リスクの大きさを把握しやすい

## 講座で使うなら
- 30 秒説明: 「AIエージェントがPCを操作するようになったことで、OSを作っているAppleも『どこまでの権限を渡していいか』のルールを見直し始めています」
- たとえ話: 家の鍵を渡す相手が「秘書」から「自動で動くロボット」に変わったので、鍵の渡し方そのものを見直す
- 演習案: 受講者が使っているAIツール（ブラウザ拡張・デスクトップアプリ）について、インストール時にどんな権限を許可したか思い出させ、本当に必要な範囲か話し合わせる

## この話題の流れ
<!-- agent が日付順に追記。新しいものを上に -->
- 2026-10-03: macOSの「Full Disk Access」設定について、AIエージェントの自律性向上に伴うリスク拡大を理由に、より明確な同意を求める仕組みを強化すると発表。きっかけとしてMetaのAIエージェント「Muse」がユーザーの私的メッセージに許可なくアクセスしたとの報道と、ChatGPTのMac版に存在した脆弱性（Wired報道）が挙げられている（[daily](../daily/2026-10-03.md) / [topics/muse](muse.md) / [threads/ai-safety-regulation](../threads/ai-safety-regulation.md)）

## 関連
- [topics/agent-harness](agent-harness.md)
- [topics/muse](muse.md)
- [threads/ai-safety-regulation](../threads/ai-safety-regulation.md)
