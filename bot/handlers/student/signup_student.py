from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext


from bot.state import Student, Student_SignUp_State
from bot.db_work import Search_date_DB, Add_New_Profile_Student, Delete_Record
from bot.keyboard import student_delete_or_login_inline_keyboard, Main_Student_Menu

async def SignUp_Student(callback: types.CallbackQuery, state: FSMContext):
    if not await Search_date_DB('user_chat_id', 'Students_info', callback.from_user.id):
        async with state.proxy() as data:
            data['user_id'] = callback.from_user.id
        await callback.message.edit_text('Для начала введите номер вашей группы.')
        await Student_SignUp_State.Student_Inpout_Name.set()
    else:
        await callback.message.edit_text('У вас уже есть профиль в данном боте, вы можете либой удалить свой старый'
                                      ' профиль и зарегестрироваться заново, либо войти в уже существующий.',
                                      reply_markup= await student_delete_or_login_inline_keyboard())


async def Delete_Student_Profile(callback: types.CallbackQuery):
    await Delete_Record('Students_info', 'user_chat_id', callback.from_user.id)
    await callback.message.answer('Ваш профиль успешно удален!'
                                  'Вы можете создать новый профиль студента отправив команду /SignUp')

async def SignUp_Student_Input_Name(message: types.Message, state: FSMContext):
    if await Search_date_DB('group', 'Group_students', message.text.upper()):
        async with state.proxy() as data:
            data['group'] = message.text.upper()
        await message.answer('Отлично! Тепепь введите ваши фамилию и имя.')
        await Student_SignUp_State.Student_Inpout_Password.set()
    else:
        await message.answer('К сожалению такой группы нет( '
                               'Попробуйте ввести номер группы еще раз.')


async def SignUp_Student_Input_Password(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['student_name'] = message.text
    await message.answer('Супер! Теперь введите ваш пароль!')
    await Student_SignUp_State.Student_SignUp_End.set()


async def SignUp_Student_End(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['password'] = message.text
    await message.delete()
    await message.answer(await Add_New_Profile_Student(state),
                         reply_markup= await Main_Student_Menu())
    await Student.student.set()


def register_handler(dp: Dispatcher):
    dp.register_message_handler(SignUp_Student_Input_Name,
                                state=Student_SignUp_State.Student_Inpout_Name)
    dp.register_message_handler(SignUp_Student_Input_Password,
                                state=Student_SignUp_State.Student_Inpout_Password)
    dp.register_message_handler(SignUp_Student_End,
                                state=Student_SignUp_State.Student_SignUp_End)


def register_callback_handler(dp: Dispatcher):
    dp.register_callback_query_handler(SignUp_Student,
                                       lambda c: c.data.startswith('Student_SignUp'))
    dp.register_callback_query_handler(Delete_Student_Profile,
                                       lambda c: c.data.startswith('Delete_profile_student'))