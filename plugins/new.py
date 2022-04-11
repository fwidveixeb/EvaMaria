import random
import asyncio
from Vars import Var
from info import PICS, ADMINS
from pyrogram import filters, Client
from utils import temp
from pyrogram.file_id import FileId
from urllib.parse import quote_plus
from database.ia_filterdb import unpack_new_file_id
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto

def get_hash(media_msg: Message) -> str:
    media = get_media_from_message(media_msg)
    return getattr(media, "file_unique_id", "")[:6]

def get_name(media_msg: Message) -> str:
    media = get_media_from_message(media_msg)
    return getattr(media, "file_name", "")

class FIleNotFound(Exception):
    message = "File not found"

async def get_file_ids(client: Client, chat_id: int, message_id: int) -> Optional[FileId]:
    message = await client.get_messages(chat_id, message_id)
    if message.empty:
        raise FIleNotFound
    media = get_media_from_message(message)
    file_unique_id = await parse_file_unique_id(message)
    file_id = await parse_file_id(message)
    setattr(file_id, "file_size", getattr(media, "file_size", 0))
    setattr(file_id, "mime_type", getattr(media, "mime_type", ""))
    setattr(file_id, "file_name", getattr(media, "file_name", ""))
    setattr(file_id, "unique_id", file_unique_id)
    return file_id

def get_media_from_message(message: "Message") -> Any:
    media_types = (
        "audio",
        "document",
        "photo",
        "sticker",
        "animation",
        "video",
        "voice",
        "video_note",
    )
    for attr in media_types:
        media = getattr(message, attr, None)
        if media:
            return media
        
def get_file_id(message):
    media=message.document or message.audio or message.video
    return media.file_id

async def banned_users(_, client, message: Message):
    return (
        message.from_user is not None or not message.sender_chat
    ) and message.from_user.id in temp.BANNED_USERS

banned_user = filters.create(banned_users)

YES_PHOTO = ["https://telegra.ph/file/2e8725f268df2e9e693f1.jpg"]

YES_TEXT = """{} \n\nFile has beendeleted successfully."""

DELETE_TEXT = """{} \n\nDo you really want to delete this file?"""

DELETE_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('✅ Yes', callback_data='yes'),
            InlineKeyboardButton('❌ No', callback_data='no'),
        ]]
      )

NO_TEXT = """{}"""

DELETE = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('🗑 Delete File', callback_data='delete')
                    ]
                ]
            )

NO_BUTTON = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('🗑 Delete File', callback_data='delete')
                    ]
                ]
            )

NEW_ABOUT_TEXT = """<b>😊 Use these buttons to know about me. Send /start to reload me.</b>"""

NEW_ABOUT_HOME = """<b>😊 Use these buttons to know about me. Send /start to reload me.</b>"""

RATING_TEXT = """This is rating text."""

SOURCE_TEXT = """This is source text."""

DONATE_TEXT = """This is donate text."""

NEW_HELP_TEXT = """<b>🧩 Here is the help of my commands. Send /about to know about me.</b>"""

NEW_HELP_HOME_TEXT = """<b>🧩 Here is the help of my commands. Send /about to know about me.</b>"""

FILE_STREAM_TEXT = """This is file stream text."""

FILE_STORE_TEXT = """This is file store text."""

INSTRUCTIONS_TEXT = """This is instructions text."""

TUTORIALS_TEXT = """This is tutorials text."""

WARNING_TEXT = """This is warning text."""

FILE_TEXT = """ This file has been deleted due to Pornographic reasons."""

VIDEO_TEXT = """ This file has been deleted due to Copyrighted material."""

AUDIO_TEXT = """ This file has been deleted due to Other reasons."""

FILE = ["https://telegra.ph/file/b2b658b749bb6b976ea8d.jpg"]

VIDEO = ["https://telegra.ph/file/bafed7e9c21f326193963.jpg"]

AUDIO = ["https://telegra.ph/file/a1900232d1715b8b9adbb.jpg"]

NEW_ABOUT_HOME_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⭐️ Rating', callback_data='rating'),
            InlineKeyboardButton('❤️ Source', callback_data='source'),
            ],[
            InlineKeyboardButton('💰 Donate', callback_data='donate')
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

ABOUT_BACK_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🔙 Back', callback_data='new_about_home')
            ]]
        )

HELP_BACK_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🔙 Back', callback_data='new_help_home')
            ]]
        )

DELETE = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('📁', callback_data='file'),
            InlineKeyboardButton('🎥', callback_data='video'),
            InlineKeyboardButton('🎧', callback_data='audio')
        ]])

@Client.on_callback_query()
async def cb_data(bot, update):
    if update.data == "new_about_home":
        await update.answer('www.hagadmansa.com')
        image=random.choice(PICS)
        await update.edit_message_media(
        media=InputMediaPhoto(media=image, caption=NEW_ABOUT_HOME),
        reply_markup=NEW_ABOUT_HOME_BUTTONS
        )
    elif update.data == "rating":
        await update.answer('www.hagadmansa.com')
        image=random.choice(PICS)
        await update.edit_message_media(
        media=InputMediaPhoto(media=image, caption=RATING_TEXT),
        reply_markup=ABOUT_BACK_BUTTONS
        )
    elif update.data == "source":
        await update.answer('www.hagadmansa.com')
        image=random.choice(PICS)
        await update.edit_message_media(
        media=InputMediaPhoto(media=image, caption=SOURCE_TEXT),
        reply_markup=ABOUT_BACK_BUTTONS
        )
    elif update.data == "donate":
        await update.answer('www.hagadmansa.com')
        image=random.choice(PICS)
        await update.edit_message_media(
        media=InputMediaPhoto(media=image, caption=DONATE_TEXT),
        reply_markup=ABOUT_BACK_BUTTONS
        )
    elif update.data == "new_help_home":
        await update.answer('www.hagadmansa.com')
        image=random.choice(PICS)
        await update.edit_message_media(
        media=InputMediaPhoto(media=image, caption=NEW_HELP_HOME_TEXT),
        reply_markup=NEW_HELP_HOME_BUTTONS
        )
    elif update.data == "file_stream":
        await update.answer('www.hagadmansa.com')
        image=random.choice(PICS)
        await update.edit_message_media(
        media=InputMediaPhoto(media=image, caption=FILE_STREAM_TEXT),
        reply_markup=HELP_BACK_BUTTONS
        )
    elif update.data == "file_store":
        await update.answer('www.hagadmansa.com')
        image=random.choice(PICS)
        await update.edit_message_media(
        media=InputMediaPhoto(media=image, caption=FILE_STORE_TEXT),
        reply_markup=HELP_BACK_BUTTONS
        )
    elif update.data == "instructions":
        await update.answer('www.hagadmansa.com')
        image=random.choice(PICS)
        await update.edit_message_media(
        media=InputMediaPhoto(media=image, caption=INSTRUCTIONS_TEXT),
        reply_markup=HELP_BACK_BUTTONS
        )
    elif update.data == "tutorials":
        await update.answer('www.hagadmansa.com')
        image=random.choice(PICS)
        await update.edit_message_media(
        media=InputMediaPhoto(media=image, caption=TUTORIALS_TEXT),
        reply_markup=HELP_BACK_BUTTONS
        )
    elif update.data == "warning":
        await update.answer('www.hagadmansa.com')
        image=random.choice(PICS)
        await update.edit_message_media(
        media=InputMediaPhoto(media=image, caption=WARNING_TEXT),
        reply_markup=HELP_BACK_BUTTONS
        )
    elif update.data == "yes":
        await update.answer('File Deleted Successfully')
        media=random.choice(YES_PHOTO)
        log_msg = await bot.copy_message(chat_id=Var.BIN_CHANNEL, from_chat_id=update.chat.id, message_id=update.message_id)
        newtext=f"User: **{update.from_user.mention(style='md')}** Track: **#u{update.chat.id}** Hash: **#{get_hash(log_msg)}{log_msg.message_id}** Link: **[Hold Me]({short_link})**"
        await update.edit_message_media(
        media=InputMediaPhoto(media=media, caption=YES_TEXT).format(newtext),
        )
    elif update.data == "no":
        await update.answer('Cancel file deleting process.')
        log_msg = await bot.copy_message(chat_id=Var.BIN_CHANNEL, from_chat_id=update.chat.id, message_id=update.message_id)
        newtext=f"User: **{update.from_user.mention(style='md')}** Track: **#u{update.chat.id}** Hash: **#{get_hash(log_msg)}{log_msg.message_id}** Link: **[Hold Me]({short_link})**"
        await update.edit_text(
        text=NO_TEXT.format(newtext),
        reply_markup=NO_BUTTONS,
        )
    elif update.data == "delete":
        await update.answer('Do you really want to delete this file?')
        log_msg = await bot.copy_message(chat_id=Var.BIN_CHANNEL, from_chat_id=update.chat.id, message_id=update.message_id)
        newtext=f"User: **{update.from_user.mention(style='md')}** Track: **#u{update.chat.id}** Hash: **#{get_hash(log_msg)}{log_msg.message_id}** Link: **[Hold Me]({short_link})**"
        await update.edit_text(
        text=DELETE_TEXT.format(newtext),
        reply_markup=DELETE_BUTTONS
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
       
YOUARENOT = ["https://telegra.ph/file/2e8725f268df2e9e693f1.jpg"]

@Client.on_message(filters.command("new")) 
async def new(client, bot):
     if bot.from_user and bot.from_user.id in ADMINS:
        return await bot.reply_photo(
        photo=random.choice(PICS),
        caption="""Hello dear owner, what can i do for you?""",
        )
     if bot.from_user and bot.from_user.id not in ADMINS:
        notforyou = await bot.reply(
        text="""You are not allowed to use this command.""",
        quote=True
        )
        await asyncio.sleep(2)
        await notforyou.delete()
        await bot.delete()
