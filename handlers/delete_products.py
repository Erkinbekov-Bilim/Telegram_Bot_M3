# delete_products.py


# send_products.py

from  aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from aiogram.types import InputMediaPhoto

from db import main_db



async def start_send_products(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    button_all = types.InlineKeyboardButton("All", callback_data="delete_all_products")
    button_one = types.InlineKeyboardButton("One", callback_data="delete_one_product")
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

            keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
            delete_button = types.InlineKeyboardButton("Delete", callback_data=f"delete_{product['product_id']}")
            keyboard.add(delete_button)

            await call.message.answer_photo(photo=product['product_photo'], caption=caption, reply_markup=keyboard)

    else:
        await call.message.answer("No products found")

async def delete_all_products(call: types.CallbackQuery):
    product_id = int(call.data.split("_")[1])

    main_db.delete_product(product_id)

    if call.message.photo:
        new_caption = "Product deleted! Please update the list"

        photo_404 = open('media/img_404.png', 'rb')

        await call.message.edit_media(
            InputMediaPhoto(photo_404, caption=new_caption)
        )

    else:
        await call.message.edit_text("Product deleted! Please update the list")






def register_handlers_send_products(dp: Dispatcher):
    dp.register_message_handler(start_send_products, commands=["delete_products"])
    dp.register_callback_query_handler(send_all_products, Text(equals="delete_all_products"))
    dp.register_callback_query_handler(delete_all_products, Text(startswith="delete_"))