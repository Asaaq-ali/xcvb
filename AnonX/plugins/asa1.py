import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnonX import app, Telegram
import random

@app.on_message(
    filters.command(["صورص","السورسس","السورس","سورس", "crs"],"")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg",
        caption=f"""
 [𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂](https://t.me/VVHH9)
 —————————————
 [𝗔𝗦𝗔𝗔𝗤](https://t.me/A_S_A_S_K)
 
 [𓏺𝙂𝙍𝙊𝙐𝙋 𝙃𝞝𝙇𝙋](https://t.me/hasheyy)
  
 [𝙒𝞝𝙇𝘾𝙊𝙈𝙀 𝙏𝙊 𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂](https://t.me/Mlze1bot)
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝗔𝗦𝗔𝗔𝗤", url=f"t.me/A_S_A_S_K"), 
                ],[
                    InlineKeyboardButton(
                        "𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂", url=f"t.me/Mlze1bot"),
                ],

            ]

        ),

    )

@app.on_message(filters.command([f"زومل", "زامل", "عيسى الليث", "{BOT_USERNAME} زامل"],""))
async def ihd(client: Client, message: Message):
    rl = random.randint(8,20)
    url = f"https://t.me/zwamlallaith/{rl}"
    await client.send_voice(message.chat.id,url,caption="`🔥 ¦ تـم اختيـار الزامـــل لـك`",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
    
@app.on_message(filters.command(["صورة","صور"]),"")
async def ihd(client: Client, message: Message):
    rs = random.randint(39,148)
    url = f"https://t.me/GTTUTY/{rs}"
    await client.send_photo(message.chat.id,url,caption="`💕 ¦ تـم اختيـار الصوره لـك`",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

                        


