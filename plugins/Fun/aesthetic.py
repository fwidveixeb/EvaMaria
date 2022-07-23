from pyrogram import Client, filters

def aesthetify(string):
    PRINTABLE_ASCII = range(0x21, 0x7F)
    for c in string:
        c = ord(c)
        if c in PRINTABLE_ASCII:
            c += 0xFF00 - 0x20
        elif c == ord(" "):
            c = 0x3000
        yield chr(c)


@Client.on_message(filters.command("ae"))
async def aesthetic(client, message):
    for e in message.command[1:]:
      text = "".join(str(e))
      text = "".join(aesthetify(text))
      await message.reply(text)
   
