from aiogram import types, Dispatcher

from bot.state import Teachet_LogIn_State, Teacher
from bot.db_work import Search_userId_date_DB, Search_date_DB
from bot.keyboard import signup_or_create_account, Main_Teacher_Menu


async def Teacher_Input_Name(callback: types.CallbackQuery):
    if await Search_date_DB('user_chat_id', 'Teacher_profile', callback.from_user.id):
        await callback.message.edit_text('Введите ваш логин!')
        await Teachet_LogIn_State.Teacher_Inpout_Password.set()
    else:
        await callback.message.answer('У вас еще нет аккаунта преподователя в данном боте.'
                                      'Вы можете...',
                                      reply_markup= await signup_or_create_account())

async def Teacher_Input_Password(message: types.Message):
    if await Search_userId_date_DB('Teacher_profile', 'name', message.from_user.id, message.text):
        await message.answer('Отилчно! Теперь введите ваш пароль.')
        await Teachet_LogIn_State.Teacher_End_Login.set()
    else:
        await message.answer('К сожалению пользователя с таким именем нет, попробуйте ввести ваш'
                                ' логин еще раз.')


async def Teacher_End_LogIn(message: types.Message):
    if await Search_userId_date_DB('Teacher_profile', 'password', message.from_user.id, message.text):
        await message.answer('Замечательно, вы вошли в свой аккаунт как преподователь! Для того чтобы узнать какими '
                             'командами вы можете воспользоваться, отправьте команду /help или откройте меню.',
                             reply_markup= await Main_Teacher_Menu())
        await Teacher.teacher.set()
    else:
        await message.answer('Вы ввели неверный пароль, попробуйте ввести его еще раз')
    await message.delete()


def register_handler(dp: Dispatcher):
    dp.register_message_handler(Teacher_Input_Password, state=Teachet_LogIn_State.Teacher_Inpout_Password)
    dp.register_message_handler(Teacher_End_LogIn, state=Teachet_LogIn_State.Teacher_End_Login)


def register_callback_handler(dp: Dispatcher):
    dp.register_callback_query_handler(Teacher_Input_Name,
                                       lambda c: c.data.startswith('Teacher_Login'))