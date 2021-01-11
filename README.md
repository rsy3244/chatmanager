### Discordチャットマネージャー

Discordでのチャットを管理するBOTです。

- 指定したチャンネルのメッセージを一定時間後に自動で削除します。
- 絵文字のみが投稿された場合に、その拡大画像を送信します。

## 起動方法

事前にBOTトークンを取得してください。

環境変数として以下を設定。

- DISCORD\_BOT\_TOKEN	BOTのトークン
- DISCORD\_BOT\_GUILD\_ID	BOTを利用するサーバーのID
- DISCORD\_BOT\_CHANNEL\_ID	メッセージを管理したいチャンネルID

discord.pyをインストール
```bash
$ python3 -m pip install -U "discord.py"
```

BOTを起動
```bash
$ python3 chatmanager.py
```
