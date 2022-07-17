import time
from info import ADMINS
from pyrogram import Client, filters

@Client.on_message(filters.command("ping") & filters.user(ADMINS))
async def ping(_, message):
    start_time = time.time()
    end_time = time.time()
    time_taken = (end_t - start_t) * 1000
    await message.reply_text(f"Pong!\n{time_taken:.3f} ms")
