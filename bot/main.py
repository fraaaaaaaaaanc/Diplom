from aiogram.utils import executor

from bot.create_bot import dp
from bot.handlers import command_start, main_commands
from bot.handlers.student import login_student, signup_student, stop_cmd_student, main_student_cmd
from bot.handlers.teacher import login_teacher, signup_teacher, stop_cmd_teacher, main_teacher_cmd
from bot.db_work import db_regist as db


async def on_startup(_):
    await db.db_start()
    print('Бот запустился!')


async def on_shutdown(_):
    await db.Close_DB()


def start_bot():
    command_start.register_handler(dp)
    main_commands.register_handler(dp)

    stop_cmd_student.register_handler(dp)
    main_student_cmd.register_handler(dp)
    main_student_cmd.register_callback_handler(dp)
    login_student.register_handler(dp)
    login_student.register_callback_handler(dp)
    signup_student.register_handler(dp)
    signup_student.register_callback_handler(dp)

    stop_cmd_teacher.register_handler(dp)
    main_teacher_cmd.register_handler(dp)
    login_teacher.register_handler(dp)
    login_teacher.register_callback_handler(dp)
    signup_teacher.register_handler(dp)
    signup_teacher.register_callback_handler(dp)


    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=on_startup,
                           on_shutdown=on_shutdown)