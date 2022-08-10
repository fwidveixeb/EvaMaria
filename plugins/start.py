import os
import logging
import random
import asyncio
from plugins.help import ADVICE_TXT, BULLY_TXT, CARBON_TXT, DAGD_TXT, DARE_TXT, DECIDE_TXT, DNS_TXT, DOB_TXT, DOC_TXT, FACT_TXT, FAKEINFO_TXT, FILESTORE_TXT, FILESTREAM_TXT, GITHUB_TXT, GLITCH_TXT, HEX_TXT, HOST_TXT, IMG_TXT, INFO_TXT, IP_TXT, JOKE_TXT, MEANING_TXT, NCODE_TXT, NEKOBIN_TXT, PEXELS_TXT, PHLOGO_TXT, PICSUM_TXT, QRCODE_TXT, QUOTE_TXT, RMBG_TXT, SPACEBIN_TXT, TELEGRAPH_TXT, TPDNE_TXT, TRUTH_TXT, UD_TXT, WHOIS_TXT
from pyrogram import Client, filters
from pyrogram.errors import ChatAdminRequired, FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.ia_filterdb import Media, get_file_details, unpack_new_file_id
from database.users_chats_db import db
from info import CHANNELS, ADMINS, AUTH_CHANNEL, LOG_CHANNEL, PICS, CUSTOM_FILE_CAPTION

import re
import json
import base64
logger = logging.getLogger(__name__)


LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""

@Client.on_message(filters.command("start"))
async def start(client, message):
    if message.chat.type in ['group', 'supergroup']:
        buttons = [
            [
                InlineKeyboardButton('🤖 Updates', url='https://t.me/hagadmansa')
            ],
            [
                InlineKeyboardButton('ℹ️ Help', url=f"https://t.me/hagadmansabot"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply(script.START_TXT.format(message.from_user.mention if message.from_user else message.chat.title, temp.U_NAME, temp.B_NAME), reply_markup=reply_markup)
        await asyncio.sleep(2) # 😢 https://github.com/EvamariaTG/EvaMaria/blob/master/plugins/p_ttishow.py#L17 😬 wait a bit, before checking.
        if not await db.get_chat(message.chat.id):
            total=await client.get_chat_members_count(message.chat.id)
            await client.send_message(LOG_CHANNEL, LOG_TEXT_G.format(message.chat.title, message.chat.id, total, "Unknown"))       
            await db.add_chat(message.chat.id, message.chat.title)
        return 
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id, message.from_user.first_name)
        await client.send_message(LOG_CHANNEL, LOG_TEXT_P.format(message.from_user.id, message.from_user.mention))
    if len(message.command) != 2:
        reply_markup = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('Updates', url='https://t.me/hagadmansa'),
            InlineKeyboardButton('Support', url='https://t.me/hagadmansachat')
            ],[
            InlineKeyboardButton('Visit Website', url='https://hagadmansa.com')
            ]])
        await message.reply_photo(
            photo="https://telegra.ph/file/bcaca021044aac6ac3804.jpg",
            caption=f"Hello {message.from_user.mention}, I can provide you movies, apart from that i've a lot of featurs.\n\nJust visit my website www.hagadmansa.com to download movies else send /cmds or /help to know my other features.",
            reply_markup=reply_markup
        )
        return
    
    if message.command[1].lower() == "advice":   
         advice = await message.reply("`Processing...`")
         await asyncio.sleep(0.5)
         return await advice.edit(ADVICE_TXT)
    elif message.command[1].lower() == "bully":
         bully = await message.reply("`Processing...`")
         await asyncio.sleep(0.5)
         return await bully.edit(BULLY_TXT)
    elif message.command[1].lower() == "carbon":
         carbon = await message.reply("`Processing...`")
         await asyncio.sleep(0.5)
         return await carbon.edit(CARBON_TXT)
    elif message.command[1].lower() == "advice":
        advice = await message.reply("`Processing...`")
        await asyncio.sleep(0.5) 
        return await advice.edit(ADVICE_TXT)
    elif message.command[1].lower() == "bully":
         bully = await message.reply("`Processing...`")
         await asyncio.sleep(0.5)
         return await bully.edit(BULLY_TXT)
    elif message.command[1].lower() == "carbon":
         carbon = await message.reply("`Processing...`") 
         await asyncio.sleep(0.5)
         return await carbon.edit(CARBON_TXT)
    elif message.command[1].lower() == "dagd":
         dagd = await message.reply("`Processing...`")
         await asyncio.sleep(0.5)
         return await dagd.edit(DAGD_TXT)
    elif message.command[1].lower() == "dare":
         dare = await message.reply("`Processing...`")
         await asyncio.sleep(0.5)
         return await dare.edit(DARE_TXT)    
    elif message.command[1].lower() == "decide":
         decide = await message.reply("`Processing...`")
         await asyncio.sleep(0.5)
         return await decide.edit(DECIDE_TXT)
    elif message.command[1].lower() == "dns":
         dns = await message.reply("`Processing...`")
         await asyncio.sleep(0.5)
         return await dns.edit(DNS_TXT)
    elif message.command[1].lower() == "dob":
         dob = await message.reply("`Processing...`")    
         await asyncio.sleep(0.5)
         return await dob.edit(DOB_TXT)
    elif message.command[1].lower() == "doc":
         doc = await message.reply("`Processing...`")
         await asyncio.sleep(0.5)
         return await doc.edit(DOC_TXT)
    elif message.command[1].lower() == "fact":
         fact = await message.reply("`Processing...`")
         await asyncio.sleep(0.5)    
         return await fact.edit(FACT_TXT)
    elif message.command[1].lower() == "fakeinfo":
         fakeinfo = await message.reply("`Processing...`")
         await asyncio.sleep(0.5)
         return await fakeinfo.edit(FAKEINFO_TXT)
    elif message.command[1].lower() == "filestore":
         filestore = await message.reply("`Processing...`")
         await asyncio.sleep(0.5)
         return await filestore.edit(FILESTORE_TXT)
    elif message.command[1].lower() == "filestream":
         filestream = await message.reply("`Processing...`")
         await asyncio.sleep(0.5)    
         return await filestream.edit(FILESTREAM_TXT)
    elif message.command[1].lower() == "github":
         github = await message.reply("`Processing...`")
         await asyncio.sleep(0.5)
         return await github.edit(GITHUB_TXT)
    elif message.command[1].lower() == "glitch":
         glitch = await message.reply("`Processing...`")
         await asyncio.sleep(0.5)
         return await glitch.edit(GLITCH_TXT)
    elif message.command[1].lower() == "hex":
         hexn = await message.reply("`Processing...`")
         await asyncio.sleep(0.5)
         return await hexn.edit(HEX_TXT)
    elif message.command[1].lower() == "host":
         host = await message.reply("`Processing...`")
         await asyncio.sleep(0.5)
         return await host.edit(HOST_TXT)
    elif message.command[1].lower() == "img":
         img = await message.reply("`Processing...`")
         await asyncio.sleep(0.5)
         return await img.edit(IMG_TXT)
    elif message.command[1].lower() == "info":
         info = await message.reply("`Processing...`")
         await asyncio.sleep(0.5)
         return await info.edit(INFO_TXT)
    elif message.command[1].lower() == "ip":
         ip = await message.reply("`Processing...`")
         await asyncio.sleep(0.5)
         return await ip.edit(IP_TXT)
    elif message.command[1].lower() == "joke":
         joke = await message.reply("`Processing...`")
         await asyncio.sleep(0.5)
         return await joke.edit(JOKE_TXT)
    elif message.command[1].lower() == "meaning":
         meaning = await message.reply("`Processing...`")
         await asyncio.sleep(0.5)
         return await meaning.edit(MEANING_TXT)
    elif message.command[1].lower() == "ncode":
         ncode = await message.reply("`Processing...`")
         await asyncio.sleep(0.5)
         return await ncode.edit(NCODE_TXT)
    elif message.command[1].lower() == "nekobin":
         nekobin = await message.reply("`Processing...`")
         await asyncio.sleep(0.5)
         return await nekobin.edit(NEKOBIN_TXT)
    elif message.command[1].lower() == "pexels":
         pexels = await message.reply("`Processing...`")
         await asyncio.sleep(0.5)
         return await pexels.edit(PEXELS_TXT)
    elif message.command[1].lower() == "phlogo":
         phlogo = await message.reply("`Processing...`")
         await asyncio.sleep(0.5)
         return await phlogo.edit(PHLOGO_TXT)
    elif message.command[1].lower() == "picsum":
         picsum = await message.reply("`Processing...`")
         await asyncio.sleep(0.5)
         return await picsum.edit(PICSUM_TXT)
    elif message.command[1].lower() == "qrcode":
         qrcode = await message.reply("`Processing...`")
         await asyncio.sleep(0.5)
         return await qrcode.edit(QRCODE_TXT)
    elif message.command[1].lower() == "quote":
         quote = await message.reply("`Processing...`")
         await asyncio.sleep(0.5)
         return await quote.edit(QUOTE_TXT)
    elif message.command[1].lower() == "rmbg":
         rmbg = await message.reply("`Processing...`")
         await asyncio.sleep(0.5)
         return await rmbg.edit(RMBG_TXT)
    elif message.command[1].lower() == "spacebin":
         spacebin = await message.reply("`Processing...`")
         await asyncio.sleep(0.5)
         return await spacebin.edit(SPACEBIN_TXT)
    elif message.command[1].lower() == "telegraph":
         telegraph = await message.reply("`Processing...`")
         await asyncio.sleep(0.5)
         return await telegraph.edit(TELEGRAPH_TXT)
    elif message.command[1].lower() == "tpdne":
         tpdne = await message.reply("`Processing...`")
         await asyncio.sleep(0.5)
         return await tpdne.edit(TPDNE_TXT)
    elif message.command[1].lower() == "truth":
         truth = await message.reply("`Processing...`")
         await asyncio.sleep(0.5)
         return await truth.edit(TRUTH_TXT)
    elif message.command[1].lower() == "ud":
         ud = await message.reply("`Processing...`")
         await asyncio.sleep(0.5)
         return await ud.edit(UD_TXT)
    elif message.command[1].lower() == "whois":
         whois = await message.reply("`Processing...`")
         await asyncio.sleep(0.5)
         return await whois.edit(WHOIS_TXT)
    
    data = message.command[1]
    try:
        pre, file_id = data.split('_', 1)
    except:
        file_id = data
        pre = ""
    files_ = await get_file_details(file_id)           
    if not files_:
        pre, file_id = ((base64.urlsafe_b64decode(data + "=" * (-len(data) % 4))).decode("ascii")).split("_", 1)
        try:
            msg = await message.reply_cached_media(file_id)
            filetype = msg.media
            file = getattr(msg, filetype.value)
            title = file.file_name
            size = file.file_size
            f_caption=CUSTOM_FILE_CAPTION.format(file_name= '' if title is None else title, file_size='' if size is None else size, file_caption='')
            await msg.edit(f_caption)
            hemlo = await message.reply('**NOTE: This file will be deleted in 10 minutes to avoid copyright infringement, make sure you forward it to your saved messages.**')
            await asyncio.sleep(600)
            await msg.delete()
            await hemlo.delete()
            return await message.reply("Your file has been deleted to avoid copyright infringement, send /cmds or /help to know about other features.")
        except Exception as e:
            return await message.reply(e)
    
