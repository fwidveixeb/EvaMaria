import asyncio
import base64
import urllib.parse
from pyrogram import Client
import logging
from typing import Any, Optional
from pyrogram import filters
from Vars import Var
from utils import temp
from pyrogram.file_id import FileId
from urllib.parse import quote_plus
from database.ia_filterdb import unpack_new_file_id
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

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

FILE = ["https://telegra.ph/file/b2b658b749bb6b976ea8d.jpg"]

VIDEO = ["https://telegra.ph/file/bafed7e9c21f326193963.jpg"]

AUDIO = ["https://telegra.ph/file/a1900232d1715b8b9adbb.jpg"]

FILE_TEXT = """ This file has been deleted due to Pornographic reasons."""

VIDEO_TEXT = """ This file has been deleted due to Copyrighted material."""

AUDIO_TEXT = """ This file has been deleted due to Other reasons."""

DELETE = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('📁', callback_data='file'),
            InlineKeyboardButton('🎥', callback_data='video'),
            InlineKeyboardButton('🎧', callback_data='audio')
        ]])

@Client.on_callback_query()
async def cb_data(bot, update):
    if update.data == "file":
        await update.answer('File Deleted Successfully')
        file=random.choice(FILE)
        await update.reply_to_message.edit_message_media(
        media=InputMediaPhoto(media=file, caption=FILE_TEXT),
        )
    elif update.data == "video":
        await update.answer('File Deleted Successfully')
        video=random.choice(VIDEO)
        await update.reply_to_message.edit_message_media(
        media=InputMediaPhoto(media=video, caption=MOVIE_TEXT),
        )
    elif update.data == "audio":
        await update.answer('File Deleted Successfully')
        audio=random.choice(AUDIO)
        await update.reply_to_message.edit_message_media(
        media=InputMediaPhoto(media=audio, caption=OTHER_TEXT),
        )
    elif update.data == "delete":
        await update.answer('Choose a option to delete')
        await update.message.edit(
        text="""hello choose any option to delete the file"""
        reply_markup=DELETE
        )
        
@Client.on_message( filters.private & ( filters.document | filters.video | filters.audio ) & ~banned_user, group=4,)
async def media_receive_handler(b, m: Message):
    
    banned_user = filters.create(banned_users)
    log_msg = await b.copy_message(chat_id=Var.BIN_CHANNEL, from_chat_id=m.chat.id, message_id=m.message_id)
    stream_link = f"{Var.URL}{log_msg.message_id}/{quote_plus(get_name(m))}?hash={get_hash(log_msg)}"
    short_link = f"{Var.URL}{get_hash(log_msg)}{log_msg.message_id}"
    logging.info(f"Generated link: {stream_link} for {m.from_user.first_name}")
    
    await log_msg.reply_text(
            text=f"User: **{m.from_user.mention(style='md')}** Track: **#u{m.chat.id}** Hash: **#{get_hash(log_msg)}{log_msg.message_id}** Link: **[Hold Me]({short_link})**",
            quote=True,
            parse_mode="markdown",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('🔞', callback_data='delete'),
                        InlineKeyboardButton('©', callback_data='delete'),
                        InlineKeyboardButton('💭', callback_data='delete')
                    ]
                ]
            )
    )
    
    await m.reply_text(
        text="""<b>🤓 I generated link for you, just reply the file with /link to generate an extra link.</b>""",
        quote=True,
        parse_mode="html",
        reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('📥 Stream Link', url=f'https://t.me/share/url?url={short_link}')
                    ]
                ]
            )
        )

TEST = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('📁', callback_data='file'),
            InlineKeyboardButton('🎥', callback_data='video'),
            InlineKeyboardButton('🎧', callback_data='audio')
        ]])
    
@Client.on_message(filters.command("test")) 
async def test(client, bot):
     await bot.reply(
        text="""Hello dear owner, what can i do for you?""",
        reply_markup=TEST
        )
