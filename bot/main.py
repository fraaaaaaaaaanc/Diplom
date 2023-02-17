from aiogram.utils import executor

from bot.create_bot import dp
from bot.handlers import command_start, input_cmd
from bot.handlers.student import signup_student, login_student
from bot.handlers.teacher import signup_teacher
from bot.db_work import db_regist as db


async def on_startup(_):
    await db.db_start()
    print('Бот запустился!')


def start_bot():
    command_start.register_handler(dp)
    input_cmd.register_handler(dp)
    signup_student.register_handler(dp)
    login_student.register_handler(dp)

    signup_teacher.register_callback_handler(dp)
    signup_student.register_callback_handler(dp)

    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=on_startup)