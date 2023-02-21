from aiogram import types, Dispatcher

from bot.keyboard import signup_inline_keyboard


async def Cmd_Start(message: types.Message):
    await message.answer('Добро пожаловать в бота для проверки лабораторных работ по программированию на языке выского'
                         ' уровня. Для начала работы с ботом создайте профиль или отправьте команду <b>/Help</b> '
                         'чтобы узнать стартовые функции бота. Создать профиль можно как...',
                         parse_mode='html',
                         reply_markup= await signup_inline_keyboard())


def register_handler(dp: Dispatcher):
    dp.register_message_handler(Cmd_Start, commands=['start'])
