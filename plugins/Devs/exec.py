import asyncio
from io import BytesIO
from info import ADMINS
from pyrogram import Client, filters

MAX_MESSAGE_LENGTH = 4096

@Client.on_message(filters.command("exec") & filters.user(ADMINS))
async def execution(_, message):
    status_message = await message.reply_text("Processing ...")
    # DELAY_BETWEEN_EDITS = 0.3
    # PROCESS_RUN_TIME = 100
    cmd = message.text.split(" ", maxsplit=1)[1]

    reply_to_ = message
    if message.reply_to_message:
        reply_to_ = message.reply_to_message

    # start_time = time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    e = stderr.decode()
    if not e:
        e = "😂"
    o = stdout.decode()
    if not o:
        o = "😐"

    OUTPUT = ""
    OUTPUT += f"<b>QUERY:</b>\n<u>Command:</u>\n<code>{cmd}</code> \n"
    OUTPUT += f"<u>PID</u>: <code>{process.pid}</code>\n\n"
    OUTPUT += f"<b>stderr</b>: \n<code>{e}</code>\n\n"
    OUTPUT += f"<b>stdout</b>: \n<code>{o}</code>"

    if len(OUTPUT) > MAX_MESSAGE_LENGTH:
        with BytesIO(str.encode(OUTPUT)) as out_file:
            out_file.name = "exec.text"
            await reply_to_.reply_document(
                document=out_file,
                caption=cmd[: MAX_MESSAGE_LENGTH // 4 - 1],
                disable_notification=True,
                thumb="resources/devoloper.png",
                quote=True,
            )
    else:
        await reply_to_.reply_text(OUTPUT, quote=True)

    await status_message.delete()
