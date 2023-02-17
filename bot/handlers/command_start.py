from aiogram import types, Dispatcher

from bot.db_work import Search_date_DB
from bot.state import Student_SignUp_State, Student_LogIn_State
from bot.keyboard import list_group_inline_keyboard, signup_inline_keyboard

async def Cmd_Start(message: types.Message):
    await message.answer('Добро пожаловать в бота для проверки лабораторных работ по программированию на языке выского'
                         ' уровня. Для начала работы с ботом создайте профиль. Создать профиль можно как...',
                         parse_mode='html',
                         reply_markup= await signup_inline_keyboard())
    # if not await Search_date_DB('user_chat_id', 'Students_info', message.from_user.id):
    #     await message.answer('Добро пожаловать в бота для проверки лабораторных работ по программированию на'
    #                      ' языке высокого уровня.\n'
    #                          'так как, у вас нет профиля, для начала работы с ботом вам нужно зарегестрироваться в нем, '
    #                          'для этого выберите чей профиль вы хотите создать.',
    #                          reply_markup= await login_inline_keyboard())
    #     await Student_SignUp_State.Student_Inpout_Group.set()
    # elif await Search_date_DB('user_chat_id', 'Students_info', message.from_user.id):
    #     await message.answer('Добро пожаловать в бота для проверки лабораторных работ по программированию на '
    #                          'языке высокого уровня.\n'
    #                          'У вас уже есть аккаунт студента, для того чтобы войти выберете номер вашей группы.',
    #                          reply_markup= await list_group_inline_keyboard())
    #     await Student_LogIn_State.Student_Сhoice_Group.set()
    # elif await Search_date_DB('user_chat_id', 'Teacher_profile', message.from_user.id):
    #     await message.answer('Добро пожаловать в бота для проверки лабораторных работ по программированию на '
    #                          'языке высокого уровня.\n'
    #                          'У вас уже есть аккаунт преподователя, для того чтобы войти введите ваш логин.')




def register_handler(dp: Dispatcher):
    dp.register_message_handler(Cmd_Start, commands=['start', 'help'])
