# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "28243586"))
	API_HASH = os.environ.get("API_HASH", "4022d5686b9b7a7cf8891205921a0ab3")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "7340328039:AAESg2u6VgJ0E-dvIao9gaM1TGenyejolfI")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "LegendFileSaver_Bot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002394249695"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "7871556756"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://madarazbotz:UbI0lIPWOAnwy6no@cluster0.wpbfa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002178219823")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1002366094744")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
<b>𝖳𝗁𝗂𝗌 𝖨𝗌 𝖠 𝖯𝖾𝗋𝗆𝖺𝗇𝖾𝗇𝗍 𝖥𝗂𝗅𝖾 𝖲𝖺𝗏𝖾𝗋 𝖡𝗈𝗍. \n\n➜ 𝖲𝖾𝗇𝖽 𝖬𝖾 𝖠𝗇𝗒 𝖥𝗂𝗅𝖾 𝖳𝗈 𝖦𝖾𝗍 𝖲𝗁𝖺𝗋𝖾𝖺𝖻𝗅𝖾 𝖫𝗂𝗇𝗄. \n➜ 𝖶𝗈𝗋𝗄𝗌 𝖨𝗇 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 𝖳𝗈𝗈. \n➜ 𝖠𝗏𝗈𝗂𝖽 𝖢𝗈𝗉𝗒𝗋𝗂𝗀𝗁𝗍 𝖨𝗇𝖿𝗋𝗂𝗇𝗀𝖾𝗆𝖾𝗇𝗍. \n\n★ 𝗔𝗯𝗼𝘂𝘁 𝗙𝗶𝗹𝗲 𝗦𝗮𝘃𝗲𝗿 \n\n๏ 𝖡𝗈𝗍 𝖭𝖺𝗆𝖾 ➜ <a href='https://t.me/TeamLegendSaver_Bot'>ʟᴇɢᴇɴᴅ ꜱᴀᴠᴇʀ ʙᴏᴛ</a> \n๏ 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾 ➜ <a href='https://www.python.org/'>ᴘʏᴛʜᴏɴ</a> \n๏ 𝖫𝗂𝖻𝗋𝖺𝗋𝗒 ➜ <a href='https://pyrogram.org/'>ᴘʏʀᴏɢʀᴀᴍ</a> \n\n☆ 𝗢𝘄𝗻𝗲𝗿 ~ <a href='https://t.me/Itz_Shixnu'>ɪᴛᴢ ꜱʜɪxɴᴜ</a>🥤 \n☆ 𝗝𝗼𝗶𝗻 ~ <a href='https://t.me/Team_Legend_Official'>ᴛᴇᴀᴍ ʟᴇɢᴇɴᴅ ᴏꜰꜰɪᴄɪᴀʟ</a>🥤</b>
"""
	ABOUT_DEV_TEXT = f"""
<b>𝖳𝗁𝗂𝗌 𝖨𝗌 𝖠 𝖯𝖾𝗋𝗆𝖺𝗇𝖾𝗇𝗍 𝖥𝗂𝗅𝖾 𝖲𝖺𝗏𝖾𝗋 𝖡𝗈𝗍. \n\n➜ 𝖲𝖾𝗇𝖽 𝖬𝖾 𝖠𝗇𝗒 𝖥𝗂𝗅𝖾 𝖳𝗈 𝖦𝖾𝗍 𝖲𝗁𝖺𝗋𝖾𝖺𝖻𝗅𝖾 𝖫𝗂𝗇𝗄. \n➜ 𝖶𝗈𝗋𝗄𝗌 𝖨𝗇 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 𝖳𝗈𝗈. \n➜ 𝖠𝗏𝗈𝗂𝖽 𝖢𝗈𝗉𝗒𝗋𝗂𝗀𝗁𝗍 𝖨𝗇𝖿𝗋𝗂𝗇𝗀𝖾𝗆𝖾𝗇𝗍. \n\n★ 𝗔𝗯𝗼𝘂𝘁 𝗙𝗶𝗹𝗲 𝗦𝗮𝘃𝗲𝗿 \n\n๏ 𝖡𝗈𝗍 𝖭𝖺𝗆𝖾 ➜ <a href='https://t.me/TeamLegendSaver_Bot'>ʟᴇɢᴇɴᴅ ꜱᴀᴠᴇʀ ʙᴏᴛ</a> \n๏ 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾 ➜ <a href='https://www.python.org/'>ᴘʏᴛʜᴏɴ</a> \n๏ 𝖫𝗂𝖻𝗋𝖺𝗋𝗒 ➜ <a href='https://pyrogram.org/'>ᴘʏʀᴏɢʀᴀᴍ</a> \n\n☆ 𝗢𝘄𝗻𝗲𝗿 ~ <a href='https://t.me/Itz_Shixnu'>ɪᴛᴢ ꜱʜɪxɴᴜ</a>🥤 \n☆ 𝗝𝗼𝗶𝗻 ~ <a href='https://t.me/Team_Legend_Official'>ᴛᴇᴀᴍ ʟᴇɢᴇɴᴅ ᴏꜰꜰɪᴄɪᴀʟ</a>🥤</b>"""
	HOME_TEXT = """
<b> 𝗛𝗲𝘆 , [{}](tg://user?id={}) ✨️ \n\n𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝗧𝗼 𝗧𝗲𝗮𝗺 𝗟𝗲𝗴𝗲𝗻𝗱 𝗢𝗳𝗳𝗶𝗰𝗶𝗮𝗹 ❤️⚡️ \n━━━━━━━━━━━ ☆ ━━━━━━━━━━━ \n➥ 𝗣𝗿𝗼𝘃𝗶𝗱𝗲𝘀 𝗙𝗿𝗲𝗲 𝗦𝘁𝘂𝗱𝘆 𝗠𝗮𝘁𝗲𝗿𝗶𝗮𝗹𝘀 📚 \n𝗙𝗼𝗿 𝗡𝗘𝗘𝗧 , 𝗝𝗘𝗘 , 𝗕𝗢𝗔𝗥𝗗𝗦 & 𝗖𝗨𝗘𝗧 🔥 \n━━━━━━━━━━━ ☆ ━━━━━━━━━━━ \n➥ 𝗜𝗙 𝗨 𝗟𝗶𝗸𝗲 𝗧𝗵𝗶𝘀 𝗕𝗼𝘁 , 𝗠𝘂𝘀𝘁 𝗦𝗵𝗮𝗿𝗲 𝗧𝗵𝗶𝘀 𝗕𝗼𝘁 👀❤️ #𝗧𝗘𝗔𝗠_𝗟𝗘𝗚𝗘𝗡𝗗_𝗢𝗙𝗙𝗜𝗖𝗜𝗔𝗟 ⚜️ \n━━━━━━━━━━━ ☆ ━━━━━━━━━━━ \n➥ 𝗠𝗮𝗱𝗲 𝗕𝘆 ➤ @Itz_Shixnu 🥤 \n➥ 𝗠𝘂𝘀𝘁 𝗝𝗼𝗶𝗻 ➤ @TeamLegend_Backup ✨️ \n ━━━━━━━━━━━ ☆ ━━━━━━━━━━━</b>

"""
