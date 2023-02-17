from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from .utils import Token_Api


storage = MemoryStorage()
bot = Bot(token=Token_Api.TOKEN_API)
dp = Dispatcher(bot, storage=storage)