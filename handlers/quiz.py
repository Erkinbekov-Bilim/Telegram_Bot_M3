# quiz.py

from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot
import os



async def quiz_1(message: types.Message):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    button = InlineKeyboardButton("Next", callback_data="quiz_2")
    keyboard.add(button)

    question = 'PC or Laptop?'

    answer = ['PC', 'Laptop', 'Both']

    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=2,
        explanation="What did you choose? It's horrible",
        open_period=60,
        reply_markup=keyboard
    )


async def quiz_2(call: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    button = InlineKeyboardButton("Next", callback_data="quiz_3")
    keyboard.add(button)

    question = 'Hamburger or Pizza?'

    answer = ['Hamburger', 'Pizza', 'Both']

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=1,
        explanation="Pizza is the best, you know it",
        open_period=60,
        reply_markup=keyboard
    )

async def quiz_3(call: types.CallbackQuery):
    question = 'Shashlik or Kebab?'

    answer = ['Shashlik', 'Kebab', 'Both']

    photo_path = os.path.join('media', 'so_juicy_shashlik.png')

    with open(photo_path, 'rb') as photo:
        await bot.send_photo(chat_id=call.from_user.id, photo=photo, caption="Juicy Shashlik - Sochnyi")


    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=0,
        explanation="Shashlik is the best, you know it",
        open_period=20
    )

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_callback_query_handler(quiz_2, text='quiz_2')
    dp.register_callback_query_handler(quiz_3, text='quiz_3')

