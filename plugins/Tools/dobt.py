import os
import pytz
import time
import aiohttp
from datetime import date
from random import choice
from shutil import rmtree
from datetime import datetime as dt
from bs4 import BeautifulSoup as bs
from pyrogram import Client, filters

async def async_searcher(
    url: str,
    post: bool = None,
    headers: dict = None,
    params: dict = None,
    json: dict = None,
    data: dict = None,
    ssl=None,
    re_json: bool = False,
    re_content: bool = False,
    real: bool = False,
    *args,
    **kwargs,
):
    
    async with aiohttp.ClientSession(headers=headers) as client:
        if post:
            data = await client.post(
                url, json=json, data=data, ssl=ssl, *args, **kwargs
            )
        else:
            data = await client.get(url, params=params, ssl=ssl, *args, **kwargs)
        if re_json:
            return await data.json()
        if re_content:
            return await data.read()
        if real:
            return data
        return await data.text()

@Client.on_message(filters.command("dobt"))
async def dob(bot, message):
    
    match = message.text.split()
    today = date.today()
    today_year = today.year
    name = message.from_user.first_name
    dobt = await message.reply("Processing...")
    
    if len(match) == 1:
        return await dobt.edit("No Date Of Birth provided, Read Help Menu to know how command works.")
    
    if len(match) == 2 :
      return await dobt.edit("No Month provided, Read Help Menu to know how command works.")

    if len(match) == 3:
      return await dobt.edit("No Year provided, Read Help Menu to know how command works.")

   if len(match) == 4:
        
      a = match[1]
      d = int(a)
      if d > 31:
        return await dobt.edit(f"**COMMAND:**\n`{message.text}`\n\n**ERROR:**\n`Hagadmansa Says: [126 FIRST_PARAMETER_INVALID] - Date must be in numbers and should not exceed 31. (Caused by 'Parameter.ValueError')`")
      
      b =  match[2]
      m = int(b)
      if m > 12:
        return await dobt.edit(f"**COMMAND:**\n`{message.text}`\n\n**ERROR:**\n`Hagadmansa Says: [128 SECOND_PARAMETER_INVALID] - Month must be in numbers and should not exceed 12. (Caused by 'Parameter.ValueError')`")
     
      
      c =  match[3]
      y = int(c)
      if len(y) != 4:
        return await dobt.edit(f"**COMMAND:**\n`{message.text}`\n\n**ERROR:**\n`Hagadmansa Says: [131 THIRD_PARAMETER_INVALID] - Year must be in 4 numbers and should not exceed 12. (Caused by 'Parameter.ValueError')`")
        
   if len(match) > 4:
      

    zn = pytz.timezone("Asia/Kolkata")
  abhi = dt.now(zn)
  p = match[1]
  r = match[2]
  s = match[3]
  monu = f"{p}/{r}/{s}"
  print(p)
  print(r)
  print(s)
  print(monu)
  day = int(p)
  month = r
  try:
      jn = dt.strptime(monu, "%d/%m/%Y")  
  except BaseException:
      return await message.reply("something went wrong in line 34")
  jnm = zn.localize(jn)
  zinda = abhi - jnm
  barsh = (zinda.total_seconds()) / (365.242 * 24 * 3600)
  saal = int(barsh)
  mash = (barsh - saal) * 12
  mahina = int(mash)
  divas = (mash - mahina) * (365.242 / 12)
  din = int(divas)
  samay = (divas - din) * 24
  ghanta = int(samay)
  pehl = (samay - ghanta) * 60
  mi = int(pehl)
  sec = (pehl - mi) * 60
  slive = int(sec)
  y = int(s) + int(saal) + 1
  m = int(r)
  brth = dt(y, m, day)
  cm = dt(abhi.year, brth.month, brth.day)
  ish = (cm - abhi.today()).days + 1
  dan = ish
  if dan == 0:
      hp = "`Happy BirthDay To U🎉🎊`"
  elif dan < 0:
      okk = 365 + ish
      hp = f"{okk} Days Left 🥳"
  elif dan > 0:
      hp = f"{ish} Days Left 🥳"
  if month == "12":
      sign = "Sagittarius" if (day < 22) else "Capricorn"
  elif month == "01":
      sign = "Capricorn" if (day < 20) else "Aquarius"
  elif month == "02":
      sign = "Aquarius" if (day < 19) else "Pisces"
  elif month == "03":
      sign = "Pisces" if (day < 21) else "Aries"
  elif month == "04":
      sign = "Aries" if (day < 20) else "Taurus"
  elif month == "05":
      sign = "Taurus" if (day < 21) else "Gemini"
  elif month == "06":
      sign = "Gemini" if (day < 21) else "Cancer"
  elif month == "07":
      sign = "Cancer" if (day < 23) else "Leo"
  elif month == "08":
      sign = "Leo" if (day < 23) else "Virgo"
  elif month == "09":
      sign = "Virgo" if (day < 23) else "Libra"
  elif month == "10":
      sign = "Libra" if (day < 23) else "Scorpion"
  elif month == "11":
      sign = "Scorpio" if (day < 22) else "Sagittarius"
  json = await async_searcher(
      f"https://aztro.sameerkumar.website/?sign={sign}&day=today",
      post=True,
      re_json=True,
  )
  dd = json.get("current_date")
  ds = json.get("description")
  lt = json.get("lucky_time")
  md = json.get("mood")
  cl = json.get("color")
  ln = json.get("lucky_number")
    
  piza = f"""
Name -: {name}
D.O.B -:  {match}
Lived -:  {saal}yr, {mahina}m, {din}d, {ghanta}hr, {mi}min, {slive}sec
Birthday -: {hp}
Zodiac -: {sign}
**Horoscope On {dd} -**
`{ds}`
Lucky Time :-        {lt}
Lucky Number :-   {ln}
Lucky Color :-        {cl}
Mood :-                   {md}"""
    
  await k.edit(piza)
    
