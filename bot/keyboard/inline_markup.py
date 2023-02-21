from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


from bot.db_work import Get_Group_list


async def login_inline_keyboard(): # стартовая илайн клавиатура
    login_ikb = InlineKeyboardMarkup(resize_keyboard=True, inline_keyboard=[
        [InlineKeyboardButton('Cтудент', callback_data='Student_Login'),
         InlineKeyboardButton('Преподаватель ', callback_data='Teacher_Login')],
    ])

    return login_ikb


async def signup_inline_keyboard(): # стартовая илайн клавиатура
    signup_ikb = InlineKeyboardMarkup(resize_keyboard=True, inline_keyboard=[
        [InlineKeyboardButton('Cтудент', callback_data='Student_SignUp'),
         InlineKeyboardButton('Преподаватель ', callback_data='Teacher_SignUp')],
    ])

    return signup_ikb


async def student_delete_or_login_inline_keyboard():
    choice_ikb = InlineKeyboardMarkup(resize_keyboard=True, inline_keyboard=[
        [InlineKeyboardButton('Удалить старый профиль.', callback_data='Delete_profile_student'),
         InlineKeyboardButton('Войти в свой профиль.', callback_data='Student_Login')],
    ])

    return choice_ikb


async def teacher_delete_or_login_inline_keyboard():
    choice_ikb = InlineKeyboardMarkup(resize_keyboard=True, inline_keyboard=[
        [InlineKeyboardButton('Удалить старый профиль.', callback_data='Delete_profile_teacher'),
         InlineKeyboardButton('Войти в свой профиль.', callback_data='Teacher_Login')],
    ])

    return choice_ikb


async def signup_or_create_account():
    choice_ikb = InlineKeyboardMarkup(resize_keyboard=True, inline_keyboard=[
        [InlineKeyboardButton('Создать профиль преподователя.', callback_data='Teacher_SignUp'),
         InlineKeyboardButton('Войти в акканут студента.', callback_data='Student_Login')],
        [InlineKeyboardButton('Открыть меню.', callback_data='Menu')]
    ])

    return choice_ikb


async def student_change_manual_or_task():
    change_ikb = InlineKeyboardMarkup(resize_keyboard=True, inline_keyboard=[
        [InlineKeyboardButton('1', callback_data='1'),
         InlineKeyboardButton('2', callback_data='2')],
        [InlineKeyboardButton('3', callback_data='3'),
         InlineKeyboardButton('4', callback_data='4')],
        [InlineKeyboardButton('5', callback_data='5'),
         InlineKeyboardButton('6', callback_data='6')],
    ])

    return change_ikb



async def list_group_inline_keyboard(): # инлайн клавиатура списка групп предлагающася студенту у которого уже есть аккаунт
    flag = 0
    group_ikb = InlineKeyboardMarkup(resize_keyboard=True)
    group_list = await Get_Group_list()
    for el in group_list:
        if not flag:
            group_ikb.add(InlineKeyboardButton(text=el, callback_data=el))
            flag += 1
        else:
            group_ikb.insert(InlineKeyboardButton(text=el, callback_data=el))
            flag -= 1

    return group_ikb