from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

async def SignUp_Teacher(callback: types.CallbackQuery):
    await callback.message.answer('!!!!!!!!!!!!!!!!!!!!!')


def register_callback_handler(dp: Dispatcher):
    dp.register_callback_query_handler(SignUp_Teacher, run_task='Teacher_SignUp')