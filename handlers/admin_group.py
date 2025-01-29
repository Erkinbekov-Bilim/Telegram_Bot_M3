# admin_group.py

from aiogram import types, Dispatcher
from config import bot, admins

async def welcome_user(message: types.Message):
    for member in message.new_chat_members:
        await message.answer(f"Welcome to the group, {member.full_name}\n\n"
                             f"Please read the rules and regulations for this group\n"
                             f"* Do not swear\n"
                             f"* Do not spam\n"
                             f"Do not abuse other users\n"
                             f"Do not advertise other groups\n"
                             f"This group not for sale\n")



user_warnings = {}

async def user_warning(message: types.Message):
    if message.chat.type != "private":
        if message.from_user.id not in admins:
            await message.answer("Not enough permissions. Please contact an admin")
        elif not message.reply_to_message:
            await message.answer("Command should be used in reply to a message")
        else:
            user_id = message.reply_to_message.from_user.id
            user_name = message.reply_to_message.from_user.full_name
            user_warnings[user_id] = user_warnings.get(user_id, 0) + 1

            for admin in admins:
                await bot.send_message(chat_id=admin, text=f"{user_name} has been warned {user_warnings[user_id]}/3")

                if user_warnings[user_id] >= 3:
                    await bot.kick_chat_member(chat_id=message.chat.id,  user_id=user_id)
                    await bot.unban_chat_member(chat_id=message.chat.id, user_id=user_id)

                    await bot.send_message(chat_id=admin.chat.id, text=f"{user_name} has been banned because of 3 warnings")

def register_handlers_welcome(dp: Dispatcher):
    dp.register_message_handler(welcome_user, content_types=[types.ContentTypes.NEW_CHAT_MEMBERS])
    dp.register_message_handler(user_warning, commands=["warn"])