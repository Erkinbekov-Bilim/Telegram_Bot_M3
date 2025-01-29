# edit_products.py

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from db import main_db


class EditProducts(StatesGroup):
    for_field = State()
    for_new_photo = State()
    for_new_field = State()


async def start_send_products(message: types.Message):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    button_all = InlineKeyboardButton("All", callback_data="edit_products_all")
    button_one = InlineKeyboardButton("One", callback_data="edit_products_one")

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

            edit_keyboard = InlineKeyboardMarkup(resize_keyboard=True)
            edit_button = InlineKeyboardButton("Edit", callback_data=f"edit_{product['product_id']}")
            edit_keyboard.add(edit_button)

            await call.message.answer_photo(photo = product['product_photo'], caption=caption, reply_markup=edit_keyboard)

    else:
        await call.message.answer("No products found")


async def edit_products(call: types.CallbackQuery, state: FSMContext):
    product_id = int(call.data.split("_")[1])

    await state.update_data(product_id=product_id)

    keyboard = InlineKeyboardMarkup(resize_keyboard=True)

    button_name = InlineKeyboardButton("Name", callback_data="field_name_product")
    button_category = InlineKeyboardButton("Category", callback_data="field_category")
    button_collection = InlineKeyboardButton("Collection", callback_data="field_collection")
    button_price = InlineKeyboardButton("Price", callback_data="field_price")
    button_size = InlineKeyboardButton("Size", callback_data="field_size")
    button_photo = InlineKeyboardButton("Photo", callback_data="field_photo")
    button_info = InlineKeyboardButton("Info", callback_data="field_info_product")

    keyboard.add(button_name, button_size, button_category, button_collection, button_info, button_photo, button_price)

    await call.message.answer("Choose field to edit", reply_markup=keyboard)

    await EditProducts.for_field.set()


async def edit_select_field_products(call: types.CallbackQuery, state: FSMContext):

    field_map = {
        'field_name_product': 'product_name',
        'field_category': 'product_category',
        'field_collection': 'collection',
        'field_price': 'product_price',
        'field_size': 'product_size',
        'field_photo': 'product_photo',
        'field_info_product': 'product_info',
    }

    field = field_map.get(call.data)

    if not field:
        await call.message.answer("Invalid field selected")
        return

    await state.update_data(field=field)

    if field == 'product_photo':
        await EditProducts.for_new_photo.set()
        await call.message.answer("Send new photo")
    else:
        await EditProducts.for_new_field.set()
        await call.message.answer(f"Send new field")

async def set_new_value(message: types.Message, state: FSMContext):
    user_data =  await state.get_data()
    product_id = user_data.get("product_id")

    field = user_data['field']

    new_value = message.text

    main_db.update_product_field(product_id, field, new_value)

    await message.answer(f"Field {field} has been updated to {new_value}\n"
                         f"Please update list!")

    await state.finish()

async def send_new_photo(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    product_id = user_data.get("product_id")

    photo_id = message.photo[-1].file_id

    main_db.update_product_field(product_id, "product_photo", photo_id)

    await message.answer(f"Photo has been updated\n"
                         f"Please update list!")

    await state.finish()

def register_handlers_edit_products(dp: Dispatcher):
    dp.register_message_handler(start_send_products, commands=["edit_products"])
    dp.register_callback_query_handler(send_all_products, Text(equals="edit_products_all"))
    dp.register_callback_query_handler(edit_products, Text(startswith="edit_"), state="*")
    dp.register_callback_query_handler(edit_select_field_products, Text(startswith="field_"), state=EditProducts.for_field)
    dp.register_message_handler(set_new_value, state=EditProducts.for_new_field)
    dp.register_message_handler(send_new_photo, content_types=["photo"], state=EditProducts.for_new_photo)

