# echo.py

from aiogram import Dispatcher, types


async def echo_handler(message: types.Message):
    text = message.text
    if text.isdigit():
        text_to_number = int(text) * 2
        await message.answer(str(text_to_number))
    else:
        await message.answer(message.text)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(echo_handler)
