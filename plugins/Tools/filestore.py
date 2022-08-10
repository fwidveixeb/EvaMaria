import re
import asyncio
import urllib.parse
import logging
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from typing import Any, Optional
from urllib.parse import quote_plus
from Vars import Var
from pyrogram import filters, Client, enums
from pyrogram.file_id import FileId
from pyrogram.errors.exceptions.bad_request_400 import ChannelInvalid, UsernameInvalid, UsernameNotModified
from info import ADMINS, LOG_CHANNEL, FILE_STORE_CHANNEL, PUBLIC_FILE_STORE
from database.ia_filterdb import unpack_new_file_id
from utils import temp
import os
import json
import base64
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

async def allowed(_, __, message):
    if PUBLIC_FILE_STORE:
        return True
    if message.from_user and message.from_user.id in ADMINS:
        return True
    return False


@Client.on_message(filters.command(['fs', 'filestore']) & filters.create(allowed))
async def gen_link_s(bot, message):
    replied = message.reply_to_message
    if not replied:
        return await message.reply('Reply to a File, Video or Audio only.')
    file_type = replied.media
    if file_type not in [enums.MessageMediaType.VIDEO, enums.MessageMediaType.AUDIO, enums.MessageMediaType.DOCUMENT]:
        return await message.reply("Reply to a File, Video or Audio only.")
    file_id, ref = unpack_new_file_id((getattr(replied, file_type)).file_id)
    string = 'filep_' if message.text.lower().strip() == "/plink" else 'file_'
    string += file_id
    outstr = base64.urlsafe_b64encode(string.encode("ascii")).decode().strip("=")
    file_link = f'https://t.me/{temp.U_NAME}?start={outstr}'
    await message.delete()
    await message.reply_text(
             text=f"<code>{file_link}</code>",
             quote=True,
             parse_mode="html",
             disable_web_page_preview=True
             )
    
