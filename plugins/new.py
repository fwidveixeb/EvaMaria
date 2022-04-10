import random
from info import PICS, ADMINS
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

NEW_ABOUT_TEXT = """😊 Use these buttons to know about me. Send /start to reload me.</b>"""

NEW_ABOUT_HOME = """😊 Use these buttons to know about me. Send /start to reload me.</b>"""

RATING_TEXT = """This is rating text."""

SOURCE_TEXT = """This is source text."""

DONATE_TEXT = """This is donate text."""

NEW_HELP_TEXT = """<b>🧩 Here is the help of my commands. Send /about to know about me.</b>"""

NEW_HELP_HOME_TEXT = """<b>🧩 Here is the help of my commands. Send /about to know about me.</b>"""

FILE_STREAM_TEXT = """This is file stream text."""

FILE_STORE_TEXT = """This is file store text."""

INSTRUCTONS_TEXT = """This is instructions text."""

TUTORIALS_TEXT = """This is tutorials text."""

WARNING_TEXT = """This is warning text."""

NEW_ABOUT_HOME_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⭐️ Rating', callback_data='rating'),
            InlineKeyboardButton('❤️ Source', callback_data='source'),
            ],[
            InlineKeyboardButton('💰 Donate', callback_data='donate')
            ]]
       )     
RATING_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🔙 Back', callback_data='new_about_home')
            ]]
        )
SOURCE_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🔙 Back', callback_data='new_about_home')
            ]]
        )
DONATE_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🔙 Back', callback_data='new_about_home')
            ]]
        )
NEW_HELP_HOME_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('📥 File Stream', callback_data='file_stream'),
            InlineKeyboardButton('📦 File Store', callback_data='file_store'),
            ],[
            InlineKeyboardButton('⚙️ Instructions', callback_data='instructions'),
            InlineKeyboardButton('🕹 Tutorials', callback_data='tutorials'),
            ],[
            InlineKeyboardButton('⚠️ Warning', callback_data='warning')
            ]]
         )

FILE_STREAM_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🔙 Back', callback_data='new_help_home')
            ]]
        )

FILE_STORE_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🔙 Back', callback_data='new_help_home')
            ]]
        )

INSTRUCTIONS_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🔙 Back', callback_data='new_help_home')
            ]]
        )

TUTORIALS_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🔙 Back', callback_data='new_help_home')
            ]]
        )

WARNING_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🔙 Back', callback_data='new_help_home')
            ]]
        )

@Client.on_callback_query()
async def cb_data(bot, update):
    if update.data == "new_about_home":
        await update.answer('www.hagadmansa.com')
        await update.message.edit_text(
            text=NEW_ABOUT_HOME,
            disable_web_page_preview=True,
            reply_markup=NEW_ABOUT_HOME_BUTTONS
        )
    elif update.data == "rating":
        await update.answer('www.hagadmansa.com')
        await update.message.edit_text(
            text=RATING_TEXT,
            disable_web_page_preview=True,
            reply_markup=RATING_BUTTONS
        )
    elif update.data == "source":
        await update.answer('www.hagadmansa.com')
        await update.message.edit_text(
            text=SOURCE_TEXT,
            disable_web_page_preview=True,
            reply_markup=SOURCE_BUTTONS
        )
    elif update.data == "donate":
        await update.answer('www.hagadmansa.com')
        await update.message.edit_text(
            text=DONATE_TEXT,
            disable_web_page_preview=True,
            reply_markup=DONATE_BUTTONS
        )
    elif update.data == "new_help_home":
        await update.answer('www.hagadmansa.com')
        await update.message.edit_text(
            text=NEW_HELP_HOME_TEXT,
            disable_web_page_preview=True,
            reply_markup=NEW_HELP_HOME_BUTTONS
        )
    elif update.data == "file_stream":
        await update.answer('www.hagadmansa.com')
        await update.message.edit_text(
            text=FILE_STREAM_TEXT,
            disable_web_page_preview=True,
            reply_markup=FILE_STREAM_BUTTONS
        )
    elif update.data == "file_store":
        await update.answer('www.hagadmansa.com')
        await update.message.edit_text(
            text=FILE_STORE_TEXT,
            disable_web_page_preview=True,
            reply_markup=FILE_STORE_BUTTONS
        )
    elif update.data == "instructions":
        await update.answer('www.hagadmansa.com')
        await update.message.edit_text(
            text=INSTRUCTONS_TEXT,
            disable_web_page_preview=True,
            reply_markup=INSTRUCTIONS_BUTTONS
        )
    elif update.data == "tutorials":
        await update.answer('www.hagadmansa.com')
        await update.message.edit_text(
            text=TUTORIALS_TEXT,
            disable_web_page_preview=True,
            reply_markup=TUTORIALS_BUTTONS
        )
    elif update.data == "warning":
        await update.answer('www.hagadmansa.com')
        await update.message.edit_text(
            text=WARNING_TEXT,
            disable_web_page_preview=True,
            reply_markup=WARNING_BUTTONS
        )
    elif update.data == "close":
        await update.answer('www.hagadmansa.com')
        await update.message.delete()
        try:
            await update.message.reply_to_message.delete()
        except:
            pass
     
@Client.on_message(filters.command("about"))
async def about(client, message):
        await message.reply_photo(
        photo=random.choice(PICS),
        caption=(NEW_ABOUT_TEXT),
        reply_markup=InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⭐️ Rating', callback_data='rating'),
            InlineKeyboardButton('❤️ Source', callback_data='source'),
            ],[
            InlineKeyboardButton('💰 Donate', callback_data='donate')
        ]]))

@Client.on_message(filters.command("help")) 
async def help(client, message):
        await message.reply_photo(
        photo=random.choice(PICS),
        caption=(NEW_HELP_TEXT),
        reply_markup=InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('📥 File Stream', callback_data='file_stream'),
            InlineKeyboardButton('📦 File Store', callback_data='file_store'),
            ],[
            InlineKeyboardButton('⚙️ Instructions', callback_data='instructions'),
            InlineKeyboardButton('🕹 Tutorials', callback_data='tutorials'),
            ],[
            InlineKeyboardButton('⚠️ Warning', callback_data='warning')
         ]]))
        
PHOTO = ["https://telegra.ph/file/ae051812efba8ab8bc0b7.jpg", "https://telegra.ph/file/50acc5072a85341b6ff52.jpg", "https://telegra.ph/file/f542659be3afe195f8a99.jpg", "https://telegra.ph/file/e66bd93f473b99f4b5d14.jpg", "https://telegra.ph/file/785038a666e6139d16756.jpg"]

@Client.on_message(filters.command("docs") & filters.user(ADMINS)) 
async def docs(client, message):
        
        new_message = await message.reply(
        text="""😊 Thanks for activating me, बिना किसी देरी के चलिए शुरू करते हैं.""",
        )
        await new_message.edit(
        text="""😊 Thanks for activating me, बिना किसी देरी के चलिए शुरू करते हैं..""",
        )
        await new_message.edit(
        text="""😊 Thanks for activating me, बिना किसी देरी के चलिए शुरू करते हैं....""",
        )
        await new_message.edit(
        text="""😊 Thanks for activating me, बिना किसी देरी के चलिए शुरू करते हैं....""",
        )
        await new_message.edit(
        text="""😊 Thanks for activating me, बिना किसी देरी के चलिए शुरू करते हैं.....""",
        )
        await new_message.edit(
        text="""🔄 Rebooting Engine.""",
        )
        await new_message.edit(
        text="""🔄 Rebooting Engine..""",
        )
        await new_message.edit(
        text="""🔄 Rebooting Engine...""",
        )
        await new_message.edit(
        text="""🔄 Rebooting Engine....""",
        )
        await new_message.edit(
        text="""🔄 Rebooting Engine.....""",
        )
        await new_message.edit(
        text="""🔝 Starting Engine again""",
        )
        await new_message.edit(
        text="""🔝 Starting Engine again, This may take some time.""",
        )
        await new_message.edit(
        text="""🔝 Starting Engine again, This may take some time.""",
        )
        await new_message.edit(
        text="""🔝 Starting Engine again, This may take some time.""",
        )
        await new_message.edit(
        text="""🔝 Starting Engine again, This may take some time.""",
        )
        await new_message.edit(
        text="""🔝 Starting Engine again, This may take some time.""",
        )
        await new_message.edit(
        text="""➕ Calculating steps to be taken.""",
        )
        await new_message.edit(
        text="""➕ Calculating steps to be taken..""",
        )
        await new_message.edit(
        text="""➕ Calculating steps to be taken...""",
        )
        await new_message.edit(
        text="""➕ Calculating steps to be taken....""",
        )
        await new_message.edit(
        text="""➕ Calculating steps to be taken.....""",
        )
        await new_message.edit(
        text="""➕ Calculating steps to be taken......""",
        )
        await new_message.edit(
        text="""➕ Calculating steps to be taken.
        
        ⏳ Read Source Code""",
        )
        await new_message.edit(
        text="""➕ Calculating steps to be taken.
        
        ⏳ Read Source Code""",
        )
        await new_message.edit(
        text="""➕ Calculating steps to be taken.
        
        ⏳ Read Source Code
        ⏳ Check Database Size""",
        )
        await new_message.edit(
        text="""➕ Calculating steps to be taken.
        
        ⏳ Read Source Code
        ⏳ Check Database Size""",
        )
        await new_message.edit(
        text="""➕ Calculating steps to be taken.
        
        ⏳ Read Source Code
        ⏳ Check Database Size""",
        )
        await new_message.edit(
        text="""➕ Calculating steps to be taken.
        
        ⏳ Read Source Code
        ⏳ Check Database Size
        ⏳ Remove Unnecessary Codes""",
        )
        await new_message.edit(
        text="""➕ Calculating steps to be taken.
        
        ⏳ Read Source Code
        ⏳ Check Database Size
        ⏳ Remove Unnecessary Codes""",
        )
        await new_message.edit(
        text="""➕ Calculating steps to be taken.
        
        ⏳ Read Source Code
        ⏳ Check Database Size
        ⏳ Remove Unnecessary Codes""",
        )
        await new_message.edit(
        text="""➕ Calculating steps to be taken.
        
        ⏳ Read Source Code
        ⏳ Check Database Size
        ⏳ Remove Unnecessary Codes
        ⏳ Reduce Database Size""",
        )
        await new_message.edit(
        text="""➕ Calculating steps to be taken.
        
        ⏳ Read Source Code
        ⏳ Check Database Size
        ⏳ Remove Unnecessary Codes
        ⏳ Reduce Database Size""",
        )
        await new_message.edit(
        text="""➕ Calculating steps to be taken.
        
        ⏳ Read Source Code
        ⏳ Check Database Size
        ⏳ Remove Unnecessary Codes
        ⏳ Reduce Database Size""",
        )
        await new_message.edit(
        text="""➕ Calculating steps to be taken.
        
        ⏳ Read Source Code
        ⏳ Check Database Size
        ⏳ Remove Unnecessary Codes
        ⏳ Reduce Database Size
        ⏳ Get Dynos Information""",
        )
        await new_message.edit(
        text="""➕ Calculating steps to be taken.
        
        ⏳ Read Source Code
        ⏳ Check Database Size
        ⏳ Remove Unnecessary Codes
        ⏳ Reduce Database Size
        ⏳ Get Dynos Information""",
        )
        await new_message.edit(
        text="""➕ Calculating steps to be taken.
        
        ⏳ Read Source Code
        ⏳ Check Database Size
        ⏳ Remove Unnecessary Codes
        ⏳ Reduce Database Size
        ⏳ Get Dynos Information""",
        )
        await new_message.edit(
        text="""➕ Calculating steps to be taken.
        
        ⏳ Read Source Code
        ⏳ Check Database Size
        ⏳ Remove Unnecessary Codes
        ⏳ Reduce Database Size
        ⏳ Get Dynos Information""",
        )
        await new_message.edit(
        text="""🕛 Loading..""",
        )
        await new_message.edit(
        text="""🕧 Loading..""",
        )
        await new_message.edit(
        text="""🕐 Loading...""",
        )
        await new_message.edit(
        text="""🕜 Loading.""",
        )
        await new_message.edit(
        text="""🕑 Loading..""",
        )
        await new_message.edit(
        text="""🕝 Loading...""",
        )
        await new_message.edit(
        text="""🕒 Loading.""",
        )
        await new_message.edit(
        text="""🕞 Loading..""",
        )
        await new_message.edit(
        text="""🕓 Loading...""",
        )
        await new_message.edit(
        text="""🕟 Loading.""",
        )
        await new_message.edit(
        text="""🕔 Loading..""",
        )
        await new_message.edit(
        text="""🕠 Loading...""",
        )
        await new_message.edit(
        text="""🕕 Loading.""",
        )
        await new_message.edit(
        text="""🕡 Loading..""",
        )
        await new_message.edit(
        text="""🕖 Loading...""",
        )
        await new_message.edit(
        text="""🕢 Loading.""",
        )
        await new_message.edit(
        text="""🕗 Loading..""",
        )
        await new_message.edit(
        text="""🕣 Loading...""",
        )
        await new_message.edit(
        text="""🕘 Loading.""",
        )
        await new_message.edit(
        text="""🕤 Loading..""",
        )
        await new_message.edit(
        text="""🕙 Loading...""",
        )
        await new_message.edit(
        text="""🕥 Loading.""",
        )
        await new_message.edit(
        text="""🕚 Loading..""",
        )
        await new_message.edit(
        text="""🕥 Loading...""",
        )
        await new_message.edit(
        text="""🕛 Loading.""",
        )
        await new_message.edit(
        text="""✅ Error Fixed.""",
        )
