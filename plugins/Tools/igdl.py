import requests
from pyrogram import Client, filters

@Client.on_message(filters.command("igdl"))
async def igdl(bot, message):
  
  ig = await message.reply("`Processing...`")
  
  if len(message.command) == 1:
      return await ig.edit("Read Help Menu to know how command works")
  
  elif len(message.command) == 2:
      return await ig.edit("Read Help Menu to know how command works")
  
  elif len(message.command) == 3:
      if message.command[1] in ["reel", "Reel", "reels", "Reels"]:
          tk = message.text.split("/")
          if tk[4] != "reel":
              return await ig.edit("Wrong url, it looks like this is not a reel")
          pk = message.text.split()
          nk = pk[2]
          uk = nk.split("/")
          url = uk[0] + "//" + uk[2] + "/" + uk[3] + "/" + uk[4]
          print(url)
          out = requests.get(f"https://open-apis-rest.up.railway.app/api/instareel?url={url}").json()
          reel = out["data"]["data"]["url"]
          await message.reply_video(video=reel, caption="Here is your reel.")
          return await ig.delete()
