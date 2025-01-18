# webapp.py

from aiogram import types, Dispatcher

async def reply_webapp(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4  )
    twitch = types.InlineKeyboardButton("Twitch", web_app=types.WebAppInfo(url="https://www.twitch.tv/"))

    youtube = types.InlineKeyboardButton("Youtube", web_app=types.WebAppInfo(url="https://www.youtube.com/"))

    github = types.InlineKeyboardButton("Github", web_app=types.WebAppInfo(url="https://github.com/"))

    netflix = types.InlineKeyboardButton("Netflix", web_app=types.WebAppInfo(url="https://www.netflix.com/"))

    keyboard.add(twitch, youtube, github, netflix)

    await message.answer("Choose a website", reply_markup=keyboard)

async def inline_webapp(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(row_width=4)

    spotify = types.InlineKeyboardButton("Spotify", web_app=types.WebAppInfo(url="https://www.spotify.com/"))

    jutsu = types.InlineKeyboardButton("Jutsu", web_app=types.WebAppInfo(url="https://jutsu.app/"))

    kinocrad = types.InlineKeyboardButton("Kinocrad", web_app=types.WebAppInfo(url="https://kinocrad.com/"))

    os_kg = types.InlineKeyboardButton("OS.KG", web_app=types.WebAppInfo(url="https://os.kg/"))

    geeks_online = types.InlineKeyboardButton("Geeks Online", web_app=types.WebAppInfo(url="https://geeks.online/"))

    keyboard.add(spotify, jutsu, kinocrad, os_kg)

    await message.answer("Choose a website", reply_markup=keyboard)

def register_handlers_webapp(dp: Dispatcher):
    dp.register_message_handler(reply_webapp, commands=["reply_webapp"])
    dp.register_message_handler(inline_webapp, commands=["inline_webapp"])