# buttons.py

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


start = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    KeyboardButton("/start"),
    KeyboardButton("/mem"),
    KeyboardButton("/game"),
    KeyboardButton("/quiz"),
    KeyboardButton("/reply_webapp"),
    KeyboardButton("/reply_inline"),
    KeyboardButton("/registration"),
    KeyboardButton("/add_product"),
    KeyboardButton("/send_products"),
    KeyboardButton("/delete_products"),
)


submit = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True).add(
    KeyboardButton("Yes"),
    KeyboardButton("Nah"),
)

sizes_products = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True).add(
    KeyboardButton("XXS"),
    KeyboardButton("XS"),
    KeyboardButton("S"),
    KeyboardButton("M"),
    KeyboardButton("L"),
    KeyboardButton("XL"),
    KeyboardButton("XXL"),
)

# Удаление кнопок из интерфейса
remove_keyboard = ReplyKeyboardRemove()