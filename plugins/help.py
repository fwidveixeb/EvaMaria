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
**Parameter:** 1, Optional.
**Replied:** (message, text document), Required.

**__Command must be reply to a message or text document.__**

**~ 1st Parameter:**
**1.** Value must be alphabetical, not numerical.
**2.** Pass '`random`' to generate random background.
**3.** Pass a color name to generate custom background.
**4.** Pass '`colorlist`' to get a list of colors.

■ **EXAMPLE:**
**1.** `/carbon`
**2.** `/carbon red`
**3.** `/carbon random`
**4.** `/carbon colorlist`"""

DAGD_TXT = """■ **HELP:** `Da.gd`
 
__Convert a long URL to short.__

■ **USAGE:**
**Parameter:** 1, Required.
**Replied:** Not Required.

**__Command must have a link to short.__**

**~ 1st Parameter:**
**1.** URL must start with http:// or https://.

■ **EXAMPLE:**
**1.** `/dagd https://1.1.1.1`
**2.** `/dagd https://hagadmansa.com`"""

DARE_TXT = """■ **HELP:** `Dare`

__Get a random Dare.__

■ **USAGE:**
**Parameter:** Not required.
**Replied:** Not required.

■ **EXAMPLE:**
**1. **`/dare`"""

DECIDE_TXT = """■ **HELP:** `Decide`

__Decide, to be Yes or No?__

■ **USAGE:**
**Parameter:** Not required.
**Replied:** Not required.

■ **EXAMPLE:**
**1. **`/decide`"""

DNS_TXT = """■ **HELP:** `DNS`
 
__Get Domain Name Servers of any website.__

■ **USAGE:**
**Parameter:** 1, Required.
**Replied:** Not Required.

**__Command must have a link to find it's DNS.__**

**~ 1st Parameter:**
**1.** URL must start with http:// or https://.

■ **EXAMPLE:**
**1.** `/dns https://hagadmansa.com`"""

DOB_TXT = """■ **HELP:** `D.O.B.`
 
__Find how much days remaining in your birthday, your exact age, your zodiac and Horoscope too.__

■ **USAGE:**
**Parameter:** 3, Required.
**Replied:** Not Required.

**__Command must have a date of birth in 3 parameters.__**

**~ 1st Parameter:**
**1.** Value must be numerical, not alphabetical.
**2.** Date must be a combination of 2 numbers and should not exceed 31.

**~ 2nd Parameter:**
**1.** Value must be numerical, not alphabetical.
**2.** Month must be a combination of 2 numbers and should not exceed 12.

**~ 3rd Parameter:**
**1.** Value must be numerical, not alphabetical.
**2.** Year must be a combination of 4 numbers.

■ **EXAMPLE:**
**1.** `/dob 01 01 2001`"""

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
            InlineKeyboardButton('Da.gd', callback_data='dagd')
            ],[
            InlineKeyboardButton('Dare', callback_data='dare'),
            InlineKeyboardButton('Decide', callback_data='decide')
            ],[
            InlineKeyboardButton('DNS', callback_data='dns'),
            InlineKeyboardButton('D.O.B.', callback_data='dob')
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

DAGD_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⇦', callback_data='carbon'),
            InlineKeyboardButton('Back', callback_data='list_1'),
            InlineKeyboardButton('⇨', callback_data='dare')
       ]])

DARE_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⇦', callback_data='dagd'),
            InlineKeyboardButton('Back', callback_data='list_1'),
            InlineKeyboardButton('⇨', callback_data='decide')
       ]])

DECIDE_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⇦', callback_data='dare'),
            InlineKeyboardButton('Back', callback_data='list_1'),
            InlineKeyboardButton('⇨', callback_data='dns')
       ]])

DNS_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⇦', callback_data='decide'),
            InlineKeyboardButton('Back', callback_data='list_1'),
            InlineKeyboardButton('⇨', callback_data='dob')
       ]])

DOB_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⇦', callback_data='dns'),
            InlineKeyboardButton('Back', callback_data='list_1'),
            InlineKeyboardButton('⇨', callback_data='doc')
       ]])


@Client.on_callback_query()
async def cb_data(bot, message):
    if message.data == "help":
        await message.edit_message_text(
          text=HELP_TXT,
          reply_markup=HELP_BTN
        )
        await message.answer('www.hagadmansa.com')
    elif message.data == "list_1":
        await message.edit_message_text(
          text=LIST_1_TXT,
          reply_markup=LIST_1_BTN
        )
        await message.answer('www.hagadmansa.com')
    elif message.data == "list_2":
        await message.edit_message_text(
          text=LIST_2_TXT,
          reply_markup=LIST_2_BTN
        )
        await message.answer('www.hagadmansa.com')
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
        await message.answer('www.hagadmansa.com')
    elif message.data == "list_5":
        await message.edit_message_text(
          text=LIST_5_TXT,
          reply_markup=LIST_5_BTN
        )
        await message.answer('www.hagadmansa.com')
    elif message.data == "advice":
        await message.edit_message_text(
          text=ADVICE_TXT,
          reply_markup=ADVICE_BTN
        )
        await message.answer('www.hagadmansa.com')
    elif message.data == "bully":
        await message.edit_message_text(
          text=BULLY_TXT,
          reply_markup=BULLY_BTN
        )
        await message.answer('www.hagadmansa.com')
    elif message.data == "carbon":
        await message.edit_message_text(
          text=CARBON_TXT,
          reply_markup=CARBON_BTN
        )
        await message.answer('www.hagadmansa.com')
    elif message.data == "dagd":
        await message.edit_message_text(
          text=DAGD_TXT,
          reply_markup=DAGD_BTN
        )
        await message.answer('www.hagadmansa.com')
    elif message.data == "dare":
        await message.edit_message_text(
          text=DARE_TXT,
          reply_markup=DARE_BTN
        )
        await message.answer('www.hagadmansa.com')
    elif message.data == "decide":
        await message.edit_message_text(
          text=DECIDE_TXT,
          reply_markup=DECIDE_BTN
        )
        await message.answer('www.hagadmansa.com')
    elif message.data == "dns":
        await message.edit_message_text(
          text=DNS_TXT,
          reply_markup=DNS_BTN
        )
        await message.answer('www.hagadmansa.com')
    elif message.data == "dob":
        await message.edit_message_text(
          text=DOB_TXT,
          reply_markup=DOB_BTN
        )
        await message.answer('www.hagadmansa.com')
      
@Client.on_message(filters.command("hp")) 
async def help(client, message):
  
    await message.reply_photo(
      photo="https://telegra.ph/file/ebba73e063dac600db5d0.jpg",
      caption=HELP_TXT,
      reply_markup=HELP_BTN
    )
