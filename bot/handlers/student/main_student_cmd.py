from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
import os

from .utils import Main_Student_Menu_Text, List_Student_State, Get_File_Path
from bot.state import Student
from bot.keyboard import Main_Student_Menu, student_change_number_lab, Main_Menu
from bot.db_work import Change_Name, Search_Task_DB, Get_Record
from bot.exel_work import visual_edit_excel
from Test_Package import test_start, get_description


async def Cmd_Stop_Student(message: types.Message):
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
                         reply_markup=await student_change_number_lab())
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
                         reply_markup=await student_change_number_lab())
    await Student.student_get_manual.set()


async def Student_Get_Manual(callback: types.CallbackQuery):
    await callback.message.answer_document(open(f'C:\pythonProject\Main_Diplom\Manual'
                                                f'\Методичка Лаб №{callback.data}.pdf', 'rb'),
                                                caption=f'Методический материал для лабораторной работы '
                                                        f'№{callback.data}.')
    await callback.message.answer('Для того чтобы продолжить работу, выберите новую команду!',
                                  reply_markup=await Main_Student_Menu())
    await Student.student.set()


async def Cmd_Check_Lab(message: types.Message):
    await message.answer('Выберите номер лабораторной работы которую вы хотите проверить!',
                         reply_markup=await student_change_number_lab())
    await Student.student_input_lab_number.set()


async def No_Callback(message: types.Message):
    await message.answer('Для начала выберите номер лабороторной работы или отправьте команду /Stop '
                                  'если хотите остановить выбранное действие.')

async def Student_Input_Number_Task(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            data['number_lab'] = callback.data
            data['group'] = await Get_Record('Students_info', 'group', callback.from_user.id)
            data['student_name'] = await Get_Record('Students_info', 'name', callback.from_user.id)
            data['user_chat_id'] = await Get_Record('Students_info', 'user_chat_id', callback.from_user.id)
        await callback.message.answer(f'Введите номер вашего задания для лабораторной №{callback.data}.')
        await Student.student_send_file.set()



async def Student_Send_File(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number_task'] = message.text
    estimation = await Search_Task_DB(state)
    if estimation:
        await message.answer(f"Ваше задание для лабораторной работы №{data['number_lab']} оценивается в данном"
                            f" диапазоне: {estimation}. Для того чтобы приступить к проверке задания прочитайте "
                             f"инструкцию к отпарвке файла ниже.")
        await message.answer(await get_description(state))
        await Student.test_file.set()
    else:
        await message.answer(f"К сожалению задания с таким номером нет, поппробуйте ввести его еще раз.")


async def Processing_File(message: types.Message, state: FSMContext):
    if message.document is None or message.document.mime_type != 'text/x-csrc':
        await message.reply("Принимаются только файлы с исходным кодом на языке С."
                            " Попробуйте отправить другой файл.")
    else:
        await message.answer('Файл принят, ожидайте результатов проверки.')
        async with state.proxy() as data:
            data['file_path'] = await Get_File_Path(message.document['file_name'], state)
        await message.document.download(data['file_path'])
        erorr_list = await test_start(state)
        if not erorr_list:
            await message.answer('Отлично! Данное решение прошло все проверки.')
            await visual_edit_excel(state, "successful")
        else:
            await message.answer(f'Ваше решение не прошло тесты по причине: {erorr_list}\n'
                       f'Попробуйте решить задание по другому и повторите попытку проверки.')
            await visual_edit_excel(state, "unsuccessful")
        await Student.student.set()


async def Cmd_Change_Name(message: types.Message):
    await message.answer('Введите новые фамилию и имя.',
                         reply_markup=types.ReplyKeyboardRemove())
    await Student.student_change_name.set()


async def Student_Change_Name(message: types.Message):
    await Change_Name(message.text.title())
    await message.answer(f'Ваш ник успешно изменен на {message.text.title()}.',
                         reply_markup=await Main_Student_Menu())
    await Student.student.set()

async def Cmd_Exit(message: types.Message, state: FSMContext):
    await message.answer('Вы вышли из аккаунта студента.',
                         reply_markup= await Main_Menu())
    await state.finish()


async def Cmd_Stop_No_State(message: types.Message):
    await message.answer('Вы еще не начали какое-либо действие чтобы его остановить для начала выберите '
                         'какую-либо команду из меню или отправьте команду /Help',
                         reply_markup=await Main_Student_Menu())


async def No_Cmd_Text(message: types.Message):
    await message.answer('Вы ввели команду которую я не могу понять('
                         'Чтобы посмотреть список команд и их функции отправьте команду /Help '
                         'или выберите команду из меню',
                         reply_markup=await Main_Student_Menu())


def register_handler(dp: Dispatcher):
    dp.register_message_handler(Cmd_Stop_Student,
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
    dp.register_message_handler(Cmd_Check_Lab,
                                commands=['CheckLab'],
                                state=Student.student)
    dp.register_message_handler(No_Callback,
                                state=Student.student_input_lab_number)
    dp.register_message_handler(Student_Input_Number_Task,
                                state=Student.student_input_lab_number)
    dp.register_message_handler(Student_Send_File,
                                state=Student.student_send_file)
    dp.register_message_handler(Processing_File,
                                content_types=['document'],
                                state=Student.test_file)
    dp.register_message_handler(Cmd_Change_Name,
                                commands=['ChangeName'],
                                state=Student.student)
    dp.register_message_handler(Student_Change_Name,
                                state=Student.student_change_name)
    dp.register_message_handler(Cmd_Exit,
                                commands=['Exit'],
                                state=Student.student)
    dp.register_message_handler(Cmd_Stop_No_State,
                                commands=['Stop'],
                                state=Student.student)
    dp.register_message_handler(No_Cmd_Text,
                                state=Student.student)


def register_callback_handler(dp: Dispatcher):
    dp.register_callback_query_handler(Student_Get_Task,
                                      state=Student.student_get_task)
    dp.register_callback_query_handler(Student_Get_Manual,
                                       state=Student.student_get_manual)
    dp.register_callback_query_handler(Student_Input_Number_Task,
                                       state=Student.student_input_lab_number)
