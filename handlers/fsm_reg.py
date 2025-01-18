
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
import buttons

class FSMReg(StatesGroup):
    fullname = State()
    age = State()
    email = State()
    city = State()
    photo =  State()
    submit = State()


async def start_reg(message: types.Message):
    await message.answer("Please enter your full name")
    await FSMReg.fullname.set()

async def load_fullname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['fullname'] = message.text

    await FSMReg.next()
    await message.answer("Please enter your age")

async def load_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text

    await FSMReg.next()
    await message.answer("Please enter your email")

async def load_email(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['email'] = message.text

    await FSMReg.next()
    await message.answer("Please enter your city")

async def load_city(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text

    await FSMReg.next()
    await message.answer("Please send your photo")

async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

    await FSMReg.next()
    await message.answer("Please confirm your registration")
    await message.answer_photo(photo = data['photo'], caption=f"Full Name: {data['fullname']}\n"
                         f"Age: {data['age']}\n"
                         f"Email: {data['email']}\n"
                         f"City: {data['city']}", reply_markup=buttons.submit)

async def submit(message: types.Message, state: FSMContext):
    if message.text == "Yes":
        await message.answer("Thank you for registration!", reply_markup=buttons.remove_keyboard)
        await state.finish()
        # Запись в базу

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


def register_handlers_fsm_reg(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, Text(equals='cancel', ignore_case=True), state="*")

    dp.register_message_handler(start_reg, commands=["registration"])
    dp.register_message_handler(load_fullname, state=FSMReg.fullname)
    dp.register_message_handler(load_age, state=FSMReg.age)
    dp.register_message_handler(load_email, state=FSMReg.email)
    dp.register_message_handler(load_city, state=FSMReg.city)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMReg.photo)
    dp.register_message_handler(submit, state=FSMReg.submit)