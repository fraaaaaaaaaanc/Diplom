from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove

from bot.handlers.utils import Main_menu_text
from bot.keyboard import signup_inline_keyboard, login_inline_keyboard, Main_Teacher_Menu, Main_Student_Menu, \
    Main_Menu
from bot.state import Student, Teacher


async def Start_Menu(message: types.Message):
    await message.answer(text=Main_menu_text,
                         parse_mode='html',
                         reply_markup= ReplyKeyboardRemove())


async def Cmd_Menu(message: types.Message):
    await message.answer('Главное меню входа. Выберите команду!',
                         reply_markup= await Main_Menu())


async def Cmd_Stop(message: types.Message):
    await message.answer('Вы еще не начали какое-либо действие чтобы его остановить для начала выберите '
                         'какую-либо команду из меню или отправьте команду /Help',
                         reply_markup= await Main_Menu())


async def Cmd_LogIn(message: types.Message):
    await message.answer('Для начала выберите как вы хотите войти!\n'
                         'Как...',
                         reply_markup = await login_inline_keyboard())


async def Cmd_SignUP(message: types.Message):
    await message.answer('Для начала выберите как вы хотите зарегестрироваться!\n'
                         'Как...',
                         reply_markup = await signup_inline_keyboard())


async def Teacher_test(message: types.Message):
    await message.answer('Тест профиля преподователя.',
                         reply_markup= await Main_Teacher_Menu())
    await Teacher.teacher.set()


async def Student_test(message: types.Message):
    await message.answer('Тест профиля Студента.',
                         reply_markup= await Main_Student_Menu())
    await Student.student.set()


async def No_Cmd_Text(message: types.Message):
    await message.answer('Вы ввели команду которую я не могу понять('
                         'Чтобы посмотреть список команд и их функции отправьте команду /Help '
                         'или выберите команду из меню',
                         reply_markup=await Main_Menu())


def register_handler(dp: Dispatcher):
    dp.register_message_handler(Start_Menu,
                                commands=['Help'])
    dp.register_message_handler(Cmd_Menu,
                                commands=['Menu'])
    dp.register_message_handler(Cmd_Stop,
                                commands=['Stop'])
    dp.register_message_handler(Cmd_LogIn,
                                commands=['LogIn'])
    dp.register_message_handler(Cmd_SignUP,
                                commands=['SignUp'])
    dp.register_message_handler(Teacher_test,
                                commands=['Teacher'])
    dp.register_message_handler(Student_test,
                                commands=['Student'])
    dp.register_message_handler(No_Cmd_Text)