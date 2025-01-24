# send_products.py

from  aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from db import main_db



async def start_send_products(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    button_all = types.InlineKeyboardButton("All", callback_data="send_all_products")
    button_one = types.InlineKeyboardButton("One", callback_data="send_one_product")
    keyboard.add(button_all, button_one)

    await message.answer("Choose what you want to send", reply_markup=keyboard)

async def send_all_products(call: types.CallbackQuery):
    products = main_db.fetch_all_products()

    if products:
        for product in products:
            caption = (f"Product ID: {product['product_id']}\n"
            f"Product Name: {product['product_name']}\n"
            f"Product Size: {product['product_size']}\n"
            f"Product Category: {product['product_category']}\n"
            f"Product Collection: {product['collection']}\n"
            f"Product Info: {product['product_info']}\n"
            f"Product Price: {product['product_price']}")

            await call.message.answer_photo(photo=product['product_photo'], caption=caption)

    else:
        await call.message.answer("No products found")

def register_handlers_delete_products(dp: Dispatcher):
    dp.register_message_handler(start_send_products, commands=["send_products"])
    dp.register_callback_query_handler(send_all_products, Text(equals="send_all_products"))