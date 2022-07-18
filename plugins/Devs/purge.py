import asyncio
from info import ADMINS
from pyrogram import Client, filters

TG_MAX_SELECT_LEN = 100


@Client.on_message(filters.command("purge") & filters.user(ADMINS))
async def purge(client, message):
    """ purge upto the replied message """
    if message.chat.type not in (("supergroup", "channel")):
        await message.reply(message.chat.id, "Use it only in Group and Channel")

    await message.delete()
    message_ids = []
    count_del_etion_s = 0

    if message.reply_to_message:
        for a_s_message_id in range(
            message.reply_to_message.message_id, message.message_id
        ):
            message_ids.append(a_s_message_id)
            if len(message_ids) == TG_MAX_SELECT_LEN:
                await client.delete_messages(
                    chat_id=message.chat.id, message_ids=message_ids, revoke=True
                )
                count_del_etion_s += len(message_ids)
                message_ids = []
        if len(message_ids) > 0:
            await client.delete_messages(
                chat_id=message.chat.id, message_ids=message_ids, revoke=True
            )
            count_del_etion_s += len(message_ids)

    status_message = await message.reply(f"Successfully deleted {count_del_etion_s} messages")
    await asyncio.sleep(5)
    await status_message.delete()
