from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from bot.state import Student_LogIn_State, Student
from bot.db_work import Search_userId_date_DB
from bot.keyboard import list_group_inline_keyboard


async def Login_Student_Choice_Group(callback: types.CallbackQuery):
        await callback.message.edit_text('Для того чтобы войти выберете номер вашей группы.',
                                       reply_markup= await list_group_inline_keyboard())
        await Student_LogIn_State.Student_Сhoice_Group.set()


async def Login_Student(callback: types.CallbackQuery):
    if await Search_userId_date_DB('Students_info', 'group', callback.from_user.id, callback.data):
        await callback.message.edit_text('Введите ваши фамилию и имя')
        await Student_LogIn_State.Student_Inpout_Name.set()
    else:
        await callback.message.edit_text('Вас нет в выбранной группе, попробуйте выбрать группу еще раз.',
                                         reply_markup= await list_group_inline_keyboard())


async def Student_Input_Name(message: types.Message):
    if await Search_userId_date_DB('Students_info', 'name', message.from_user.id, message.text):
        await message.answer('Отилчно! Теперь введите ваш пароль.')
        await Student_LogIn_State.Student_Inpout_Password.set()
    else:
        await message.answer('К сожалению пользователя с таким именем нет, попробуйте ввести ваши'
                                ' имя и фамилию еще раз.')


async def Student_Input_Password(message: types.Message):
    if await Search_userId_date_DB('Students_info', 'password', message.from_user.id, message.text):
        await message.answer('Замечательно, вы вошли в свой аккаунт как студент! Для того чтобы узнать какими командами '
                             'вы можете воспользоваться, отправьте команду /help или откройте меню.')
        await Student.student.set()
    else:
        await message.answer('Вы ввели неверный пароль, попробуйте ввести его еще раз')
    await message.delete()


def register_handler(dp: Dispatcher):
    dp.register_message_handler(Student_Input_Name, state=Student_LogIn_State.Student_Inpout_Name)
    dp.register_message_handler(Student_Input_Password, state=Student_LogIn_State.Student_Inpout_Password)


# def register_callback_handler(dp: Dispatcher):
#     dp.register_callback_query_handler(Login_Student_Choice_Group, callback='Student_Login')
#     dp.register_callback_query_handler(Login_Student, state=Student_LogIn_State.Student_Сhoice_Group)