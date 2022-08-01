from pyrogram import Client, filters
from plugins.Helper.json import json_parser

@Client.on_message(filters.command("json"))
async def json(bot, message):
  
    dns = await message.reply("`Processing...`")
    replied = message.reply_to_message
    if replied:
      msg = replied
    else:
      msg = message
    try:
      match = message.command[1]
    except:
      pass
    if match and hasattr(msg, match):
        msg = getattr(msg, match)
        if hasattr(msg, "to_json"):
            try:
                msg = json_parser(msg.to_json(ensure_ascii=False), indent=1)
            except Exception as e:
                return await json.edit(e)
        msg = str(msg)
    else:
        msg = json_parser(msg.to_json(), indent=1)
    if len(msg) > 4096:
        with io.BytesIO(str.encode(msg)) as out_file:
            out_file.name = f"json_{message,chat.id}.txt"
            await message.reply_document(
              document=f"json_{message,chat.id},
              caption="Here is your JSON data."
              thumb="resources/devoliper.png"
            )
            return await json.delete()
    else:
        await json.edit(f"```{msg or None}```")
