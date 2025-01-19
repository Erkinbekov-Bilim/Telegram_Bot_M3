# fsm_shop.py

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
import buttons
from db import main_db

class FSMShop(StatesGroup):
    product_name = State()
    product_size = State()
    product_category = State()
    product_price = State()
    product_id = State()
    product_info = State()
    product_photo = State()
    product_submit = State()


async def start_shop(message: types.Message, state: FSMContext):
    await FSMShop.product_name.set()
    await message.answer("Please enter product name")

async def load_product_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_name'] = message.text
    await FSMShop.next()
    await message.answer("Please choose product size", reply_markup=buttons.sizes_products)

async def load_product_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_size'] = message.text
    await FSMShop.next()
    await message.answer("Please enter product category")

async def load_product_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_category'] = message.text
    await FSMShop.next()
    await message.answer("Please enter product price")

async def load_product_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_price'] = message.text
    await FSMShop.next()
    await message.answer("Please enter product id")

async def load_product_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_id'] = message.text

    await FSMShop.next()
    await message.answer("Please enter product info")

async def load_product_info(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_info'] = message.text

    await FSMShop.next()
    await message.answer("Please send product photo")

async def load_product_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_photo'] = message.photo[-1].file_id

    await FSMShop.next()
    await message.answer("Please confirm product registration")
    await message.answer_photo(photo = data['product_photo'], caption=f"Product ID: {data['product_id']}\n"
                         f"Product Name: {data['product_name']}\n"
                         f"Product Size: {data['product_size']}\n"
                         f"Product Category: {data['product_category']}\n"
                         f"Product Info: {data['product_info']}\n"
                         f"Product Price: {data['product_price']}", reply_markup=buttons.submit)

async def submit(message: types.Message, state: FSMContext):
    if message.text == "Yes":
        async with state.proxy() as data:
            # Запись в базу
            await main_db.sql_insert_store(
                product_name=data["product_name"],
                product_size=data["product_size"],
                product_price=data["product_price"],
                product_id=data["product_id"],
                product_photo=data["product_photo"]
            )

            await main_db.sql_insert_product_details(
                product_category=data["product_category"],
                product_info=data["product_info"],
                product_id=data["product_id"]
            )

            await message.answer("Thank you for registration!", reply_markup=buttons.remove_keyboard)
            await state.finish()


    elif message.text == "Nah":
        await message.answer('Bye!', reply_markup=buttons.remove_keyboard)
        await state.finish()
        # Отмена записи в базу
    else:
        await message.answer("Please answer Yes or Nah")


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()

    if current_state is None:
        await state.finish()
        await message.answer("Registration canceled", reply_markup=buttons.remove_keyboard)


def register_handlers_fsm_shop(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, Text(equals='cancel', ignore_case=True), state="*")

    dp.register_message_handler(start_shop, commands=["add_product"])
    dp.register_message_handler(load_product_name, state=FSMShop.product_name)
    dp.register_message_handler(load_product_size, state=FSMShop.product_size)
    dp.register_message_handler(load_product_category, state=FSMShop.product_category)
    dp.register_message_handler(load_product_price, state=FSMShop.product_price)
    dp.register_message_handler(load_product_id, state=FSMShop.product_id)
    dp.register_message_handler(load_product_info, state=FSMShop.product_info)
    dp.register_message_handler(load_product_photo, content_types=['photo'], state=FSMShop.product_photo)
    dp.register_message_handler(submit, state=FSMShop.product_submit)