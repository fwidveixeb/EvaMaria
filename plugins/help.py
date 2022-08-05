import asyncio
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

__Get a dare to play with your friends & family.__

■ **USAGE:**
**Parameter:** Not required.
**Replied:** Not required.

■ **EXAMPLE:**
**1.** `/dare`"""

DECIDE_TXT = """■ **HELP:** `Decide`

__Decide, to be Yes or No?__

■ **USAGE:**
**Parameter:** Not required.
**Replied:** Not required.

■ **EXAMPLE:**
**1.** `/decide`"""

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

DOC_TXT = """■ **HELP:** `Doc`
 
__Convert your text into files.__

■ **USAGE:**
**Parameter:** 1, Required.
**Replied:** (Message), Required

**__Command must be reply to a message.__**

**~ 1st Parameter:**
**1.** File name must be alphabetical, numerical.
**2.** File name must end with a text file extension such as '`.txt`', '`.py`'.

■ **EXAMPLE:**
**1.** `/doc hagadmansa.txt`"""

FACT_TXT = """■ **HELP:** `Fact`

__Get a random Fact.__

■ **USAGE:**
**Parameter:** Not required.
**Replied:** Not required.

■ **EXAMPLE:**
**1.** `/fact`"""

FAKEINFO_TXT = """■ **HELP:** `Fake Information`

__Get fake information about a person.__

■ **USAGE:**
**Parameter:** Not required.
**Replied:** Not required.

■ **EXAMPLE:**
**1.** `/fakeinfo`"""

FILESTORE_TXT = """■ **HELP:** `File Store`

__Get a link to access files available on Telegram.__

■ **USAGE:**
**Parameter:** Not required.
**Replied:** (video, audio, document), Required.

**__Command must be reply to a video, audio or document.__**

■ **EXAMPLE:**
**1.** `/filestore`"""

FILESTREAM_TXT = """■ **HELP:** `File Stream`

__Get Direct Download Links of files to download it outside of Telegram.__

■ **USAGE:**
**Parameter:** Not required.
**Replied:** (video, audio, document), Required.

**__Command must be reply to a video, audio or document.__**

■ **EXAMPLE:**
**1.** `/filestream`"""

GITHUB_TXT = """■ **HELP:** `Github`
 
__Get Github users details.__

■ **USAGE:**
**Parameter:** 1, Required.
**Replied:** Not Required.

**__Command must have a valid username to find it's details.__**

**~ 1st Parameter:**
**1.** Value should be alphabetical, not numerical.
**2.** Value must be a valid github username.

■ **EXAMPLE:**
**1.** `/github hagadmansa`"""

GLITCH_TXT = """■ **HELP:** `Glitch`
 
__Convert a photo to glitchy GIF.__

■ **USAGE:**
**Parameter:** Not Required
**Replied:** (Photo), Required.

**__Command must be reply to a photo.__**

■ **EXAMPLE:**
**1.** `/glitch`"""

HEX_TXT = """■ **HELP:** `Hex Color`
 
__Get a image of color codes.__

■ **USAGE:**
**Parameter:** 1, Required
**Replied:** Not Required.

**__Command must have a valid color code.__**

**~ 1st Parameter:**
**1.** Code must be a combination of 6 alphabets and numericals.

■ **EXAMPLE:**
**1.** `/hex 7FFFD4`"""

HOST_TXT = """■ **HELP:** `Host`
 
__Find on which IP Address a website is hosting?__

■ **USAGE:**
**Parameter:** 1, Required.
**Replied:** Not Required.

**__Command must have a link to find it's Host.__**

**~ 1st Parameter:**
**1.** URL must start with http:// or https://.
**2.** Value must be a valid URL.

■ **EXAMPLE:**
**1.** `/host https://hagadmansa.com`"""

IMG_TXT = """■ **HELP:** `Google Image`
 
__Search Images on Google.__

■ **USAGE:**
**Parameter:** 1, Required.
**Replied:** Not Required.

**__Command must have a query to search.__**

■ **EXAMPLE:**
**1.** `/img hagadmansa`"""

INFO_TXT = """■ **HELP:** `User Info`
 
__Get details about your Telegram Account.__

■ **USAGE:**
**Parameter:** Not Required.
**Replied:** Not Required.

■ **EXAMPLE:**
**1.** `/info`"""

IP_TXT = """■ **HELP:** `IP Address`
 
__Get details about your IP Address.__

■ **USAGE:**
**Parameter:** 1, Required.
**Replied:** Not Required.

**__Command must have a valid IP Address to get it's details.__**

**~ 1st Parameter:**
**1.** Value must be numerical, not alphabetical.
**2.** Value must be a valid IP Address.

■ **EXAMPLE:**
**1.** `/ip 103.81.26.122`"""

JOKE_TXT = """■ **HELP:** `Joke`

__Get a random Joke.__

■ **USAGE:**
**Parameter:** Not required.
**Replied:** Not required.

■ **EXAMPLE:**
**1.** `/joke`"""

MEANING_TXT = """■ **HELP:** `Meaning`
 
__Find meaning of a word.__

■ **USAGE:**
**Parameter:** 1, Required.
**Replied:** Not Required.

**__Command must have a query to search it's meaning.__**

**~ 1st Parameter:**
**1.** Value must be alphabetical., not numerical.

■ **EXAMPLE:**
**1.** `/meaning help`"""

NCODE_TXT = """■ **HELP:** `Ncode`
 
__Convert your text to images.__

■ **USAGE:**
**Parameter:** Not Required.
**Replied:** (message, text document), Required.

**__Command must be reply to a message or text document.__**

■ **EXAMPLE:**
**1.** `/ncode`"""

NEKOBIN_TXT = """■ **HELP:** `Nekobin`
 
__Upload given text to Nekobin.__

■ **USAGE:**
**Parameter:** Not Required.
**Replied:** (message, text document), Required.

**__Command must be reply to a message or text document.__**

■ **EXAMPLE:**
**1.** `/nekobin`"""

PEXELS_TXT = """■ **HELP:** `Pexels`
 
__Get Images from Pexels.com.__

■ **USAGE:**
**Parameter:** 1, Required.
**Replied:** Not Required.

**__Command must have a query to get images.__**

■ **EXAMPLE:**
**1.** `/pexels cat`
**2.** `/pexels mountain`"""

PHLOGO_TXT = """■ **HELP:** `Pornhub Logo`
 
__Genarate a logo like Pornhub.__

■ **USAGE:**
**Parameter:** 2, Required.
**Replied:** Not Required.

**__Command must have a name and sirname to generate logo.__**

■ **EXAMPLE:**
**1.** `/phlogo Hello moto`
**2.** `/phlogo Ankit Kumar`"""

PICSUM_TXT = """■ **HELP:** `Picsum`
 
__Get random images according to your size.__

■ **USAGE:**
**Parameter:** 2, Required; 1, Optional.
**Replied:** Not Required.

**__Command must have height and width to get image.__**

**~ 1st Parameter:**
**1.** Value must be numerical, not alphabetical.
**2.** Height must be in multiple of 100 and should not exceed 5000.

**~ 2nd Parameter:**
**1.** Value must be numerical, not alphabetical.
**2.** Width must be in multiple of 100 and should not exceed 5000.

**~ 3rd Parameter:**
**1.** Pass '`Blur`' to get a blurred image.
**2.** Pass '`Grey`' to get a grayscale image.

■ **EXAMPLE:**
**1.** `/picsum 500 1000`
**1.** `/picsum 2000 3000`
**1.** `/picsum 1200 1800 Blur`
**1.** `/picsum 2500 1500 Gray`"""

QRCODE_TXT = """■ **HELP:** `QR Generator`
 
__Genarate a QR Code of given text.__

■ **USAGE:**
**Parameter:** Required.
**Replied:** Not Required.

**__Command must have some text to make QR Code of.__**

■ **EXAMPLE:**
**1.** `/qrcode https://hagadmansa.com`
**2.** `/qrcode Hello my name is {your name here}.`"""

QUOTE_TXT = """■ **HELP:** `Quote`

__Get a random Quotes.__

■ **USAGE:**
**Parameter:** Not required.
**Replied:** Not required.

■ **EXAMPLE:**
**1.** `/quote`"""

RMBG_TXT = """■ **HELP:** `Remove Background`
 
__Remove background of any image.__

■ **USAGE:**
**Parameter:** Not Required.
**Replied:** (photo), Required.

**__Command must be replied to a photo to remove background.__**

■ **EXAMPLE:**
**1.** `/rmbg`"""

SPACEBIN_TXT = """■ **HELP:** `Spacebin`
 
__Upload given text to Spacebin.__

■ **USAGE:**
**Parameter:** Not Required.
**Replied:** (message, text document), Required.

**__Command must be reply to a message or text document.__**

■ **EXAMPLE:**
**1.** `/spacebin`"""

TELEGRAPH_TXT = """■ **HELP:** `Telegrph`
 
__Upload message, photo, video, animation, text document to Telegraph.__

■ **USAGE:**
**Parameter:** Optional.
**Replied:** (message, photo, video, animation, text document), Required.

**__Command must be reply to a message, photo, video, animation or text document.__**

**~ 1st Parameter:**
**1.** While replying to a message or text document, you can paas a custom alias.

■ **EXAMPLE:**
**1.** `/telegraph`
**2.** `/telegraph Hello this is a Telegraph.`"""

TPDNE_TXT = """■ **HELP:** `This Person Does Not Exist`

__Get a random image of person that does not exist.__

■ **USAGE:**
**Parameter:** Not required.
**Replied:** Not required.

■ **EXAMPLE:**
**1. **`/tpdne`"""

TRUTH_TXT = """■ **HELP:** `Truth`

__Get a truth to play with your friends & family.__

■ **USAGE:**
**Parameter:** Not required.
**Replied:** Not required.

■ **EXAMPLE:**
**1. **`/truth`"""

UD_TXT = """■ **HELP:** `Urban Dictionary`
 
__Search words on Urban Dictionary.__

■ **USAGE:**
**Parameter:** 1, Required.
**Replied:** Not Required.

**__Command must have a query to search on Urban Dictionary.__**

**~ 1st Parameter:**
**1.** Value must be alphabetical., not numerical.

■ **EXAMPLE:**
**1.** `/ud help`"""

WHOIS_TXT = """■ **HELP:** `WHOIS`
 
__Check website's WHOIS details.__

■ **USAGE:**
**Parameter:** 1, Required.
**Replied:** Not Required.

**__Command must have a link to get WHOIS details.__**

**~ 1st Parameter:**
**1.** URL must start with http:// or https://.

■ **EXAMPLE:**
**1.** `/whois https://hagadmansa.com`"""

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
            InlineKeyboardButton('carbon', callback_data='carbon'),
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
            InlineKeyboardButton('Doc', callback_data='doc'),
            InlineKeyboardButton('Fact', callback_data='fact')
            ],[
            InlineKeyboardButton('Fake Info', callback_data='fakeinfo'),
            InlineKeyboardButton('File Store', callback_data='filestore')
            ],[
            InlineKeyboardButton('File Stream', callback_data='filestream'),
            InlineKeyboardButton('Github', callback_data='github')
            ],[
            InlineKeyboardButton('Glitch', callback_data='glitch'),
            InlineKeyboardButton('Hex Color', callback_data='hex')
            ],[
            InlineKeyboardButton('⇦', callback_data='list_1'),
            InlineKeyboardButton('Home', callback_data='help'),
            InlineKeyboardButton('⇨', callback_data='list_3')
       ]])

LIST_3_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('Host', callback_data='host'),
            InlineKeyboardButton('Google Img', callback_data='img')
            ],[
            InlineKeyboardButton('User Info', callback_data='info'),
            InlineKeyboardButton('IP Address', callback_data='ip')
            ],[
            InlineKeyboardButton('Joke', callback_data='joke'),
            InlineKeyboardButton('Meaning', callback_data='meaning')
            ],[
            InlineKeyboardButton('Ncode', callback_data='ncode'),
            InlineKeyboardButton('Nekobin', callback_data='nekobin')
            ],[
            InlineKeyboardButton('⇦', callback_data='list_2'),
            InlineKeyboardButton('Home', callback_data='help'),
            InlineKeyboardButton('⇨', callback_data='list_4')
       ]])

LIST_4_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('Pexels', callback_data='pexels'),
            InlineKeyboardButton('PH Logo', callback_data='phlogo')
            ],[
            InlineKeyboardButton('Picsum', callback_data='picsum'),
            InlineKeyboardButton('QR Generator', callback_data='qrcode')
            ],[
            InlineKeyboardButton('Quote', callback_data='quote'),
            InlineKeyboardButton('Remove BG', callback_data='rmbg')
            ],[
            InlineKeyboardButton('Spacebin', callback_data='spacebin'),
            InlineKeyboardButton('Telegraph', callback_data='telegraph')
            ],[
            InlineKeyboardButton('⇦', callback_data='list_3'),
            InlineKeyboardButton('Home', callback_data='help'),
            InlineKeyboardButton('⇨', callback_data='list_5')
       ]])

LIST_5_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('TPDNE', callback_data='tpdne'),
            InlineKeyboardButton('Truth', callback_data='truth')
            ],[
            InlineKeyboardButton('Dictionary', callback_data='ud'),
            InlineKeyboardButton('WHOIS', callback_data='whois')
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

DOC_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⇦', callback_data='dob'),
            InlineKeyboardButton('Back', callback_data='list_2'),
            InlineKeyboardButton('⇨', callback_data='fact')
       ]])

FACT_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⇦', callback_data='doc'),
            InlineKeyboardButton('Back', callback_data='list_2'),
            InlineKeyboardButton('⇨', callback_data='fakeinfo')
       ]])

FAKEINFO_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⇦', callback_data='fact'),
            InlineKeyboardButton('Back', callback_data='list_2'),
            InlineKeyboardButton('⇨', callback_data='filestore')
       ]])

FILESTORE_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⇦', callback_data='fakeinfo'),
            InlineKeyboardButton('Back', callback_data='list_2'),
            InlineKeyboardButton('⇨', callback_data='filestream')
       ]])

FILESTREAM_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⇦', callback_data='filestore'),
            InlineKeyboardButton('Back', callback_data='list_2'),
            InlineKeyboardButton('⇨', callback_data='github')
       ]])

GITHUB_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⇦', callback_data='filestream'),
            InlineKeyboardButton('Back', callback_data='list_2'),
            InlineKeyboardButton('⇨', callback_data='glitch')
       ]])

GLITCH_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⇦', callback_data='github'),
            InlineKeyboardButton('Back', callback_data='list_2'),
            InlineKeyboardButton('⇨', callback_data='hex')
       ]])

HEX_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⇦', callback_data='glitch'),
            InlineKeyboardButton('Back', callback_data='list_2'),
            InlineKeyboardButton('⇨', callback_data='host')
       ]])

HOST_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⇦', callback_data='hex'),
            InlineKeyboardButton('Back', callback_data='list_3'),
            InlineKeyboardButton('⇨', callback_data='img')
       ]])

IMG_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⇦', callback_data='host'),
            InlineKeyboardButton('Back', callback_data='list_3'),
            InlineKeyboardButton('⇨', callback_data='info')
       ]])

INFO_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⇦', callback_data='img'),
            InlineKeyboardButton('Back', callback_data='list_3'),
            InlineKeyboardButton('⇨', callback_data='ip')
       ]])

IP_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⇦', callback_data='info'),
            InlineKeyboardButton('Back', callback_data='list_3'),
            InlineKeyboardButton('⇨', callback_data='joke')
       ]])

JOKE_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⇦', callback_data='ip'),
            InlineKeyboardButton('Back', callback_data='list_3'),
            InlineKeyboardButton('⇨', callback_data='meaning')
       ]])

MEANING_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⇦', callback_data='joke'),
            InlineKeyboardButton('Back', callback_data='list_3'),
            InlineKeyboardButton('⇨', callback_data='ncode')
       ]])

NCODE_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⇦', callback_data='meaning'),
            InlineKeyboardButton('Back', callback_data='list_3'),
            InlineKeyboardButton('⇨', callback_data='nekobin')
       ]])

NEKOBIN_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⇦', callback_data='ncode'),
            InlineKeyboardButton('Back', callback_data='list_3'),
            InlineKeyboardButton('⇨', callback_data='pexels')
       ]])

PEXELS_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⇦', callback_data='nekobin'),
            InlineKeyboardButton('Back', callback_data='list_4'),
            InlineKeyboardButton('⇨', callback_data='phlogo')
       ]])

PHLOGO_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⇦', callback_data='pexels'),
            InlineKeyboardButton('Back', callback_data='list_4'),
            InlineKeyboardButton('⇨', callback_data='picsum')
       ]])

PICSUM_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⇦', callback_data='phlogo'),
            InlineKeyboardButton('Back', callback_data='list_4'),
            InlineKeyboardButton('⇨', callback_data='qrcode')
       ]])

QRCODE_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⇦', callback_data='picsum'),
            InlineKeyboardButton('Back', callback_data='list_4'),
            InlineKeyboardButton('⇨', callback_data='quote')
       ]])

QUOTE_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⇦', callback_data='qrcode'),
            InlineKeyboardButton('Back', callback_data='list_4'),
            InlineKeyboardButton('⇨', callback_data='rmbg')
       ]])

RMBG_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⇦', callback_data='quote'),
            InlineKeyboardButton('Back', callback_data='list_4'),
            InlineKeyboardButton('⇨', callback_data='spacebin')
       ]])

SPACEBIN_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⇦', callback_data='rmbg'),
            InlineKeyboardButton('Back', callback_data='list_4'),
            InlineKeyboardButton('⇨', callback_data='telegraph')
       ]])

TELEGRAPH_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⇦', callback_data='spacebin'),
            InlineKeyboardButton('Back', callback_data='list_4'),
            InlineKeyboardButton('⇨', callback_data='tpdne')
       ]])

TPDNE_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⇦', callback_data='telegraph'),
            InlineKeyboardButton('Back', callback_data='list_5'),
            InlineKeyboardButton('⇨', callback_data='truth')
       ]])

TRUTH_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⇦', callback_data='tpdne'),
            InlineKeyboardButton('Back', callback_data='list_5'),
            InlineKeyboardButton('⇨', callback_data='ud')
       ]])

UD_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⇦', callback_data='truth'),
            InlineKeyboardButton('Back', callback_data='list_5'),
            InlineKeyboardButton('⇨', callback_data='whois')
       ]])

WHOIS_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⇦', callback_data='ud'),
            InlineKeyboardButton('Back', callback_data='list_5'),
            InlineKeyboardButton('⇨', callback_data='advice')
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
    elif message.data == "doc":
        await message.edit_message_text(
          text=DOC_TXT,
          reply_markup=DOC_BTN
        )
        await message.answer('www.hagadmansa.com')
    elif message.data == "fact":
        await message.edit_message_text(
          text=FACT_TXT,
          reply_markup=FACT_BTN
        )
        await message.answer('www.hagadmansa.com')
    elif message.data == "fakeinfo":
        await message.edit_message_text(
          text=FAKEINFO_TXT,
          reply_markup=FAKEINFO_BTN
        )
        await message.answer('www.hagadmansa.com')
    elif message.data == "filestore":
        await message.edit_message_text(
          text=FILESTORE_TXT,
          reply_markup=FILESTORE_BTN
        )
        await message.answer('www.hagadmansa.com')
    elif message.data == "filestream":
        await message.edit_message_text(
          text=FILESTREAM_TXT,
          reply_markup=FILESTREAM_BTN
        )
        await message.answer('www.hagadmansa.com')
    elif message.data == "github":
        await message.edit_message_text(
          text=GITHUB_TXT,
          reply_markup=GITHUB_BTN
        )
        await message.answer('www.hagadmansa.com')
    elif message.data == "glitch":
        await message.edit_message_text(
          text=GLITCH_TXT,
          reply_markup=GLITCH_BTN
        )
        await message.answer('www.hagadmansa.com')
    elif message.data == "hex":
        await message.edit_message_text(
          text=HEX_TXT,
          reply_markup=HEX_BTN
        )
        await message.answer('www.hagadmansa.com')
    elif message.data == "host":
        await message.edit_message_text(
          text=HOST_TXT,
          reply_markup=HOST_BTN
        )
        await message.answer('www.hagadmansa.com')
    elif message.data == "img":
        await message.edit_message_text(
          text=IMG_TXT,
          reply_markup=IMG_BTN
        )
        await message.answer('www.hagadmansa.com')
    elif message.data == "info":
        await message.edit_message_text(
          text=INFO_TXT,
          reply_markup=INFO_BTN
        )
        await message.answer('www.hagadmansa.com')
    elif message.data == "ip":
        await message.edit_message_text(
          text=IP_TXT,
          reply_markup=IP_BTN
        )
        await message.answer('www.hagadmansa.com')
    elif message.data == "joke":
        await message.edit_message_text(
          text=JOKE_TXT,
          reply_markup=JOKE_BTN
        )
        await message.answer('www.hagadmansa.com')
    elif message.data == "meaning":
        await message.edit_message_text(
          text=MEANING_TXT,
          reply_markup=MEANING_BTN
        )
        await message.answer('www.hagadmansa.com')
    elif message.data == "ncode":
        await message.edit_message_text(
          text=NCODE_TXT,
          reply_markup=NCODE_BTN
        )
        await message.answer('www.hagadmansa.com')
    elif message.data == "nekobin":
        await message.edit_message_text(
          text=NEKOBIN_TXT,
          reply_markup=NEKOBIN_BTN
        )
        await message.answer('www.hagadmansa.com')
    elif message.data == "pexels":
        await message.edit_message_text(
          text=PEXELS_TXT,
          reply_markup=PEXELS_BTN
        )
        await message.answer('www.hagadmansa.com')
    elif message.data == "phlogo":
        await message.edit_message_text(
          text=PHLOGO_TXT,
          reply_markup=PHLOGO_BTN
        )
        await message.answer('www.hagadmansa.com')
    elif message.data == "picsum":
        await message.edit_message_text(
          text=PICSUM_TXT,
          reply_markup=PICSUM_BTN
        )
        await message.answer('www.hagadmansa.com')
    elif message.data == "qrcode":
        await message.edit_message_text(
          text=QRCODE_TXT,
          reply_markup=QRCODE_BTN
        )
        await message.answer('www.hagadmansa.com')
    elif message.data == "quote":
        await message.edit_message_text(
          text=QUOTE_TXT,
          reply_markup=QUOTE_BTN
        )
        await message.answer('www.hagadmansa.com')
    elif message.data == "rmbg":
        await message.edit_message_text(
          text=RMBG_TXT,
          reply_markup=RMBG_BTN
        )
        await message.answer('www.hagadmansa.com')
    elif message.data == "spacebin":
        await message.edit_message_text(
          text=SPACEBIN_TXT,
          reply_markup=SPACEBIN_BTN
        )
        await message.answer('www.hagadmansa.com')
    elif message.data == "telegraph":
        await message.edit_message_text(
          text=TELEGRAPH_TXT,
          reply_markup=TELEGRAPH_BTN
        )
        await message.answer('www.hagadmansa.com')
    elif message.data == "tpdne":
        await message.edit_message_text(
          text=TPDNE_TXT,
          reply_markup=TPDNE_BTN
        )
        await message.answer('www.hagadmansa.com')
    elif message.data == "truth":
        await message.edit_message_text(
          text=TRUTH_TXT,
          reply_markup=TRUTH_BTN
        )
        await message.answer('www.hagadmansa.com')
    elif message.data == "ud":
        await message.edit_message_text(
          text=UD_TXT,
          reply_markup=UD_BTN
        )
        await message.answer('www.hagadmansa.com')
    elif message.data == "whois":
        await message.edit_message_text(
          text=WHOIS_TXT,
          reply_markup=WHOIS_BTN
        )
        await message.answer('www.hagadmansa.com')
      
@Client.on_message(filters.command("hp")) 
async def help(client, message):
 
 if len(message.command) == 1:
     await message.reply_photo(
       photo="https://telegra.ph/file/ebba73e063dac600db5d0.jpg",
       caption=HELP_TXT,
       reply_markup=HELP_BTN
     )
 elif message.command[1].lower() == "advice":
     advice = await message.reply("`Processing...`")
     await asyncio.sleep(0.5)
     await advice.edit(ADVICE_TXT)
