from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from bot.state import Student, Student_SignUp_State, Student_LogIn_State


async def Cmd_Student_Stop_LogIn(message: types.Message, state: FSMContext):
    await message.answer('Вы остановили авторизацию студента!')
    await state.finish()


async def Cmd_Student_Stop_SignUp(message: types.Message, state: FSMContext):
    await message.answer('Вы остановили регестрацию студента!')
    await state.finish()


def register_handler(dp: Dispatcher):
    dp.register_message_handler(Cmd_Student_Stop_LogIn,
                                commands=['Stop'],
                                state=[Student_LogIn_State.Student_Inpout_Name,
                                       Student_LogIn_State.Student_Inpout_Password,
                                       Student_LogIn_State.Student_End_Login]
                                )
    dp.register_message_handler(Cmd_Student_Stop_SignUp,
                                commands=['Stop'],
                                state=[Student_SignUp_State.Student_Inpout_Name,
                                       Student_SignUp_State.Student_Inpout_Password,
                                       Student_SignUp_State.Student_SignUp_End]
                                )