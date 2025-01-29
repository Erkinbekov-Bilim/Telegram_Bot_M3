# commands.py

from aiogram import Dispatcher, types
import os
from config import bot
from random import sample





async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=f"Hello {message.from_user.first_name}!\n"
                                                              f"Your telegram ID: {message.from_user.id}" )

    await message.answer('Привет!')



async def mem_handler(message: types.Message):
    photo_path = os.path.join('media', 'img.png')

    with open(photo_path, 'rb') as photo:
        await bot.send_photo(chat_id=message.from_user.id, photo=photo, caption="It's a mem")

        # await message.answer_photo(photo=photo, caption="Mem")

dice_options = ['⚽', '🎰', '🏀', '🎯', '🎳', '🎲']
async def game_handler(message: types.Message):
    selected_dices = sample(dice_options, 3)
    selected_dice = sample(selected_dices, 1)[0]

    bot_message = await bot.send_dice(chat_id=message.chat.id, emoji=selected_dice)
    bot_score = bot_message.dice.value
    print(bot_score)

    user_message = await bot.send_dice(chat_id=message.chat.id, emoji=selected_dice)
    user_score = user_message.dice.value
    print(user_score)

    if bot_score > user_score:
        await message.answer("Bot wins")
    elif bot_score < user_score:
        await message.answer("You win! Congratulations!")
    else:
        await message.answer("It's a draw")



def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(mem_handler, commands=['mem'])
    dp.register_message_handler(game_handler, commands=['game'])