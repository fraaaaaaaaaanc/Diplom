from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from .utils import Main_Student_Menu_Text, List_Student_State
from bot.state import Student
from bot.keyboard import Main_Student_Menu, student_change_manual_or_task, Main_Menu


async def Cmd_Stop_Teacher(message: types.Message):
    await message.answer('Вы отсановили выбранную команду. '
                         'В меню вы можете выбрать другую команду.',
                         reply_markup=await Main_Student_Menu())
    await Student.student.set()


async def Cmd_Menu_Student(message: types.Message):
    await message.answer('Меню команд для работы с ботом.',
                         reply_markup= await Main_Student_Menu())


async def Cmd_Help_Student(message: types.Message):
    await message.answer(Main_Student_Menu_Text,
                         parse_mode='html')


async def Cmd_Get_Tusk(message: types.Message):
    await message.answer('Выберите номер лабораторной работы для задания на нее.',
                         reply_markup=await student_change_manual_or_task())
    await Student.student_get_task.set()


async def Student_Get_Task(callback: types.CallbackQuery):
    await callback.message.answer_document(open(f'C:\pythonProject\Main_Diplom\Task'
                                                f'\Задание Лаб №{callback.data}.docx', 'rb'),
                                           caption=f'Задание для\nлабораторной работы '
                                                   f'№{callback.data}.')
    await callback.message.answer('Для того чтобы продолжить работу, выберите новую команду!',
                                  reply_markup=await Main_Student_Menu())
    await Student.student.set()


async def Cmd_GetManual(message: types.Message):
    await message.answer('Выберите номер лабораторной работы для получения методического материала.',
                         reply_markup=await student_change_manual_or_task())
    await Student.student_get_manual.set()


async def Student_Get_Manual(callback: types.CallbackQuery):
    await callback.message.answer_document(open(f'C:\pythonProject\Main_Diplom\Manual'
                                                f'\Методичка Лаб №{callback.data}.pdf', 'rb'),
                                                caption=f'Методический материал для лабораторной работы '
                                                        f'№{callback.data}.')
    await callback.message.answer('Для того чтобы продолжить работу, выберите новую команду!',
                                  reply_markup=await Main_Student_Menu())
    await Student.student.set()


async def Cmd_Check_L(message: types.Message):
    pass


async def Cmd_Exit(message: types.Message, state: FSMContext):
    await message.answer('Вы вышли из аккаунта студента.',
                         reply_markup= await Main_Menu())
    await state.finish()


async def No_Cmd_Text(message: types.Message):
    await message.answer('Вы ввели команду которую я не могу понять('
                         'Чтобы посмотреть список команд и их функции отправьте команду /Help '
                         'или выберите команду из меню',
                         reply_markup=await Main_Student_Menu())


def register_handler(dp: Dispatcher):
    dp.register_message_handler(Cmd_Stop_Teacher,
                                commands=['Stop'],
                                state=List_Student_State)
    dp.register_message_handler(Cmd_Menu_Student,
                                commands=['Menu'],
                                state=Student.student)
    dp.register_message_handler(Cmd_Help_Student,
                                commands=['Help'],
                                state=Student.student)
    dp.register_message_handler(Cmd_Get_Tusk,
                                commands=['GetTask'],
                                state=Student.student)
    dp.register_message_handler(Cmd_GetManual,
                                commands=['GetManual'],
                                state=Student.student)
    dp.register_message_handler(Cmd_Exit,
                                commands=['Exit'],
                                state=Student.student)

    dp.register_message_handler(No_Cmd_Text,
                                state=Student.student)


def register_callback_handler(dp: Dispatcher):
    dp.register_callback_query_handler(Student_Get_Task,
                                      state=Student.student_get_task)
    dp.register_callback_query_handler(Student_Get_Manual,
                                       state=Student.student_get_manual)
