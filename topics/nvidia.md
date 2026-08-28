---
type: topic
title: "NVIDIA（エヌビディア）"
slug: nvidia
created: 2026-08-28
updated: 2026-08-29
tags: [nvidia]
level: beginner
audience: [engineer, business, instructor]
related: [topics/hugging-face.md, topics/anthropic.md]
---

# NVIDIA（エヌビディア）

## 一言で
AIモデルの学習・推論に使われるGPU（画像処理用半導体）を主力とする米国の半導体企業。AIブームの計算需要をほぼ一手に引き受け、AI企業各社の計算基盤契約・投資の中心的な存在になっている。

## 仕組み
- 主力製品はデータセンター向けGPU。世代ごとに「Vera Rubin」のような開発コード名が付き、AI各社が次世代チップの調達を競っている（要追記：GPU世代とアーキテクチャの詳細な対応表）
- 自社製品の販売だけでなく、有望なAI関連企業への出資（例：Hugging Faceへの出資提案）や、自社チップを使う企業への大型計算基盤契約という形でもエコシステムに関わる
- 2026年8月、AIモデル共有プラットフォームのHugging Faceを129億ドルで買収することに合意したと報じられた（未確定、[topics/hugging-face](hugging-face.md)）

## 実務での使い方
- AI導入のコスト構造を理解する上で、モデル提供企業（OpenAI・Anthropicなど）だけでなく、その計算基盤を支えるNVIDIAの動向（供給状況・チップ価格）も間接的にサービス価格に影響しうる点を押さえておく（要追記：チップ需給とAPI価格の関係の具体例）

## 講座で使うなら
- 30 秒説明: 「AIの計算に使われる半導体（GPU）を作っている会社です。AI各社がこぞってNVIDIA製チップを大量に調達しており、AIブームの裏方的な存在になっています」
- たとえ話: AIというゴールドラッシュにおける「つるはしとシャベル」を売る会社
- 演習案: 「AIサービスの利用料金が上がったとしたら、その背景にどんな要因（チップ調達コストなど）があり得るか」を受講者に洗い出させる

## この話題の流れ
<!-- agent が日付順に追記。新しいものを上に -->
- 2026-08-28: オープンウェイトAI企業の買収競争が加速——NVIDIAはHugging Face（約130億ドル）に加えPoolsideも60億ドルで買収。企業のオープンウェイトモデル利用率は6%・利用エンジニアは2%とまだ少数派（[daily](../daily/2026-08-29.md)）
- 2026-08-28: Hugging Face買収交渉が最終段階に。129億ドル規模だが正式合意はまだ（[daily](../daily/2026-08-28.md)）
- 2026-08-28: Anthropicが英Nscaleと締結した6年450億ドルの計算基盤契約で、次世代チップ「Vera Rubin」が使用される（[daily](../daily/2026-08-28.md)）

## 関連
- [topics/hugging-face](hugging-face.md)
- [topics/anthropic](anthropic.md)
