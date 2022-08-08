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
from info import CHANNELS, ADMINS, AUTH_CHANNEL, LOG_CHANNEL, PICS, BATCH_FILE_CAPTION, CUSTOM_FILE_CAPTION, PROTECT_CONTENT
from utils import get_settings, get_size, is_subscribed, save_group_settings, temp
from database.connections_mdb import active_connection
import re
import json
import base64
logger = logging.getLogger(__name__)

BATCH_FILES = {}

LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""

@Client.on_message(filters.command("start") & filters.incoming & ~filters.edited)
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
            reply_markup=reply_markup,
            parse_mode='html'
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
    if data.split("-", 1)[0] == "BATCH":
        sts = await message.reply("Please wait")
        file_id = data.split("-", 1)[1]
        msgs = BATCH_FILES.get(file_id)
        if not msgs:
            file = await client.download_media(file_id)
            try: 
                with open(file) as file_data:
                    msgs=json.loads(file_data.read())
            except:
                await sts.edit("FAILED")
                return await client.send_message(LOG_CHANNEL, "UNABLE TO OPEN FILE.")
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
                await client.send_cached_media(
                    chat_id=message.chat.id,
                    file_id=msg.get("file_id"),
                    caption=f_caption,
                    protect_content=msg.get('protect', False),
                    )
            except FloodWait as e:
                await asyncio.sleep(e.x)
                logger.warning(f"Floodwait of {e.x} sec.")
                await client.send_cached_media(
                    chat_id=Var.message.chat.id,
                    file_id=msg.get("file_id"),
                    caption=f_caption,
                    protect_content=msg.get('protect', False),
                    )
            except Exception as e:
                logger.warning(e, exc_info=True)
                continue
        await sts.edit(
            text=f"all files has been successfully sent to Target Channel"
            )
        return
    elif data.split("-", 1)[0] == "DSTORE":
        sts = await message.reply("Please wait")
        b_string = data.split("-", 1)[1]
        decoded = (base64.urlsafe_b64decode(b_string + "=" * (-len(b_string) % 4))).decode("ascii")
        try:
            f_msg_id, l_msg_id, f_chat_id, protect = decoded.split("_", 3)
        except:
            f_msg_id, l_msg_id, f_chat_id = decoded.split("_", 2)
            protect = "/pbatch" if PROTECT_CONTENT else "batch"
        diff = int(l_msg_id) - int(f_msg_id)
        async for msg in client.iter_messages(int(f_chat_id), int(l_msg_id), int(f_msg_id)):
            if msg.media:
                media = getattr(msg, msg.media)
                if BATCH_FILE_CAPTION:
                    try:
                        f_caption=BATCH_FILE_CAPTION.format(file_name=getattr(media, 'file_name', ''), file_size=getattr(media, 'file_size', ''), file_caption=getattr(msg, 'caption', ''))
                    except Exception as e:
                        logger.exception(e)
                        f_caption = getattr(msg, 'caption', '')
                else:
                    media = getattr(msg, msg.media)
                    file_name = getattr(media, 'file_name', '')
                    f_caption = getattr(msg, 'caption', file_name)
                try:
                    await msg.copy(message.chat.id, caption=f_caption, protect_content=True if protect == "/pbatch" else False)
                except FloodWait as e:
                    await asyncio.sleep(e.x)
                    await msg.copy(message.chat.id, caption=f_caption, protect_content=True if protect == "/pbatch" else False)
                except Exception as e:
                    logger.exception(e)
                    continue
            elif msg.empty:
                continue
            else:
                try:
                    await msg.copy(message.chat.id, protect_content=True if protect == "/pbatch" else False)
                except FloodWait as e:
                    await asyncio.sleep(e.x)
                    await msg.copy(message.chat.id, protect_content=True if protect == "/pbatch" else False)
                except Exception as e:
                    logger.exception(e)
                    continue
            await asyncio.sleep(1) 
        return await sts.delete()
        

    files_ = await get_file_details(file_id)           
    if not files_:
        pre, file_id = ((base64.urlsafe_b64decode(data + "=" * (-len(data) % 4))).decode("ascii")).split("_", 1)
        try:
            msg = await client.send_cached_media(
                chat_id=message.from_user.id,
                file_id=file_id
            )
            filetype = msg.media
            file = getattr(msg, filetype)
            title = file.file_name
            size=get_size(file.file_size)
            f_caption = f"<code>{title}</code>"
            if CUSTOM_FILE_CAPTION:
                try:
                    f_caption=CUSTOM_FILE_CAPTION.format(file_name= '' if title is None else title, file_size='' if size is None else size, file_caption='')
                except:
                    return
            #await msg.edit_caption(f_caption)
            hemlo = await client.send_message('This file will be deleted in 1 hour, make sure you forward it to your saved messages.')
            await asyncio.sleep(10)
            await msg.delete()
            await hemlo.delete()
            return
        except:
            pass
        return await message.reply('No such file exist.')
    files = files_[0]
    title = files.file_name
    size=get_size(files.file_size)
    f_caption=files.caption
    if CUSTOM_FILE_CAPTION:
        try:
            f_caption=CUSTOM_FILE_CAPTION.format(file_name= '' if title is None else title, file_size='' if size is None else size, file_caption='' if f_caption is None else f_caption)
        except Exception as e:
            logger.exception(e)
            f_caption=f_caption
    if f_caption is None:
        f_caption = f"{files.file_name}"
    await client.send_cached_media(
        chat_id=message.from_user.id,
        file_id=file_id,
        caption=f_caption,
        protect_content=True if pre == 'filep' else False,
        )
                    
