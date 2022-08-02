import random
import asyncio
from Vars import Var
from info import PICS, ADMINS
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto

HELP_TEXT = """**Welcome to the Help Menu**

Here you will find a detailed overview of every command with examples.

Click on 'Open Help Menu' to open the detailed Menu."""

HELP_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('Visit Website', url='https://hagadmansa.com')
            ],[
            InlineKeyboardButton('Updates', url='https://t.me/hagadmansa'),
            InlineKeyboardButton('Support', url='https://t.me/hagadmansachat')
            ],[
            InlineKeyboardButton('Open Help Menu', callback_data='help')
        ]])

@Client.on_callback_query()
async def cb_data(bot, message):
    if message.data == "help":
        await message.answer('www.hagadmansa.com')
        await message.edit(
          caotion=HELP_TEXT,
          reply_markup=HELP_BUTTONS
        )

@Client.on_message(filters.command("help")) 
async def help(client, message):
  
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=HELP_TEXT,
        reply_markup=HELP_BUTTONS
    )
