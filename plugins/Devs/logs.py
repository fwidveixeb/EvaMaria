from info import ADMINS
from pyrogram import Client, filters

@Client.on_message(filters.command('logs') & filters.user(ADMINS))
async def logs(bot, message):
    try:
        await message.reply_document('Hagadmansa.log')
    except Exception as e:
        await message.reply(str(e))
