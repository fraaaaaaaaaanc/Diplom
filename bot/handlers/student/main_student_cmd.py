from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove

from .utils import Main_Student_Menu_Text
from bot.state import Student
from bot.keyboard import Main_Student_Menu


async def Cmd_Menu_Student(message: types.Message):
    await message.answer('Меню команд для работы с ботом.',
                         reply_markup= await Main_Student_Menu())


async def Cmd_Help_Student(message: types.Message):
    await message.answer(Main_Student_Menu_Text,
                         parse_mode='html')


async def Cmd_Get_Tusk(message: types.Message):
    await message.answer('!',
                         reply_markup= types.ReplyKeyboardRemove())


def register_handler(dp: Dispatcher):
    dp.register_message_handler(Cmd_Menu_Student,
                                commands=['Menu'],
                                state=Student.student)
    dp.register_message_handler(Cmd_Help_Student,
                                commands=['Help'],
                                state=Student.student)
    dp.register_message_handler(Cmd_Get_Tusk,
                                commands=['GetTask'],
                                state=Student.student)