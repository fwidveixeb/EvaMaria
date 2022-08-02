import requests
from pyrogram import Client, filters

@Client.on_message(filters.command("ttdl"))
async def ttdl(bot, message):
  
  tt = await message.reply("`Processing...`")
  
  if len(message.command) == 1:
      return await tt.edit("No URL provided to download, Read Help Menu to know how command works")
  
  elif len(message.command) == 2:
      url = message.command[1]
      out = requests.get(f"https://open-apis-rest.up.railway.app/api/tiktok?url={url}").json()
      try:
          m = out["error"]
          return await ig.edit("Wrong URL provided.")
      except:
          pass
      try:
          video = out["data"]["server1"]["video"]
      except:
          return await tt.edit("API didn't responded, please report it at @HagadmansaChat or try again later.")
      await message.reply_video(video=video, caption="Here is your video.")
      return await tt.delete()
  else:
      await tt.edit("Parameter limit exceeded, Read Help Menu to know how command works.")
