"""
TikTok DL Bot
© All rights reserved by X-Gorn
Kangers don't f*ckin kang this !!!
Should have to give credits 😏 else f***off
"""
from main import *
import json, requests, os, shlex, asyncio, uuid, shutil
from typing import Tuple
from pyrogram import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

# Configs
API_HASH = "6cc6449dcef22f608af2cf7efb76c99d"
API_ID = 2345226
#BOT_TOKEN = "5277895733:AAE4ZUdXauqDkerpV4oW9kEyL7ZfQ4beEbk"
BOT_TOKEN="5735001878:AAG-a2CEBQWBCsAKpLlxsa03Zq8vJpWRXYs"
downloads = './downloads/{}/'

#Button
START_BUTTONS=[
    [
        InlineKeyboardButton("Source", url="https://t.me/madewgn"),
        InlineKeyboardButton("Project Channel", url="https://madewgn.my.id"),
    ],
    [InlineKeyboardButton("Author", url="https://t.me/madewgn")],
]


# Running bot
xbot = Client('InstaDL',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN)

# Helpers
# Thanks to FridayUB

# Start
@xbot.on_message(filters.command('start') & filters.private)
async def start(bot, update):
  await update.reply("Halo, Saya IGMD! \nKamu dapat mendownload foto, video, maupun reels dari Instagram. Cukup pastekan link dan kirim.")

# Downloader for tiktok
@xbot.on_message(filters.regex(pattern='.*http.*') & filters.private)
async def insta(bot, update):
    print("start cmd")
    url = update.text
    if not 'instagram.com' in url:
        return ":)"
    else:
        dirs = downloads.format(uuid.uuid4().hex)
        os.makedirs(dirs)
        url = update.text
        tes = cek(url)
        if tes == "GraphSidecar":
            #result = dl(url)
            result = dl(url)
#            cak = acak()

            r = requests.get(result, allow_redirects=True)
            if ".mp4" in result:
                cak = acak()
                open(f'{cak}.mp4', 'wb').write(r.content)
                print("dl berhasil otw upload")
                await bot.send_video(update.chat.id, f'{cak}.mp4',)
                os.remove(f"{cak}.mp4")
            else:
                print("gambar")
                for x in result:
                    r = requests.get(x, allow_redirects=True)
                    cak = acak()
                    open(f'{cak}.jpg', 'wb').write(r.content)
                    await bot.send_photo(update.chat.id, f'{cak}.jpg',)
                    os.remove(f"{cak}.jpg")
#  await update.reply('Select the options below', True, reply_markup=InlineKeyboardMarkup(DL_BUTTONS))

print("bot aktif!")
xbot.run()
