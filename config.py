from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
from pyro import validate_session

APP_ID = os.environ.get("APP_ID")
APP_HASH = os.environ.get("APP_HASH")

ss = os.environ.get("1BJWap1sBuxObMZXde7S4nLQ8s1NfrBKMVyDEUVlVVgK3U7y7Y6nmWBVub9IIVufXH1zqAYDE9YW9pYcVr3OTq9tHVoKkLWLD9Ay6NHTRzHuDxcgixCOxtqri5Wfm97o0DODBmHZA3VIaLCQzWKOgq8mt1Bi_8hbc4DJ-FQBO5FiSbNw2hfXuO8506YC0mnBJoK4w7wQcws3_XUa3bEGhwEm52pauS59RBCIBpEpz7VkiCXScyFw73cvauNFF5JLinPhqsvNnW0yFfpxGIMcnnrZshp1K-zXtag_vP_0uiIq-Yxs02QWx12qqqUutE4pu-MdM7AGuzKhIodrWX14vU8ybbrskpik=")
session = validate_session(ss)
IEX = TelegramClient(StringSession(session), APP_ID, APP_HASH)

ispay = ['yes']

# BOT_USERNAME = os.environ.get("BOT_USERNAME")
# token = os.environ.get("TOKEN")
# bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
# bot.start()
