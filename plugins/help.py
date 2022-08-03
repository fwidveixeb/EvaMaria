from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto

HELP_TXT = """**Welcome to the Help Menu**

Here you will find a detailed overview of every command with examples.

Click on 'Open Help Menu' to open the detailed Menu."""

LIST_1_TXT = "List 1"

LIST_2_TXT = "List 2"

LIST_3_TXT = "List 3"

LIST_4_TXT = "List 4"

LIST_5_TXT = "List 5"

ADVICE_TXT = """■ **HELP:** `Advice`

__Get a random advice.__

■ **USAGE:**
**Parameter:** Not required.
**Replied:** Not required.

■ **EXAMPLE:**
**1. **`/advice`"""

BULLY_TXT = """■ **HELP:** `Bully`

__Get a random bully.__

■ **USAGE:**
**Parameter:** Not required.
**Replied:** Not required.

■ **EXAMPLE:**
**1.** `/bully`"""

CARBON_TXT = """■ **HELP:** `Carbon`
 
__Convert your text to beautiful images.__

■ **USAGE:**
**Parameter:** 1, Optional
**Replied:** (message, text document), Required.

**__Command must be reply to a message or text document.__**

**~ 1st Parameter:**
**1.** 1st Parameter must be alphabetical, not numerical.
**2.** Pass `random` to generate random background.
**3.** Pass a color name to generate custom background.
**4.** Pass `colorlist` to get a list of colors.

■ **EXAMPLE:**
**1.** `/carbon`
**2.** `/carbon red`
**3.** `/carbon random`
**4.** `/carbon colorlist`"""

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
            InlineKeyboardButton('Advice', callback_data='advice'),
            InlineKeyboardButton('Bully', callback_data='bully')
            ],[
            InlineKeyboardButton('Carbon', callback_data='carbon'),
            InlineKeyboardButton('Da.gd', callback_data='3')
            ],[
            InlineKeyboardButton('Dare', callback_data='1'),
            InlineKeyboardButton('Decide', callback_data='3')
            ],[
            InlineKeyboardButton('DNS', callback_data='1'),
            InlineKeyboardButton('D.O.B.', callback_data='3')
            ],[
            InlineKeyboardButton('⇦', callback_data='list_5'),
            InlineKeyboardButton('Home', callback_data='help'),
            InlineKeyboardButton('⇨', callback_data='list_2')
       ]])

LIST_2_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('Doc', callback_data='1'),
            InlineKeyboardButton('Fact', callback_data='3')
            ],[
            InlineKeyboardButton('Fake Info', callback_data='1'),
            InlineKeyboardButton('File Store', callback_data='3')
            ],[
            InlineKeyboardButton('File Stream', callback_data='1'),
            InlineKeyboardButton('Github', callback_data='3')
            ],[
            InlineKeyboardButton('Glitch', callback_data='1'),
            InlineKeyboardButton('Hex Color', callback_data='3')
            ],[
            InlineKeyboardButton('⇦', callback_data='list_1'),
            InlineKeyboardButton('Home', callback_data='help'),
            InlineKeyboardButton('⇨', callback_data='list_3')
       ]])

LIST_3_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('Host', callback_data='1'),
            InlineKeyboardButton('Google Img', callback_data='3')
            ],[
            InlineKeyboardButton('User Info', callback_data='1'),
            InlineKeyboardButton('IP Address', callback_data='3')
            ],[
            InlineKeyboardButton('Joke', callback_data='1'),
            InlineKeyboardButton('Meaning', callback_data='3')
            ],[
            InlineKeyboardButton('Ncode', callback_data='1'),
            InlineKeyboardButton('Nekobin', callback_data='3')
            ],[
            InlineKeyboardButton('⇦', callback_data='list_2'),
            InlineKeyboardButton('Home', callback_data='help'),
            InlineKeyboardButton('⇨', callback_data='list_4')
       ]])

LIST_4_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('Pexels', callback_data='1'),
            InlineKeyboardButton('PH Logo', callback_data='3')
            ],[
            InlineKeyboardButton('Picsum', callback_data='1'),
            InlineKeyboardButton('QR Generator', callback_data='3')
            ],[
            InlineKeyboardButton('Quote', callback_data='1'),
            InlineKeyboardButton('Remove BG', callback_data='3')
            ],[
            InlineKeyboardButton('Spacebin', callback_data='1'),
            InlineKeyboardButton('Telegraph', callback_data='3')
            ],[
            InlineKeyboardButton('⇦', callback_data='list_3'),
            InlineKeyboardButton('Home', callback_data='help'),
            InlineKeyboardButton('⇨', callback_data='list_5')
       ]])

LIST_5_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('TPDNE', callback_data='1'),
            InlineKeyboardButton('Truth', callback_data='3')
            ],[
            InlineKeyboardButton('Dictionary', callback_data='1'),
            InlineKeyboardButton('WHOIS', callback_data='3')
            ],[
            InlineKeyboardButton('⇦', callback_data='list_4'),
            InlineKeyboardButton('Home', callback_data='help'),
            InlineKeyboardButton('⇨', callback_data='list_1')
       ]])

ADVICE_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⇦', callback_data='whois'),
            InlineKeyboardButton('Back', callback_data='list_1'),
            InlineKeyboardButton('⇨', callback_data='bully')
       ]])

BULLY_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⇦', callback_data='advice'),
            InlineKeyboardButton('Back', callback_data='list_1'),
            InlineKeyboardButton('⇨', callback_data='carbon')
       ]])

CARBON_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⇦', callback_data='bully'),
            InlineKeyboardButton('Back', callback_data='list_1'),
            InlineKeyboardButton('⇨', callback_data='dagd')
       ]])


@Client.on_callback_query()
async def cb_data(bot, message):
    if message.data == "help":
        await message.edit_message_text(
          text=HELP_TXT,
          reply_markup=HELP_BTN
        )
    elif message.data == "list_1":
        await message.edit_message_text(
          text=LIST_1_TXT,
          reply_markup=LIST_1_BTN
        )
    elif message.data == "list_2":
        await message.edit_message_text(
          text=LIST_2_TXT,
          reply_markup=LIST_2_BTN
        )
    elif message.data == "list_3":
        await message.edit_message_text(
          text=LIST_3_TXT,
          reply_markup=LIST_3_BTN
        )
        await message.answer('www.hagadmansa.com')
    elif message.data == "list_4":
        await message.edit_message_text(
          text=LIST_4_TXT,
          reply_markup=LIST_4_BTN
        )
    elif message.data == "list_5":
        await message.edit_message_text(
          text=LIST_5_TXT,
          reply_markup=LIST_5_BTN
        )
    elif message.data == "advice":
        await message.edit_message_text(
          text=ADVICE_TXT,
          reply_markup=ADVICE_BTN
        )
    elif message.data == "bully":
        await message.edit_message_text(
          text=BULLY_TXT,
          reply_markup=BULLY_BTN
        )
    elif message.data == "carbon":
        await message.edit_message_text(
          text=CARBON_TXT,
          reply_markup=CARBON_BTN
        )
      
@Client.on_message(filters.command("hp")) 
async def help(client, message):
  
    await message.reply_photo(
      photo="https://telegra.ph/file/ebba73e063dac600db5d0.jpg",
      caption=HELP_TXT,
      reply_markup=HELP_BTN
    )
