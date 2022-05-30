from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from variables import STAT_STICK, PICS, ADMIN, DELAY
import asyncio
import random


WAIT_MSG = """"<b>Processing ...</b>"""



@Client.on_message(filters.private & filters.command("start"))
async def start_message(bot, message):
    insert(int(message.chat.id))
    await message.reply_chat_action("Typing")
    await asyncio.sleep(DELAY)
    m=await message.reply_sticker(STAT_STICK)
    await asyncio.sleep(DELAY)
    await m.delete()             
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=f"Hello {message.from_user.mention}👋🏻\nI'am A Multi use Bot with many usefull features.\neg:- Telegarph, Channel ID, User ID, Fun, Group Id etc...\nYou can see My commands by below button... \n\n◉ send channel last message with forwerd tag to get the channel id 💯",               
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("❣️ 𝐒𝐔𝐏𝐏𝐎𝐑𝐓", url="https://t.me/BETA_BOTSUPPORT"),
            InlineKeyboardButton("📢 𝐔𝐏𝐃𝐀𝐓𝐄𝐒", url="https://t.me/BETA_UPDATES")
            ],[            
            InlineKeyboardButton("ℹ️ 𝐇𝐄𝐋𝐏", callback_data="help"),
            InlineKeyboardButton("😉 𝐅𝐔𝐍", callback_data="fun")
            ],[
            InlineKeyboardButton("👨‍💻 𝐃𝐄𝐕𝐒 👨‍💻 ", callback_data="devs"),
            InlineKeyboardButton("🤖 𝐀𝐁𝐎𝐔𝐓", callback_data="about")
            ]]
            )
        )
         
@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["broadcast"]))
async def broadcast(bot, message):
 if (message.reply_to_message):
   ms = await message.reply_text("Geting All ids from database ...........")
   ids = getid()
   tot = len(ids)
   await ms.edit(f"Starting Broadcast .... \n Sending Message To {tot} Users")
   for id in ids:
     try:
     	await message.reply_to_message.copy(id)
     except:
     	pass


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["users"]))
async def get_users(client: Client, message: Message):    
    msg = await client.send_message(chat_id=message.chat.id, text=WAIT_MSG)
    ids = getid()
    tot = len(ids)
    await msg.edit(f"Total uses = {tot}")





@Client.on_message(filters.private & filters.incoming & filters.text)
async def style_buttons(c, m, cb=False):
    buttons = [[
        InlineKeyboardButton('𝚃𝚢𝚙𝚎𝚠𝚛𝚒𝚝𝚎𝚛', callback_data='style+typewriter'),
        InlineKeyboardButton('𝕆𝕦𝕥𝕝𝕚𝕟𝕖', callback_data='style+outline'),
        InlineKeyboardButton('𝐒𝐞𝐫𝐢𝐟', callback_data='style+serif'),
        ],[
        InlineKeyboardButton('𝑺𝒆𝒓𝒊𝒇', callback_data='style+bold_cool'),
        InlineKeyboardButton('𝑆𝑒𝑟𝑖𝑓', callback_data='style+cool'),
        InlineKeyboardButton('Sᴍᴀʟʟ Cᴀᴘs', callback_data='style+small_cap'),
        ],[
        InlineKeyboardButton('𝓈𝒸𝓇𝒾𝓅𝓉', callback_data='style+script'),
        InlineKeyboardButton('𝓼𝓬𝓻𝓲𝓹𝓽', callback_data='style+script_bolt'),
        InlineKeyboardButton('ᵗⁱⁿʸ', callback_data='style+tiny'),
        ],[
        InlineKeyboardButton('ᑕOᗰIᑕ', callback_data='style+comic'),
        InlineKeyboardButton('𝗦𝗮𝗻𝘀', callback_data='style+sans'),
        InlineKeyboardButton('𝙎𝙖𝙣𝙨', callback_data='style+slant_sans'),
        ],[
        InlineKeyboardButton('𝘚𝘢𝘯𝘴', callback_data='style+slant'),
        InlineKeyboardButton('𝖲𝖺𝗇𝗌', callback_data='style+sim'),
         InlineKeyboardButton('Ⓒ︎Ⓘ︎Ⓡ︎Ⓒ︎Ⓛ︎Ⓔ︎Ⓢ︎', callback_data='style+circles'),
        ],[
        InlineKeyboardButton('🅒︎🅘︎🅡︎🅒︎🅛︎🅔︎🅢︎', callback_data='style+circle_dark'),
        InlineKeyboardButton('𝔊𝔬𝔱𝔥𝔦𝔠', callback_data='style+gothic'),
        InlineKeyboardButton('𝕲𝖔𝖙𝖍𝖎𝖈', callback_data='style+gothic_bolt'),
        ],[
        InlineKeyboardButton('C͜͡l͜͡o͜͡u͜͡d͜͡s͜͡', callback_data='style+cloud'),
        InlineKeyboardButton('H̆̈ă̈p̆̈p̆̈y̆̈', callback_data='style+happy'),
        InlineKeyboardButton('S̑̈ȃ̈d̑̈', callback_data='style+sad'),
        ],[
        InlineKeyboardButton('Next ➡️', callback_data="nxt")
    ]]
    if not cb:
        await m.reply_text(m.text, reply_markup=InlineKeyboardMarkup(buttons), quote=True)
    else:
        await m.answer()
        await m.message.edit_reply_markup(InlineKeyboardMarkup(buttons))

