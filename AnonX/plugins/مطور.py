import asyncio


import random
from AnonX import app
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from strings.filters import command
from pyrogram import filters, Client
import config



txt = [

            "تعاال يامطووري يبووك @A_S_A_S_K 🥺❤",


             "هذا مطوري @A_S_A_S_K🥺❤",
            

             "المزعجين ينادوك @A_S_A_S_K 🙂😒",
            
           
 
            
            

        ]


        


@app.on_message(command(["اليسع","اسحاق","حفيد"]))


async def cutt(client: Client, message: Message):


      a = random.choice(txt)


      await message.reply(


        f"{a}")
