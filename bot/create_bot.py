from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from .utils import Token_Api


storage = MemoryStorage()
# bot = Bot(token=Token_Api.TOKEN_API)
bot = Bot(token="5914794540:AAGFZ11N8faMMLg4kU7Kc3IDrfn73_zxVv4")
dp = Dispatcher(bot, storage=storage)