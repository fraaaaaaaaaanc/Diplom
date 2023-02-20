from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from bot.state import Teachet_LogIn_State, Teacher_SignUp_State


async def Cmd_teacher_Stop_LogIn(message: types.Message, state: FSMContext):
    await message.answer('Вы остановили авторизацию преподователя!')
    await state.finish()


async def Cmd_Teacher_Stop_SignUp(message: types.Message, state: FSMContext):
    await message.answer('Вы остановили регестрацию преподователя!')
    await state.finish()


def register_handler(dp: Dispatcher):
    dp.register_message_handler(Cmd_teacher_Stop_LogIn,
                                commands=['Stop'],
                                state=[Teachet_LogIn_State.Teacher_Inpout_Password,
                                       Teachet_LogIn_State.Teacher_End_Login]
                                )
    dp.register_message_handler(Cmd_Teacher_Stop_SignUp,
                                commands=['Stop'],
                                state=[Teacher_SignUp_State.Teacher_Input_Login,
                                       Teacher_SignUp_State.Teacher_Inpout_Password,
                                       Teacher_SignUp_State.Teacher_End_SignUp]
                                )