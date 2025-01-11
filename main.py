from aiogram import Bot, Dispatcher, executor, types
from decouple import config
import logging
import os

token = config('TOKEN')
bot = Bot(token=token)
dp = Dispatcher(bot=bot)
admins = [5576961334]

async def on_startup(_):
    for admin in admins:
        await bot.send_message(chat_id=admin, text="Bot started")

async def on_shutdown(_):
    for admin in admins:
        await bot.send_message(chat_id=admin, text="Bot stopped")


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=f"Hello {message.from_user.first_name}!\n"
                                                              f"Your telegram ID: {message.from_user.id}" )

    await message.answer('Привет!')


@dp.message_handler(commands=['mem'])
async def mem_handler(message: types.Message):
    photo_path = os.path.join('media', 'img.png')

    with open(photo_path, 'rb') as photo:
        await bot.send_photo(chat_id=message.from_user.id, photo=photo, caption="It's a mem")

        await message.answer_photo(photo=photo, caption="Mem")


@dp.message_handler()
async def echo_handler(message: types.Message):
    text = message.text
    if text.isdigit():
        text_to_number = int(text) * 2
        await message.answer(str(text_to_number))
    else:
        await message.answer(message.text)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)


