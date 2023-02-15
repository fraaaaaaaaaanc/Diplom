from aiogram import Bot
from aiogram.dispatcher import Dispatcher

from .config import TOKEN_API


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)