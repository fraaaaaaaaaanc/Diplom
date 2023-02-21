from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from .utils import Main_Teacher_Menu_Text
from bot.keyboard import Main_Teacher_Menu, Main_Menu
from .utils import List_State_Teacher
from bot.state import Teacher
from bot.db_work import Add_Group, Delete_Group, Get_Group_list, Get_StudentList, Delete_Student, Change_Token


async def Cmd_Stop_Teacher(message: types.Message):
    await message.answer('Вы отсановили выбранную команду. '
                         'В меню вы можете выбрать другую команду.',
                         reply_markup=await Main_Teacher_Menu())
    await Teacher.teacher.set()


async def Cmd_Menu_Teacher(message: types.Message):
    await message.answer('Меню команд для работы с ботом.',
                         reply_markup= await Main_Teacher_Menu())


async def Cmd_Help_Teacher(message: types.Message):
    await message.answer(Main_Teacher_Menu_Text,
                         parse_mode='html')


async def Cmd_AddGroup_Teacher(message: types.Message):
    await message.answer('Введите номер группы которую вы хотите добавить.',
                         reply_markup= types.ReplyKeyboardRemove())
    await Teacher.teacher_add_group.set()


async def Teacher_AddGroup(message: types.Message):
    if await Add_Group(message.text.upper()):
        await message.answer(f'Группа {message.text.upper()}, успешно добавлена в список групп.',
                             reply_markup= await Main_Teacher_Menu())
    else:
        await message.answer(f'Група {message.text.upper()} уже есть в списке групп, попробуйте '
                             f'отправить команду /GroupList для просмотра списка групп, затем попробуйте '
                             f'добавить группу еще раз.',
                             reply_markup= await Main_Teacher_Menu())
    await Teacher.teacher.set()


async def Cmd_DeleteGroup_Teacher(message: types.Message):
    await message.answer('Введите номер группы которую, вы хотите удалить.',
                         reply_markup= types.ReplyKeyboardRemove())
    await Teacher.teacher_delete_group.set()


async def Teacher_DeleteGroup(message: types.Message):
    if await Delete_Group(message.text.upper()):
        await message.answer(f'Группа {message.text.upper()} успешно удалена из списка групп.',
                             reply_markup= await Main_Teacher_Menu())
    else:
        await message.answer(f'Группы {message.text.upper()} нет в списке групп, попробуйте'
                             f'отправить команду /GroupList для просмотра списка групп, затем попробуйте '
                             f'удалить группу еще раз.',
                             reply_markup= await Main_Teacher_Menu())
    await Teacher.teacher.set()


async def Cmd_Get_GroupList(message: types.Message):
    group_list = ''
    res = await Get_Group_list()
    for el in res:
        group_list += f'{el}\n'
    await message.answer(f'Список групп:\n<b>{group_list}</b>',
                         parse_mode='html',
                         reply_markup= await Main_Teacher_Menu())
    await Teacher.teacher.set()


async def Cmd_Get_StudentList(message: types.Message):
    await message.answer('Введите номер группы, список студентов которой вы хотите получить.',
                         reply_markup= types.ReplyKeyboardRemove())
    await Teacher.teacher_get_list_student.set()


async def Teacher_Get_StudentList(message: types.Message):
    res = await Get_StudentList(message.text.upper())
    if res:
        student_list = ''
        for tuple in res:
            for el in tuple:
                student_list += f'{el}\n'
        await message.answer(f'Список группы {message.text.upper()}:\n{student_list}',
                             reply_markup= await Main_Teacher_Menu())
    elif res == []:
        await message.answer(f'Список групп {message.text.upper()} пуст.',
                             reply_markup= await Main_Teacher_Menu())
    else:
        await message.answer(f'Группы {message.text.upper()} нет в списке групп, попробуйте ввести команду '
                             f'/GroupList, для просмотра списка групп, после чего выведите список студентое еще раз.',
                             reply_markup= await Main_Teacher_Menu())
    await Teacher.teacher.set()


async def Cmd_Delete_Student(message: types.Message):
    await message.answer('Введите Фамилию и имя студента которого вы хотите удалить.')
    await Teacher.teacher_delete_student.set()


async def Teacher_Delete_Student(message: types.Message):
    if await Delete_Student(message.text):
        await message.answer(f'Студент {message.text} успешно удален из списка студентов.',
                             reply_markup= await Main_Teacher_Menu())
    else:
        await message.answer(f'Студент {message.text} не был найден в списке студентов, попробуйте отправить команду '
                             f'/StudentList для получения списка группы, найдите нужного студента и попробуйте удалить '
                             f'его еще раз.',
                             reply_markup= await Main_Teacher_Menu())
    await Teacher.teacher.set()


async def Cmd_Change_Token(message: types.Message):
    await message.answer('Для того чтобы сменить, токен введите новый.',
                         reply_markup= types.ReplyKeyboardRemove())
    await Teacher.teacher_change_token.set()


async def Teacher_Change_Token(message: types.Message):
    await Change_Token(message.text)
    await message.answer(f'Токен успешно изменен на "{message.text}"')
    await Teacher.teacher.set()


async def Cmd_Exit(message: types.Message, state: FSMContext):
    await message.answer('Вы вышли из аккаунта преподователя.',
                         reply_markup= await Main_Menu())
    await state.finish()


async def No_Cmd_Text(message: types.Message):
    await message.answer('Вы ввели команду которую я не могу понять('
                         'Чтобы посмотреть список команд и их функции отправьте команду /Help '
                         'или выберите команду из меню',
                         reply_markup=await Main_Teacher_Menu())


def register_handler(dp: Dispatcher):
    dp.register_message_handler(Cmd_Stop_Teacher,
                                commands=['Stop'],
                                state=List_State_Teacher)
    dp.register_message_handler(Cmd_Menu_Teacher,
                                commands=['Menu'],
                                state=Teacher.teacher)
    dp.register_message_handler(Cmd_Help_Teacher,
                                commands=['Help'],
                                state=Teacher.teacher)
    dp.register_message_handler(Cmd_AddGroup_Teacher,
                                commands=['AddGroup'],
                                state=Teacher.teacher)
    dp.register_message_handler(Teacher_AddGroup,
                                state=Teacher.teacher_add_group)
    dp.register_message_handler(Cmd_DeleteGroup_Teacher,
                                commands=['DeleteGroup'],
                                state=Teacher.teacher)
    dp.register_message_handler(Teacher_DeleteGroup,
                                state=Teacher.teacher_delete_group)
    dp.register_message_handler(Cmd_Get_GroupList,
                                commands=['GroupList'],
                                state=[Teacher.teacher,
                                       Teacher.teacher_delete_group,
                                       Teacher.teacher_add_group])
    dp.register_message_handler(Cmd_Get_StudentList,
                                commands=['StudentList'],
                                state=Teacher.teacher)
    dp.register_message_handler(Teacher_Get_StudentList,
                                state=Teacher.teacher_get_list_student)
    dp.register_message_handler(Cmd_Delete_Student,
                                commands=['DeleteStudent'],
                                state=Teacher.teacher)
    dp.register_message_handler(Teacher_Delete_Student,
                                state=Teacher.teacher_delete_student)
    dp.register_message_handler(Cmd_Change_Token,
                                commands=['ChangeToken'],
                                state=Teacher.teacher)
    dp.register_message_handler(Teacher_Change_Token,
                                state=Teacher.teacher_change_token)
    dp.register_message_handler(Cmd_Exit,
                                commands=['Exit'],
                                state=Teacher.teacher)
    dp.register_message_handler(No_Cmd_Text,
                                state=Teacher.teacher)