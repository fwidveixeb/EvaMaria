from pyrogram import Client, filters
from plugins.Helper.get_synonyms_or_antonyms import get_synonyms_or_antonyms

@Client.on_message(filters.command("synonym"))
async def synonym(bot, message):
  
    synonym = await message.reply("`Processing...`")
    
    if len(message.command) == 1:
        return await synonym.edit("No word provided to find synonyms, Read Help Menu to know how command works")
    
    elif len(message.command) == 2:
        word = message.command[1]
        ok = await get_synonyms_or_antonyms(word, "synonyms")
        x = "".format(word)
        try:
            for c, i in enumerate(ok, start=1):
                x += f"**{c}.** `{i}`\n"
            if len(x) > 4096:
                with io.BytesIO(str.encode(x)) as file:
                    file.name = f"{word}-synonyms.txt"
                    await message.reply_document(document=file, caption=f"Synonyms of {word}", thumb="resources/devoloper.png")
                    return await synonym.delete()
            else:
                await synonym.edit(x)
        except Exception as e:
            return await synonym.edit(e)
    else:
        await synonym.edit("Parameter limit exceeded, Read Help Menu to know how command works.")
