import asyncio
import urllib.parse
import logging
from pyrogram import filters
from Vars import Var
from urllib.parse import quote_plus
import get_hash, get_name
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(
    filters.private
    & (
        filters.document
        | filters.video
        | filters.audio
        | filters.animation
        | filters.voice
        | filters.video_note
        | filters.photo
        | filters.sticker
    ),
    group=4,
)
async def media_receive_handler(_, m: Message):
    log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
    stream_link = f"https://download.hagadmansa.com/{log_msg.message_id}/{quote_plus(get_name(m))}?hash={get_hash(log_msg)}"
    short_link = f"https://download.hagadmansa.com/{get_hash(log_msg)}{log_msg.message_id}"
    logging.info(f"Generated link: {stream_link} for {m.from_user.first_name}")
    
    await log_msg.reply_text(
            text=f"😎 Hello Himanshu, i generated 2 links for **{m.from_user.mention(style='md')}**. You can view **{m.from_user.mention(style='md')}'s** all generated links with **#u{m.chat.id}**.",
            quote=True,
            parse_mode="markdown",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('📥 Full link', url=stream_link),
                        InlineKeyboardButton('📦 Short link', url=short_link)
                    ]
                ]
            )
    )
    
    await m.reply_text(
        text="""<b>🤓 I generated 2 links for you, but both links work same. Just hold the inline button to copy the link.</b>""",
        quote=True,
        parse_mode="html",
        reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('📥 Full link', url=stream_link),
                        InlineKeyboardButton('📦 Short link', url=short_link)
                    ]
                ]
            )
        )
    
