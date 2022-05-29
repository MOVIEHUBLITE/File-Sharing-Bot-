from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from variables import STAT_STICK, PICS, ADMIN, DELAY
import asyncio
import random


Text = 


@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
 await message.reply_text("Helo iam Youtube Video Search\nUse in inline mode")
 
