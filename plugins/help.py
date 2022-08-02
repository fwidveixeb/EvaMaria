from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto

HELP_TXT = """**Welcome to the Help Menu**

Here you will find a detailed overview of every command with examples.

Click on 'Open Help Menu' to open the detailed Menu."""

LIST_1_TXT = "12 Commands are listed here."

HELP_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('Visit Website', url='https://hagadmansa.com')
            ],[
            InlineKeyboardButton('Updates', url='https://t.me/hagadmansa'),
            InlineKeyboardButton('Support', url='https://t.me/hagadmansachat')
            ],[
            InlineKeyboardButton('Open Help Menu', callback_data='list_1')
        ]])

LIST_1_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('1', callback_data='1'),
            InlineKeyboardButton('2', callback_data='2'),
            InlineKeyboardButton('3', callback_data='3')
            ],[
            InlineKeyboardButton('1', callback_data='1'),
            InlineKeyboardButton('2', callback_data='2'),
            InlineKeyboardButton('3', callback_data='3')
            ],[
            InlineKeyboardButton('1', callback_data='1'),
            InlineKeyboardButton('2', callback_data='2'),
            InlineKeyboardButton('3', callback_data='3')
            ],[
            InlineKeyboardButton('1', callback_data='1'),
            InlineKeyboardButton('2', callback_data='2'),
            InlineKeyboardButton('3', callback_data='3')
            ],[
            InlineKeyboardButton('⇦', callback_data='1'),
            InlineKeyboardButton('Home', callback_data='help'),
            InlineKeyboardButton('⇨', callback_data='3')
       ]])

@Client.on_callback_query()
async def cb_data(bot, message):
    if message.data == "help":
        await message.answer('www.hagadmansa.com')
        await message.edit_message_text(
          text=HELP_TXT,
          reply_markup=HELP_BTN
        )
    elif message.data == "list_1":
        await message.answer('www.hagadmansa.com')
        await message.edit_message_text(
          text=LIST_1_TXT,
          reply_markup=LIST_1_BTN
        )
      
@Client.on_message(filters.command("help")) 
async def help(client, message):
  
    await message.reply_photo(
      photo="https://telegra.ph/file/ebba73e063dac600db5d0.jpg",
      caption=HELP_TXT,
      reply_markup=HELP_BTN
    )
