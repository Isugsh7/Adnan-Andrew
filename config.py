from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from pyro import validate_session

# ضع القيم الخاصة بك هنا مباشرة
APP_ID = 20621590  
# ضع هنا الـ APP_ID الخاص بك كرقم صحيح
APP_HASH = "a7e91275d681fefd4b2453b158b254ec"  
# ضع هنا الـ APP_HASH كسلسلة نصية
ss = "1BJWap1sAUF8B-YYYtte-w_gCT7Ucb4SsqWC--N4wzwERLhYqByU1LPArKt54Mng2IFc-l7Gy1stQonO9RgAns9ZV4-pfjfWkNRA94iQi8dilnRhSz-_18vXFdbkGOx0SkFp6Uvexv6Cm4d2fcu3_UpzRynPLfQZJuCXz1GhbbydEWse8BFXWuL56OGCdNVoR78gG8TiJ1vYgekfRtP-MdjllylT2LDkGu_pYoYnS0qXeAogFzhlkdl-OQtBenR2yYnQ4zX8CVD_5QPh_bD4Q7iReOcyx0xIbbM_HaK-0Pd_C385e-rcLfjj_wlS4ZWLrfAnO5kwEm5fiZsg9ViC-zm9W_1gf36k="
  # ضع هنا الـ String Session كنص

# التحقق من صحة الجلسة
session = validate_session(ss)

# إنشاء العميل
IEX = TelegramClient(StringSession(session), APP_ID, APP_HASH)

ispay = ['yes']

# إذا كنت تستخدم بوت، يمكنك تفعيل الأسطر التالية:
# BOT_USERNAME = "your_bot_username"
# token = "your_bot_token"
# bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
# bot.start()
