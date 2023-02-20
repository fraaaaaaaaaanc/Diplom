from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from bot.state import Teacher, Teacher_SignUp_State
from .utils import TOKEN_Teacher
from bot.db_work import Add_New_Profile_Teacher, Search_date_DB, Delete_Record
from bot.keyboard import teacher_delete_or_login_inline_keyboard, Main_Teacher_Menu

async def SignUp_Teacher_Input_Token(callback: types.CallbackQuery):
    if not await Search_date_DB('user_chat_id', 'Teacher_profile', callback.from_user.id):
        await callback.message.answer('Для того чтобы создать новый аккаунт преподователя нужно ввести токен!'
                                      '(его можно узнать у ...)')
        await Teacher_SignUp_State.Teacher_Input_Login.set()
    else:
        await callback.message.edit_text('У вас уже есть аккаунт преподователя.'
                                      'Вы можете войти в старый аккаунт, либо удалить его и создать новый.',
                                      reply_markup= await teacher_delete_or_login_inline_keyboard())


async def Delete_Teacher_Profile(callback: types.CallbackQuery):
    await Delete_Record('Teacher_profile', 'user_chat_id', callback.from_user.id)
    await callback.message.answer('Ваш профиль успешно удален!'
                                  'Вы можете создать новый профиль преподователя отправив команду /SignUp')


async def SignUp_Teacher_Input_LogIn(message: types.Message, state: FSMContext):
    if TOKEN_Teacher == message.text:
        async with state.proxy() as data:
            data['user_id'] = message.from_user.id
        await message.answer('Придумайте свой логин.')
        await Teacher_SignUp_State.Teacher_Inpout_Password.set()
    else:
        await message.answer('Вы ввели неверный токен, попробуйте ввести его еще раз!')


async def SignUp_Teacher_Input_Password(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['teacher_login'] = message.text
    await message.answer('Отлично, теперь придумайте пароль.')
    await Teacher_SignUp_State.Teacher_End_SignUp.set()


async def Teacher_End_Sigup(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['teacher_password'] = message.text
    await message.delete()
    await message.answer(await Add_New_Profile_Teacher(state),
                         reply_markup= await Main_Teacher_Menu())
    await Teacher.teacher.set()


def register_handler(dp: Dispatcher):
    dp.register_message_handler(SignUp_Teacher_Input_LogIn, state=Teacher_SignUp_State.Teacher_Input_Login)
    dp.register_message_handler(SignUp_Teacher_Input_Password, state=Teacher_SignUp_State.Teacher_Inpout_Password)
    dp.register_message_handler(Teacher_End_Sigup, state=Teacher_SignUp_State.Teacher_End_SignUp)


def register_callback_handler(dp: Dispatcher):
    dp.register_callback_query_handler(SignUp_Teacher_Input_Token,
                                       lambda c: c.data.startswith('Teacher_SignUp'))
    dp.register_callback_query_handler(Delete_Teacher_Profile,
                                       lambda c: c.data.startswith('Delete_profile_teacher'))