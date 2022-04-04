from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

If you don't trust this bot, 
1) stop reading this message
2) delete this chat

Still reading?
You can use me to generate pyrogram and telethon string session. Use below buttons to learn more !

By @StarkBots
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton ("🔥 بدء إنشاء الجلسة 🔥" ، callback_data = "إنشاء")], 
        [InlineKeyboardButton(text="🏠 رجـــوع 🏠", callback_data="الصفحة الرئيسية")]
    ]

    generate_button = [
        [InlineKeyboardButton("🔥 ابدأ بتوليد الجلسة 🔥", callback_data="انشاء")]
    ]

    # أزرار الراحة
    أزرار  = [
        [InlineKeyboardButton("🔥 ابدأ بتوليد الجلسة 🔥", callback_data="انشاء")],
        [InlineKeyboardButton("✨ حالة البوت والمزيد من الروبوتات ✨", url="https://t.me/MR_X_N_3")],
        [
            InlineKeyboardButton("كيف تستعمل ❔", callback_data="مساعدة"),
            InlineKeyboardButton("🎪 حول 🎪", callback_data="حول")
        ],
        [InlineKeyboardButton("♥ المزيد من الروبوتات المذهلة ♥", url="https://t.me/MR_X_N_3")],
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Start Generating Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    # About Message
    ABOUT = """
**About This Bot** 

A telegram bot to generate pyrogram and telethon string session by @StarkBots

Source Code : [Click Here](https://github.com/StarkBotsIndustries/StringSessionBot)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @StarkProgrammer
    """
