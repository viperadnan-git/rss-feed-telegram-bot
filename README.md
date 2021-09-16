# RSS Feed Telegram Bot
A bot to post messages to Telegram Groups or Channels from rss feed.
- This bot can also send /mirror commands to your mirror bot using your telegram account.
bcoz bot can't read another bot's mag. So this bot will use your TG account to interact with mirror bot.
Fill `STR_SESSION` and `MIRROR_CHAT_ID` vars to enable it.

## Configuration
- Edit the [rss.py](./rss.py) as your needs.
- Edit values in [config.env](./config.env.template) or set it in Environment Variables. There is an template for `config.env` already exists just edit it and rename the file.

### Configuration Values
- `APP_ID` - Get it from [my.telegram.org](https://my.telegram.org/apps)
- `API_HASH` - Get it from [my.telegram.org](https://my.telegram.org/apps)
- `BOT_TOKEN` - Get it by creating a Telegram bot on [BotFather](https://t.me/BotFather)
- `FEED_URLS` - List of URLs of RSS Feed, sperated by `|` vertical bar.
- `LOG_CHAT` - ID of the Telegram Chat where messages are to be posted.
- `DATABASE_URL` - Here is a full [guide](https://github.com/SpEcHiDe/NoPMsBot/wiki/How-to-Install-Database-%3F). For Heroku, just add the `Heroku Postgres` add-on.
- `INTERVAL` - Checking Interval in seconds. (optional)
- `MAX_INSTANCES` - Max instances to be used while checking rss feed. (optional)
### Working as a userbot on your behalf to interact with mirror bot.

These variabls are required only if you want to use your tg account to send /mirror cmd to any mirror bot.
- `MIRROR_CHAT_ID` - Group/chat_id of mirror chat or mirror bot to send mirror cmd.
- `MIRROR_CMD` - if you have changed default cmd of mirror bot, replace this.
- `STR_SESSION` - String session generate using your tg mobile number for sending mirror cmd on your behalf. Generate by running
```
python gen_str.py 
```
(heroku users run in heroku console)

## Deployment

### Deploying on Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

### VPS or any other server/pc

- Install requirements from [requirements.txt](./requirements.txt)
```
pip3 install -r requirements.txt
```
- Deploy
```
python3 rss.py
```

## Copyright & License
- Copyright (©) 2021 by [Adnan Ahmad](https://github.com/viperadnan-git)
- Licensed under the terms of the [GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007](./LICENSE)