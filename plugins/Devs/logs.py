import os
from info import ADMINS
from pyrogram import Client, filters

@Client.on_message(filters.command(['log', 'logs']) & filters.user(ADMINS))
async def logs(bot, message):
    os.rename('TelegramBot.log', 'Hagadmansa.log')
    await message.reply_document(document='Hagadmansa.log', caption='Bot Logs')
    
