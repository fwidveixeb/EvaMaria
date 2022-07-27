import os
import pytz
import time
import pyaztro
import aiohttp
from datetime import date
from random import choice
from shutil import rmtree
from datetime import datetime as dt
from bs4 import BeautifulSoup as bs
from pyrogram import Client, filters

@Client.on_message(filters.command("dobt"))
async def dobt(bot, message):
    
    #Declairing Some Important Variables
    match = message.text.split()
    today = date.today()
    today_year = today.year
    name = message.from_user.first_name
    dobt = await message.reply("`Processing...`")
    
    #Checking if Message has no Parameters
    if len(match) == 1:
        return await dobt.edit("No Date Of Birth provided, Read Help Menu to know how command works.")
    
    #Checking if Message has only 1 Parameter
    if len(match) == 2 :
      return await dobt.edit("No Month provided, Read Help Menu to know how command works.")

    #Checking if Message has only 2 Parameter
    if len(match) == 3:
      return await dobt.edit("No Year provided, Read Help Menu to know how command works.")

    #Checking if all Parameters are fullfilled
    if len(match) == 4:
        
      #Checking if Date is wrong
      a = match[1]
      d = int(a)
      if d > 31:
        return await dobt.edit(f"**COMMAND:**\n`{message.text}`\n\n**ERROR:**\n`Hagadmansa Says: [126 FIRST_PARAMETER_INVALID] - Date must be in numbers and should not exceed 31. (Caused by 'Parameter.ValueError')`")
      
      #Checking if Month is wrong
      b =  match[2]
      m = int(b)
      if m > 12:
        return await dobt.edit(f"**COMMAND:**\n`{message.text}`\n\n**ERROR:**\n`Hagadmansa Says: [128 SECOND_PARAMETER_INVALID] - Month must be in numbers and should not exceed 12. (Caused by 'Parameter.ValueError')`")
     
      #Checking if Year is wrong
      c =  match[3]
      y = int(c)
      if len(c) != 4:
        return await dobt.edit(f"**COMMAND:**\n`{message.text}`\n\n**ERROR:**\n`Hagadmansa Says: [131 THIRD_PARAMETER_INVALID] - Year must be in 4 numbers and should not exceed {today_year}. (Caused by 'Parameter.ValueError')`")
        
      #Getting Some Important Variables
      ab = pytz.timezone("Asia/Kolkata")
      abhi = dt.now(ab) 
      full = f"{d}/{m}/{y}"
      
      #Checking If everything is right or not?
      try:
        cd = dt.strptime(full, "%d/%m/%Y")  
      except BaseException:
        return await dobt.edit("Something went wrong in your Date Of Birth, please contact [Support](https://t.me/HagadmansaChat). ")
      
      #Getting Of Year
      abcd = ab.localize(cd)
      zinda = abhi - abcd
      saal = (zinda.total_seconds()) / (365.242 * 24 * 3600)
      year = int(saal)
      #Getting Of Month
      mahina = (saal - year) * 12
      month = int(mahina)
      #Getting Of Day
      din = (mahina - month) * (365.242 / 12)
      day = int(din)
      #Getting Of Hour
      ghanta = (din - day) * 24
      hour = int(ghanta)
      #Getting Of Minute
      mint = (ghanta - hour) * 60
      minute = int(mint)
      #Getting Of Second
      sec = (mint - minute) * 60
      second = int(sec)
      
      #Getting Some Important Variables
      yr = y + int(year) + 1
      brth = dt(yr, m, d)
      cm = dt(abhi.year, brth.month, brth.day)
      ish = (cm - abhi.today()).days + 1
      dan = ish
      lived = f"{year} Year, {month} Month, {day} Days, {hour} Hour, {minute} Minute, {second} Second"
        
      #Finding Days left in Birthday
      if dan == 0:
          bday = "`Happy BirthDay To You🎉🎊`"
      elif dan < 0:
          okk = 365 + ish
          bday = f"{okk} Days Left 🥳"
      elif dan > 0:
          bday = f"{ish} Days Left 🥳"
        
      #Determining Zodiac
      if m == "12":
          zodiac = "Sagittarius" if (d < 22) else "Capricorn"
      elif m == "01":
          zodiac = "Capricorn" if (d < 20) else "Aquarius"
      elif m == "02":
          zodiac = "Aquarius" if (d < 19) else "Pisces"
      elif m == "03":
          zodiac = "Pisces" if (d < 21) else "Aries"
      elif m == "04":
          zodiac = "Aries" if (d < 20) else "Taurus"
      elif m == "05":
          zodiac = "Taurus" if (d < 21) else "Gemini"
      elif m == "06":
          zodiac = "Gemini" if (d < 21) else "Cancer"
      elif m == "07":
          zodiac = "Cancer" if (d < 23) else "Leo"
      elif m == "08":
          zodiac = "Leo" if (d < 23) else "Virgo"
      elif m == "09":
          zodiac = "Virgo" if (d < 23) else "Libra"
      elif m == "10":
          zodiac = "Libra" if (d < 23) else "Scorpion"
      elif m == "11":
          zodiac = "Scorpio" if (d < 22) else "Sagittarius"
    
      #Getting Horoscope
      horoscope = pyaztro.Aztro(sign='Virgo')
      description = horoscope.description
      today_date = horoscope.current_date
        
      #Creating Final output that would be sent to user
      output = f"**Name:** `{name}`\n**D.O.B:** `{full}`\n**Life Lived:** `{lived}`\n**Upcoming Birthday:** `{bday}`\n**Zodiac:** `{zodiac}`\n\n**Horoscope on `{today_date}:`**\n`{description}`"
        
      #Sendind Data to the User
      return await dobt.edit(output)
    
    if len(match) > 4:
      await dobt.edit("Argument limit exceeded, Read Help Menu to know how command works.")
    
    
