from pyrogram import Client, filters

@Client.on_message(filters.command("restart"))
async def restart(bot, message):
  a = await message.reply("Restarting Bot, this may take some time...")
  await app.restart()
  await a.delete()
  await message.reply("Restarted successfully.")
