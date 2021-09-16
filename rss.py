import os
import sys
import feedparser
from sql import db
from time import sleep, time
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from apscheduler.schedulers.background import BackgroundScheduler


try:
    api_id = int(os.environ["API_ID"])   # Get it from my.telegram.org
    api_hash = os.environ["API_HASH"]   # Get it from my.telegram.org
    feed_urls = list(set(i for i in os.environ["FEED_URLS"].split("|")))  # RSS Feed URL of the site.
    bot_token = os.environ["BOT_TOKEN"]   # Get it by creating a bot on https://t.me/botfather
    log_channel = int(os.environ["LOG_CHANNEL"])   # Telegram Channel ID where the bot is added and have write permission. You can use group ID too.
    check_interval = int(os.environ.get("INTERVAL", 10))   # Check Interval in seconds.  
    max_instances = int(os.environ.get("MAX_INSTANCES", 3))   # Max parallel instance to be used.
    str_session = os.environ.get("STR_SESSION")    #String session generate using your tg mobile number for sending mirror cmd on your behalf. Generate using python gen_str.py
    mirr_chat = int(os.environ.get("MIRROR_CHAT_ID"))    #Group/chat_id of mirror chat or mirror bot to send mirror cmd
    mirr_cmd = os.environ.get("MIRROR_CMD", "/mirror")    #if you have changed default cmd of mirror bot, replace this.
except Exception as e:
    print(e)
    print("One or more variables missing or have error. Exiting !")
    sys.exit(1)


for feed_url in feed_urls:
    if db.get_link(feed_url) == None:
        db.update_link(feed_url, "*")


app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)
app2 = None
if str_session is not None and str_session != "":
    app2 = Client(str_session, api_id=api_id, api_hash=api_hash)

def create_feed_checker(feed_url):
    def check_feed():
        FEED = feedparser.parse(feed_url)
        entry = FEED.entries[0]
        if entry.id != db.get_link(feed_url).link:
                       # ↓ Edit this message as your needs.
            message = f"**{entry.title}**\n```{entry.link}```"
            try:
                app.send_message(log_channel, message)
                if app2 is not None:
                    mirr_msg = f"{mirr_cmd} {entry.link}"
                    app2.send_message(mirr_chat, mirr_msg)
                db.update_link(feed_url, entry.id)
            except FloodWait as e:
                print(f"FloodWait: {e.x} seconds")
                sleep(e.x)
            except Exception as e:
                print(e)
        else:
            print(f"Checked RSS FEED: {entry.id}")
    return check_feed


scheduler = BackgroundScheduler()
for feed_url in feed_urls:
    feed_checker = create_feed_checker(feed_url)
    scheduler.add_job(feed_checker, "interval", seconds=check_interval, max_instances=max_instances)
scheduler.start()
if app2 is not None:
    app2.start()
app.run()