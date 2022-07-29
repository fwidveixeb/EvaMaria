from shutil import rmtree
from pyrogram import Client, filters
from plugins.Helper.google_image import googleimagesdownload

@Client.on_message(filters.command("img"))
async def img(bot, message):
 
    img = await message.reply("`Processing...`")
    
    if len(message.command) == 1:
      return await img.edit("No query provided to search, Read Help Menu to know how command works.")
       
    elif len(message.command) > 1:
      query = message.command[1:]
      limit = 5
      if ";" in query:
        try:
            query = query.split(";")[0]
            limit = int(query.split(";")[1])
        except BaseException:
            pass
      
      ggl = googleimagesdownload()
      args = {
          "keywords": query,
          "limit": limit,
          "format": "jpg",
          "output_directory": "./resources/",
      }
      path = await ggl.download(args)
      ok = ['hagadmansa']
      await message.reply_media_group(media=ok)
      rmtree(f"./resources/{query}/")
      await img.delete()
      
    else:
      return await img.edit("Parameter limit exceeded, Read Help Menu to know how command works.")
