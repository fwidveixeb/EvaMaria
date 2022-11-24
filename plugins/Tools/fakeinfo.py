import os
import random 
import requests
from pyrogram import Client, filters

@Client.on_message(filters.command("fakeinfo"))
async def fakeinfo(bot, message):
  
  id = message.chat.id
  m = await message.reply("`Processing...`")
  API = "https://api.safone.me/fakeinfo?gender=anything"
  k = requests.get(f"{API}").json()
    
  #Personal Details
  name = k['name']
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
  #Mobile
  ios = k['iosuserAgent']
  mob = [android, ios]
  mobile = random.choice(mob)
  #Computer
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
  
  URL = "https://thispersondoesnotexist.com/image"
  response = requests.get(URL)
  open(f"fakeinfo_{id}.jpg", "wb").write(response.content)
  
  await message.reply_photo(photo=f"fakeinfo_{id}.jpg", caption=output)
  await m.delete()
  os.remove(f"fakeinfo_{id}.jpg")
  
