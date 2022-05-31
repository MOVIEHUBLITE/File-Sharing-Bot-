from pyrogram import Client


TextBot = Client(
    "TextBot",
    api_hash="5820bc246505e0ff60af5391d649f9a6",
    api_id="8406611",
    bot_token="5302212624:AAHUi7x_cRvLm8uuYsplXXG5fd3Gjp9wlSc",
    plugins=dict(root="TextBot")
)

TextBot.run()
