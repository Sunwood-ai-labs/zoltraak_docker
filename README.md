<p align="center">
<img src="https://huggingface.co/datasets/MakiAi/IconAssets/resolve/main/Zoltraak_icon.jpeg" width="100%">
<br>
<h1 align="center">Zoltraak Docker</h1>
<h2 align="center">
  ～ General Attack Magic ～

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/MakiAi/zoltraak_docker)
[![zoltraak_docker - Sunwood-ai-labs](https://img.shields.io/static/v1?label=zoltraak_docker&message=Sunwood-ai-labs&color=blue&logo=github)](https://github.com/zoltraak_docker/Sunwood-ai-labs "Go to GitHub repo")
[![stars - Sunwood-ai-labs](https://img.shields.io/github/stars/zoltraak_docker/Sunwood-ai-labs?style=social)](https://github.com/zoltraak_docker/Sunwood-ai-labs)
[![forks - Sunwood-ai-labs](https://img.shields.io/github/forks/zoltraak_docker/Sunwood-ai-labs?style=social)](https://github.com/zoltraak_docker/Sunwood-ai-labs)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/Sunwood-ai-labs/zoltraak_docker)](https://github.com/Sunwood-ai-labs/zoltraak_docker)
[![GitHub Top Language](https://img.shields.io/github/languages/top/Sunwood-ai-labs/zoltraak_docker)](https://github.com/Sunwood-ai-labs/zoltraak_docker)
[![GitHub Release](https://img.shields.io/github/v/release/Sunwood-ai-labs/zoltraak_docker?sort=date&color=red)](https://github.com/Sunwood-ai-labs/zoltraak_docker)
[![GitHub Tag](https://img.shields.io/github/v/tag/Sunwood-ai-labs/zoltraak_docker?color=orange)](https://github.com/Sunwood-ai-labs/zoltraak_docker)

  <br>

</h2>

</p>

>[!IMPORTANT]
>このリポジトリは[SourceSage](https://github.com/Sunwood-ai-labs/SourceSage)を活用しており、リリースノートやREADME、コミットメッセージの9割は[SourceSage](https://github.com/Sunwood-ai-labs/SourceSage) ＋ [claude.ai](https://claude.ai/)で生成しています。

## 🌟 [Zoltraak](https://twitter.com/ai_syacho/status/1782926797790941615)とは

[Zoltraak（ゾルトラーク）](https://twitter.com/ai_syacho/status/1782926797790941615) は、自然言語（日本語）で様々なタスクを依頼することができる、革新的なプログラミングツールです。
システム開発、ホームページ制作、デザイン、分析など、短い文章で依頼するだけで必要な資料やソースコードを生成してくれます。

従来の対話型AIとは一線を画し、シンプルかつパワフルな問題解決を実現。
プログラミングの知識がなくても、アイデアを具現化できる魔法のようなツールです。

このリポジトリでは、DockerでかんたんにZoltraakを利用する環境を提供しています。


## 📚 更新情報

### 🎉 [v1.0.0](https://github.com/Sunwood-ai-labs/zoltraak_docker/releases/tag/v1.0.0) - 2024-04-28

- Dockerを使ったZoltraakの簡単な利用環境の提供
- `.env`ファイルでのANTHROPIC APIキーの設定
- `README.md`へのZoltraakの詳細説明の追加

## 🚀 はじめに

### 事前準備

- Docker、docker-composeのインストール 
- [ANTHROPIC](https://www.anthropic.com/) でAPIキーを取得し、 `.env` ファイルに設定

`.env` ファイルにANTHROPICとGeminiのAPIキーを設定:

```
ANTHROPIC_API_KEY=sk-ant-XXXXXXXXXXX
GEMINI_API_KEY=XXXXXXXXXXX
```

### 起動方法

```bash
# イメージのビルドとコンテナ起動
docker-compose up --build

# コンテナ内でbashを起動  
docker-compose exec app /bin/bash

# Zoltraakを実行
zoltraak "mp4からgifを作成するstremlitのアプリを作成したい" -c dev_obj
```

## 🙌 コントリビューション

IssueやPull Requestは大歓迎です。改善案や機能追加のアイデアがありましたらぜひお寄せください。

## 📄 ライセンス

Zoltraak DockerはMITライセンスの下で公開されています。

## 🙏 謝辞

Zoltraakを開発している [元木大介さん（@ai\_syacho）](https://twitter.com/ai_syacho) に深く感謝いたします。
