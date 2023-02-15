from aiogram.utils import executor

from .create_bot import dp
from .handlers import command_start
from .db_work import db_start

async def on_startup(_):
    await db_start()
    print('Бот запустился!')


def start_bot():
    command_start.register_handler(dp)
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=on_startup)