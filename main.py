import pytz
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import MessageIdInvalid
from pyrogram.errors import FloodWait
 
from pyrogram.types import ChatPermissions
 
import time
from time import sleep
import random

api_id = 29428185
api_hash = "2297b20af7fccd425f4e51eadc9dfc1b"

import asyncio
from datetime import datetime


with Client ("session", api_id, api_hash) as app:
    app.send_message("me", '.time' )

app = Client("session", api_id, api_hash)



@app.on_message(filters.command('info', prefixes='.') & filters.me)
async def info(app, msg: Message):
    await msg.delete()
    await app.send_message(text=f'<b>Info:\n\n- ID: {msg.from_user.id}\n- Chat_ID: {msg.chat.id}</b>',
                           chat_id=msg.chat.id)

@app.on_message(filters.command('mama', prefixes='.') & filters.me)
async def info(app,msg: Message):
    lst = ['❤️','🤍','🧡','💛','💚','💙','💜','🖤','🤎','💖','💝']
    serf = random.choice(lst)   
    serff = random.choice(lst)   
    await asyncio.sleep(1)
    await msg.edit( 'i')
    await asyncio.sleep(1)
    await msg.edit( 'i love')
    await asyncio.sleep(1)
    await msg.edit( 'i love you')
    await asyncio.sleep(1)
    await msg.edit(text=f'<b>i love you mubina  {serf} </b>')
    await asyncio.sleep(1)
    await msg.edit( text=f'<b>i love you mubina  {serff} </b>') 
@app.on_message(filters.command('time', prefixes='.') & filters.me)
async def time_bot(app, msg: Message):
    tz_NY = pytz.timezone('Asia/Tashkent')
    datetime_NY = datetime.now(tz_NY)
    while True:
        await asyncio.sleep(0.1)
        await msg.edit('<b>Запущен!</b>')
        while True:
            await asyncio.sleep(60)
            #count = await app.get_chat_members_count(chat_id= -1001622920699)
            tz_NY = pytz.timezone('Asia/Tashkent')
            datetime_NY = datetime.now(tz_NY)
            
            await app.update_profile(last_name=f"{datetime_NY.strftime('%H:%M')}")

asyncio.run(app.run())