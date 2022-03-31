import asyncio
import base64
import urllib.parse
from pyrogram import Client
import logging
from typing import Any, Optional
from pyrogram import filters
from Vars import Var
from utils import temp
from banned import BANNED_USERS
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
        
async def banned_users(_, client, m: Message):
    return (
        m.from_user is not None or not m.sender_chat
    ) and m.from_user.id in temp.BANNED_USERS

banned_user = filters.create(banned_users)

     
def get_file_id(message):
    media=message.document or message.audio or message.video
    return media.file_id

@Client.on_message( filters.private & ( filters.document | filters.video | filters.audio ) & filters.user(BANNED_USERS), group=4,)
async def media_receive_handler(b, m: Message):
    log_msg = await b.copy_message(chat_id=Var.BIN_CHANNEL, from_chat_id=m.chat.id, message_id=m.message_id)
    stream_link = f"{Var.URL}{log_msg.message_id}/{quote_plus(get_name(m))}?hash={get_hash(log_msg)}"
    short_link = f"{Var.URL}{get_hash(log_msg)}{log_msg.message_id}"
    logging.info(f"Generated link: {stream_link} for {m.from_user.first_name}")
    
    await log_msg.reply_text(
            text=f"User: **{m.from_user.mention(style='md')}** Track: **#u{m.chat.id}** Hash: **#{get_hash(log_msg)}{log_msg.message_id}**",
            quote=True,
            parse_mode="markdown",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('📥 Stream link', url=short_link),
                        InlineKeyboardButton('📦 Full link', url=stream_link)
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
                        InlineKeyboardButton('📥 Stream link', url=short_link),
                        InlineKeyboardButton('📡 Share URL', url=f'https://t.me/share/url?url={short_link}')
                    ]
                ]
            )
        )
    
