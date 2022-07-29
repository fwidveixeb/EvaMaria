from shutil import rmtree
from pyrogram import Client, filters
from pyUltroid.functions.google_image import googleimagesdownload

@Client.on_messqge(filters.command("img"))
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
      try:
        ggl = googleimagesdownload()
        args = {
            "keywords": query,
            "limit": lmt,
            "format": "jpg",
            "output_directory": "./resources/",
        }
        path = await ggl.download(args)
        ok = path[0][query]
        await message.reply_photo(photo=ok, caption=query)
        rmtree(f"./resources/{query}/")
        await img.delete()
      except Exception as e:
        return await img.edit(f"#Error {e}")
   else:
     return await img.edit("Parameter limit exceeded, Read Help Menu to know how command works.")
