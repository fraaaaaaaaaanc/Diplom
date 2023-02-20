from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from bot.handlers.utils import Main_menu_text
from bot.keyboard import signup_inline_keyboard, login_inline_keyboard, Main_Teacher_Menu, Main_Student_Menu
from bot.state import Student, Teacher


async def Start_Menu(message: types.Message):
    await message.answer(text=Main_menu_text, parse_mode='html')


async def Cmd_LogIn(message: types.Message):
    await message.answer('Для начала выберите как бы вы хотите войти!\n'
                         'Как...',
                         reply_markup= await login_inline_keyboard())


async def Cmd_SignUP(message: types.Message):
    await message.answer('Для начала выберите как бы вы хотите зарегестрироваться!\n'
                         'Как...',
                         reply_markup= await signup_inline_keyboard())


async def Cmd_Exit(message: types.Message, state: FSMContext):
    await message.answer('Удачи!')
    await state.finish()


async def Teacher_test(message: types.Message):
    await message.answer('Тест профиля преподователя.',
                         reply_markup= await Main_Teacher_Menu())
    await Teacher.teacher.set()


async def Student_test(message: types.Message):
    await message.answer('Тест профиля Студента.',
                         reply_markup= await Main_Teacher_Menu())
    await Student.student.set()


def register_handler(dp: Dispatcher):
    dp.register_message_handler(Start_Menu,
                                commands=['Help'])
    dp.register_message_handler(Cmd_LogIn,
                                commands=['LogIn'])
    dp.register_message_handler(Cmd_SignUP,
                                commands=['SignUp'])
    dp.register_message_handler(Cmd_Exit,
                                commands=['Exit'],
                                state=Student.student)
    dp.register_message_handler(Teacher_test,
                                commands=['Teacher'])
    dp.register_message_handler(Student_test,
                                commands=['Student'])