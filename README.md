# RSS Feed Telegram Bot
A bot to post messages to Telegram Groups or Channels from rss feed.

### Configuration
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

### Deployment
- Install requirements from [requirements.txt](./requirements.txt)
```
pip3 install requirements.txt
```
- Deploy
```
python3 rss.py
```

## Copyright & License
- Copyright (©) 2021 by [Adnan Ahmad](https://github.com/viperadnan-git)
- Licensed under the terms of the [GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007](./LICENSE)