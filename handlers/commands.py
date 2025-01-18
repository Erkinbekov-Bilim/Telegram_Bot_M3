# commands.py

from aiogram import Dispatcher, types
import os
from config import bot
import random





async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=f"Hello {message.from_user.first_name}!\n"
                                                              f"Your telegram ID: {message.from_user.id}" )

    await message.answer('Привет!')



async def mem_handler(message: types.Message):
    photo_path = os.path.join('media', 'img.png')

    with open(photo_path, 'rb') as photo:
        await bot.send_photo(chat_id=message.from_user.id, photo=photo, caption="It's a mem")

        # await message.answer_photo(photo=photo, caption="Mem")

async def game_handler(message: types.Message):
    games = ['⚽', '🎰', '🏀', '🎯', '🎳', '🎲']

    await bot.send_dice(chat_id=message.from_user.id, emoji=random.choice(games))



def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(mem_handler, commands=['mem'])
    dp.register_message_handler(game_handler, commands=['game'])