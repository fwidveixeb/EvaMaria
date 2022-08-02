from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto

HELP_TXT = """**Welcome to the Help Menu**

Here you will find a detailed overview of every command with examples.

Click on 'Open Help Menu' to open the detailed Menu."""

LIST_1_TXT = "List 1"

LIST_2_TXT = "List 2"

LIST_3_TXT = "List 3"

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
            InlineKeyboardButton('4', callback_data='1'),
            InlineKeyboardButton('5', callback_data='2'),
            InlineKeyboardButton('6', callback_data='3')
            ],[
            InlineKeyboardButton('7', callback_data='1'),
            InlineKeyboardButton('8', callback_data='2'),
            InlineKeyboardButton('9', callback_data='3')
            ],[
            InlineKeyboardButton('10', callback_data='1'),
            InlineKeyboardButton('11', callback_data='2'),
            InlineKeyboardButton('12', callback_data='3')
            ],[
            InlineKeyboardButton('⇦', callback_data='list_3'),
            InlineKeyboardButton('Home', callback_data='help'),
            InlineKeyboardButton('⇨', callback_data='list_2')
       ]])

LIST_2_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('13', callback_data='1'),
            InlineKeyboardButton('14', callback_data='2'),
            InlineKeyboardButton('15', callback_data='3')
            ],[
            InlineKeyboardButton('16', callback_data='1'),
            InlineKeyboardButton('17', callback_data='2'),
            InlineKeyboardButton('18', callback_data='3')
            ],[
            InlineKeyboardButton('19', callback_data='1'),
            InlineKeyboardButton('20', callback_data='2'),
            InlineKeyboardButton('21', callback_data='3')
            ],[
            InlineKeyboardButton('22', callback_data='1'),
            InlineKeyboardButton('23', callback_data='2'),
            InlineKeyboardButton('24', callback_data='3')
            ],[
            InlineKeyboardButton('⇦', callback_data='list_1'),
            InlineKeyboardButton('Home', callback_data='help'),
            InlineKeyboardButton('⇨', callback_data='list_3')
       ]])

LIST_3_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('25', callback_data='1'),
            InlineKeyboardButton('26', callback_data='2'),
            InlineKeyboardButton('27', callback_data='3')
            ],[
            InlineKeyboardButton('28', callback_data='1'),
            InlineKeyboardButton('29', callback_data='2'),
            InlineKeyboardButton('30', callback_data='3')
            ],[
            InlineKeyboardButton('31', callback_data='1'),
            InlineKeyboardButton('32', callback_data='2'),
            InlineKeyboardButton('33', callback_data='3')
            ],[
            InlineKeyboardButton('34', callback_data='1'),
            InlineKeyboardButton('35', callback_data='2'),
            InlineKeyboardButton('36', callback_data='3')
            ],[
            InlineKeyboardButton('⇦', callback_data='list_2'),
            InlineKeyboardButton('Home', callback_data='help'),
            InlineKeyboardButton('⇨', callback_data='list_1')
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
    elif message.data == "list_2":
        await message.answer('www.hagadmansa.com')
        await message.edit_message_text(
          text=LIST_2_TXT,
          reply_markup=LIST_2_BTN
        )
    elif message.data == "list_3":
        await message.answer('www.hagadmansa.com')
        await message.edit_message_text(
          text=LIST_3_TXT,
          reply_markup=LIST_3_BTN
        )
      
@Client.on_message(filters.command("hp")) 
async def help(client, message):
  
    await message.reply_photo(
      photo="https://telegra.ph/file/ebba73e063dac600db5d0.jpg",
      caption=HELP_TXT,
      reply_markup=HELP_BTN
    )
