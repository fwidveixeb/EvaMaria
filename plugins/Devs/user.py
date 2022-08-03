from pyrogram import Client

@Client.on_message(filters.command("user"))
async def user(bot, message):
  user = message,command[1]
  k = await bot.get_users(user)
  print(k)
  await message.reply(k)
