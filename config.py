from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
from pyro import validate_session

APP_ID = os.environ.get("27455984'")
APP_HASH = os.environ.get("62d5f68ce2e9189636967120220f5755")

ss = os.environ.get("1BJWap1sBuxiqyFHXxseDPNvJSO9iRmhOpBwniSTZaoZwoQaCZ_mW_Msbbczk3RORSOLV_qzDbehtCZG6c-Piu-GDJbsRn_vEa73csJUt7CmL_xohj_9Dvg4LPd2ETtzx7cynSV0mGbLIIL-T--v4HK4MXyyxCUvzWxJz7gcVffnJUCZGthtok0PRVFD7eEs_7u_MXUt1Og6dpgzQKWHHM2kqXXhqfQqqIxffvV5sbTyYkVxd9EtgGvFVBH3fqTtXx65g1H_vLGOD5P99Gjg80YXpRyGfP__vVisyxTU7aQ49Ql8zN9uOQlJxdc04yMd1419YBk2uA2UMaSC35YhvD1Zr5smKiAk=")
session = validate_session(ss)
IEX = TelegramClient(StringSession(session), APP_ID, APP_HASH)

ispay = ['yes']

# BOT_USERNAME = os.environ.get("BOT_USERNAME")
# token = os.environ.get("TOKEN")
# bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
# bot.start()