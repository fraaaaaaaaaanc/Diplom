from aiogram import types, Dispatcher

from ..create_bot import bot
from ..keyboard import login_inline_keyboard


async def Cmd_Start(message: types.Message):
    await message.answer('Добро пожаловать в бота для проверки лабораторных работ по базам данных.\n'
                         'Для того чтобы начать работу с ботом авторизируйтесь как...',
                         reply_markup=login_inline_keyboard())


def register_handler(dp: Dispatcher):
    dp.register_message_handler(Cmd_Start, commands=['start', 'help'])