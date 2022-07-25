import os
import random 
import requests
from pyrogram import Client, filters

@Client.on_message(filters.command("fakeinfo"))
async def fakeinfo(bot, message):
  if (message.command):
    query = message.command[1]
    m = await message.reply("Generating Fake Information...")
    API = "https://api.safone.tech/fakeinfo?gender="
    k = requests.get(f"{API}{query}").json()
    
    #Personal Details
    name = k['name']
    photo = k['picture']
    dob = k['dateofBirth']
    number = k['phoneNumber']
    email = k['emailAddress']
    cc = k['creditCard']
    address = k['address']
    country = k['country']
    
    #Device Details
    browser = k['browser']
    ip = k['ipAddress']
    mac = k['macAddress']
    android = k['androiduserAgent']
    ios = k['iosuserAgent']
    mob = [android, ios]
    mobile = random.choice(mob)
    linux = k['linuxuserAgent']
    windows = k['windowsuserAgent']
    com = [linux, windows]
    computer = random.choice(com)
   
    #Work Details
    profession = k['profession']
    company = k['company']
    
    output = f"""**PERSONAL DETAIL**
**Name:** `{name}`
**Date Of Birth:** `{dob}`
**Phone Number:** `{number}`
**Email Address:** `{email}`
**Credit Card:** `{cc}`
**Address:** `{address}, {country}`
    
**DEVICE DETAIL**
**Browser:** `{browser}`
**IP Address:** `{ip}`
**Mac Address:** `{mac}`
**Mobile:** `{mobile}`
**Computer:** `{computer}`
    
**WORK DETAIL**
**Profession:** `{profession}`
**Company:** `{company}`"""
    
    await m.delete()
    await message.reply_photo(
      photo=photo,
      caption=output
    )
    
@Client.on_message(filters.command("this"))
async def thisperson(bot, message):
  b = requests.get("https://thispersondoesnotexist.com/image").save("random.jpg")
  await message.reply_photo(b)
  os.remove("random.jpg")
  
