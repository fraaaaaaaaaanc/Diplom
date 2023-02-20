from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


async def Main_Student_Menu():
    menu_student = ReplyKeyboardMarkup(resize_keyboard=True,
                                       keyboard=[
        [KeyboardButton('/GetTask'), KeyboardButton('/GetManual')],
        [KeyboardButton('/CheckLab'), KeyboardButton('/Exit')]
    ])

    return menu_student


async def Main_Teacher_Menu():
    menu_teacher = ReplyKeyboardMarkup(resize_keyboard=True,
                                       keyboard=[
        [KeyboardButton('/AddGroup'), KeyboardButton('/DeleteGroup'), KeyboardButton('/GroupList')],
        [KeyboardButton('/StudentList'), KeyboardButton('/DeleteStudent'), KeyboardButton('/ChangeToken')],
        [KeyboardButton('/Exit')]
                                       ])

    return menu_teacher


async def Main_Menu():
    main_menu = ReplyKeyboardMarkup(resize_keyboard=True,
                                    keyboard=[
        [KeyboardButton('/LogIn'), KeyboardButton('/SignUp')]
                                    ])

    return main_menu