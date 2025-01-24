from aiogram import executor
import logging
from config import bot, admins, dp
from handlers import commands, echo, quiz, webapp, fsm_reg, fsm_shop, send_products, delete_products
import buttons
from db import main_db



async def on_startup(_):
    for admin in admins:
        await bot.send_message(chat_id=admin, text="Bot started", reply_markup=buttons.start)

    await main_db.create_db()


async def on_shutdown(_):
    for admin in admins:
        await bot.send_message(chat_id=admin, text="Bot stopped")

commands.register_handlers(dp)
quiz.register_handlers(dp)
webapp.register_handlers_webapp(dp)
fsm_reg.register_handlers_fsm_reg(dp)
fsm_shop.register_handlers_fsm_shop(dp)
send_products.register_handlers_delete_products(dp)
delete_products.register_handlers_send_products(dp)
echo.register_handlers(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)


