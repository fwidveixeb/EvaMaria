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
        
        new_message = await message.reply_photo(
        photo=random.choice(PHOTO),
        caption="""⏱ Please wait 100 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 99 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 98 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 97 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 96 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 95 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 94 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 93 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 92 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 91 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 90 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 89 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 88 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 87 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 86 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 85 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 84 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 83 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 82 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 81 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 80 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 79 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 78 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 77 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 76 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 75 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 74 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 73 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 72 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 71 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 70 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 69 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 68 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 67 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 66 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 65 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 64 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 63 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 62 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 61 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 60 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 59 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 58 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 57 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 56 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 55 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 54 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 53 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 52 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 51 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 50 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 49 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 48 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 47 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 46 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 45 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 44 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 43 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 42 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 41 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 40 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 39 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 38 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 37 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 36 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 35 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 34 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 33 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 32 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 31 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 30 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 29 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 28 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 27 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 26 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 25 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 24 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 23 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 22 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 21 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 20 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 19 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 18 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 17 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 16 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 15 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 14 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 13 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 12 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 11 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 10 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 09 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 08 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 07 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 06 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 05 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 04 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 03 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 02 seconds.""",
        )
        await new_message.edit(
        text="""⏱ Please wait 01 seconds.""",
        )
        await new_message.edit(
        text=(NEW_HELP_TEXT),
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
