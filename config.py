# config.py

from decouple import config
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

token = config('TOKEN')
bot = Bot(token=token)
dp = Dispatcher(bot=bot, storage=MemoryStorage())
admins = [5576961334]