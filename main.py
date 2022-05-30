from pyrogram import Client


TextBot = Client(
    "TextBot",
    api_hash="5820bc246505e0ff60af5391d649f9a6",
    api_id="8406611",
    bot_token="5302212624:AAE6L5B65dYqfyZdKACnkr8X7wJrgFd4SBk",
    plugins=dict(root="TextBot")
)

TextBot.run()
