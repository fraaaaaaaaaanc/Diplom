from aiogram import types, Dispatcher

from ..utils import start_menu
from ..keyboard import login_inline_keyboard


async def Start_Menu(message: types.Message):
    await message.answer(text=start_menu, parse_mode='html')


async def Cmd_SignUP(message: types.Message):
    await message.answer('Для начала выберите как бы вы хотели авторизоваться!\n'
                         'Как...',
                         reply_markup=login_inline_keyboard())


def register_handler(dp: Dispatcher):
    dp.register_message_handler(Start_Menu, commands=['menu'])
    dp.register_message_handler(Cmd_SignUP, commands=['SignUp'])