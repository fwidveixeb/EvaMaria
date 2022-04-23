import os
import logging
import random
import asyncio
from Vars import Var, get_size
from pyrogram import Client, filters
from pyrogram.errors import ChatAdminRequired, FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.ia_filterdb import Media, get_file_details, unpack_new_file_id
from database.users_chats_db import db
from info import CHANNELS, ADMINS, AUTH_CHANNEL, LOG_CHANNEL, PICS, BATCH_FILE_CAPTION, CUSTOM_FILE_CAPTION, PROTECT_CONTENT
from database.connections_mdb import active_connection
import re
import json
import base64
logger = logging.getLogger(__name__)

BATCH_FILES = {}

@Client.on_message(filters.command("start") & filters.incoming & ~filters.edited)
async def start(bot, message):
    if len(message.command) != 2:
        buttons = [[
            InlineKeyboardButton('🌐 Website', url='https://hagadmansa.com'),
            InlineKeyboardButton('📣 Updates', url='https://t.me/hagadmansa')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo=random.choice(PICS),
            caption=("""Hello Dear I Am A Auto Forward Bot."""),
            reply_markup=reply_markup,
            parse_mode='html'
        )
        return
    
    if message.command[1] != "hello":
        await client.send_message(
            chat_id=message.from_user.id,
            text="**This is message command 1.**",
            )
        return
    
    if len(message.command) == 2 and message.command[1] 
        await client.send_message(
            chat_id=message.from_user.id,
            text="**This is message command 2 and 1.**",
            )
        return
        return
    
    data = message.command[1]
    try:
        pre, file_id = data.split('_', 1)
    except:
        file_id = data
        pre = ""
    if data.split("-", 1)[0] == "BATCH":
        sts = await message.reply("I am sending files in your TARGET CHANNEL, when it will complete i will notify you via a message. If i am not sending files in your TARGET CHANNEL then check your logs.")
        file_id = data.split("-", 1)[1]
        msgs = BATCH_FILES.get(file_id)
        if not msgs:
            file = await bot.download_media(file_id)
            try: 
                with open(file) as file_data:
                    msgs=json.loads(file_data.read())
            except:
                await sts.edit("FAILED")
                return await bot.send_message(LOG_CHANNEL, "UNABLE TO OPEN FILE.")
            os.remove(file)
            BATCH_FILES[file_id] = msgs
        for msg in msgs:
            title = msg.get("title")
            size=get_size(int(msg.get("size", 0)))
            f_caption=msg.get("caption", "")
            if BATCH_FILE_CAPTION:
                try:
                    f_caption=BATCH_FILE_CAPTION.format(file_name= '' if title is None else title, file_size='' if size is None else size, file_caption='' if f_caption is None else f_caption)
                except Exception as e:
                    logger.exception(e)
                    f_caption=f_caption
            if f_caption is None:
                f_caption = f"{title}"
            try:
                await bot.send_cached_media(
                    chat_id=Var.TARGET_CHANNEL,
                    file_id=msg.get("file_id"),
                    caption=f_caption,
                    protect_content=msg.get('protect', False),
                    )
            except FloodWait as e:
                await asyncio.sleep(e.x)
                logger.warning(f"Floodwait of {e.x} sec.")
                await client.send_cached_media(
                    chat_id=Var.TARGET_CHANNEL,
                    file_id=msg.get("file_id"),
                    caption=f_caption,
                    protect_content=msg.get('protect', False),
                    )
            except Exception as e:
                logger.warning(e, exc_info=True)
                continue
            await asyncio.sleep(3)
        await sts.delete()
        await bot.send_message(
            chat_id=message.chat.id,
            text="""All files have been successfully sent to TARGET CHANNEL. If not then check your logs."""
        )
        return

@Client.on_message(filters.command("forward") & filters.incoming & ~filters.edited)
async def start(bot, message):
    await bot.forward_messages("message.chat.id", "himanshurastogiofficial", [3, 20, 27])
