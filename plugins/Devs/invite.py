from info import ADMINS
from pyrogram import Client, filters


@Client.on_message(filters.command('invite') & filters.user(ADMINS))
async def gen_invite(bot, message):
    if len(message.command) == 1:
        return await message.reply('Give me a chat id')
    chat = message.command[1]
    try:
        chat = int(chat)
    except:
        return await message.reply('Give Me A Valid Chat ID')
    try:
        link = await bot.create_chat_invite_link(chat)
    except ChatAdminRequired:
        return await message.reply("Invite Link Generation Failed, I'am Not Having Sufficient Rights")
    except Exception as e:
        return await message.reply(f'Error {e}')
    await message.reply(f'Here is your Invite Link {link.invite_link}')
