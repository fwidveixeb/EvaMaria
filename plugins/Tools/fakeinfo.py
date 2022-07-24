import requests
from pyrogram import Client, message

@Client.on_message(filters.command("fakeinfo"))
async def fakeinfo(bot, message):
  if len(message.command) == 1:
    query = message.command[1]
    await message.reply("Generating Fake Information...")
    API = "https://api.safone.tech/fakeinfo?gender="
    k = requests.get(f"{API}{query}").json()
    
    #Personal Details
    name = k['name']
    photo = k['picture']
    dob = k['dateofBirth']
    number = k['phoneNumber']
    email = k['emailAddress']
    cc = k['creditCard']
    postalcode = k['postalCode']
    timezone = ['timeZone']
    address = k['address']
    country = k['country']
    
    #Device Details
    browser = k['browser']
    ip = k['ipAddress']
    mac = k['macAddress']
    password = k['password']
    android = k['androiduserAgent']
    ios = k['iosuserAgent']
    linux = k['linuxuserAgent']
    windows = k['windowsuserAgent']
    
    #Work Details
    profession = k['profession']
    company = k['company']
    
    output = f"""**PERSONAL DETAILS**
    **Name:** `{name}`
    **Date Of Birth:** `{dob}`
    **Phone Number:** `{number}`
    **Email Address:** `{email}`
    **Credit Card:** `{cc}`
    **Postal Code:** `{postalcode}`
    **Time Zone:** `{timezone}`
    **Address:** `{address}, {country}`
    
    **DEVICE DETAIL**
    
   
    
