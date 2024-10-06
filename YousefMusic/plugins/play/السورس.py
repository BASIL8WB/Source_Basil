import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from YousefMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from YousefMusic import app
from random import  choice, randint

# 𝐃𝐞𝐩𝐥𝐨𝐲𝐞𝐝 ⛥ 𓏺 H M D .tele_https://t.me/xs_ub
                
@app.on_message(
    command(["سورس","• السورس •"," ","السورس"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://i.ibb.co/yFvyj7C/aw-IRUSRibv-K.jpg",
        caption = f"""<b>  <b>\n<a href="https://t.me/L_K_VV"> ➮ 𝐰𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐒𝐨𝐮𝐫𝐜𝐞 </a></b>""",
reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                         "𝐃𝐞𝐯 𝐒𝐨𝐮𝐫𝐜𝐞", url=f"https://t.me/xs_ub"), 
                 ],[
                   InlineKeyboardButton(
                        "𝐒𝐨𝐮𝐫𝐜𝐞 ", url=f"https://t.me/L_K_VV"),
                ],

            ]

        ),

    )
