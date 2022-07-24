from pyrogram import Client, filters
import random
from utils import temp
from pyrogram.types import Message
from database.users_chats_db import db
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from info import SUPPORT_CHAT, PICS

async def disabled_chat(_, client, message: Message):
    return message.chat.id in temp.BANNED_CHATS

disabled_group=filters.create(disabled_chat)

@Client.on_message(filters.group & disabled_group & filters.incoming)
async def grp_bd(bot, message):
    buttons = [[
        InlineKeyboardButton('💬 Support', url=f'https://t.me/{SUPPORT_CHAT}'),
        InlineKeyboardButton('🔐 Close', callback_data='close')
    ]]
    reply_markup=InlineKeyboardMarkup(buttons)
    vazha = await db.get_chat(message.chat.id)
    k = await message.reply(
        text=f"🚫 <b>Chat not allowed</b> \nMy admins has restricted me from working here! \n<b>Reason:</b> {vazha['reason']}.",
        quote=True,
        disable_web_page_preview=True,
        reply_markup=reply_markup)
    try:
        await k.pin()
    except:
        pass
    await bot.leave_chat(message.chat.id)
