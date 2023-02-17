from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


from bot.db_work import Get_Group_list


async def login_inline_keyboard(): # стартовая илайн клавиатура
    login_ikb = InlineKeyboardMarkup(resize_keyboard=True, inline_keyboard=[
        [InlineKeyboardButton('Cтудент', callback_data='Student'),
         InlineKeyboardButton('Преподаватель ', callback_data='Teacher')],
    ])

    return login_ikb


async def signup_inline_keyboard(): # стартовая илайн клавиатура
    signup_ikb = InlineKeyboardMarkup(resize_keyboard=True, inline_keyboard=[
        [InlineKeyboardButton('Cтудент', callback_data='Student_SignUp'),
         InlineKeyboardButton('Преподаватель ', callback_data='Teacher_SignUp')],
    ])

    return signup_ikb


async def delete_or_login_inline_keyboard():
    choice_ikb = InlineKeyboardMarkup(resize_keyboard=True, inline_keyboard=[
        [InlineKeyboardButton('Удалить старый профиль.', callback_data='Delete_profile'),
         InlineKeyboardButton('Войти в свой профиль.', callback_data='Student_Login')],
    ])

    return choice_ikb


async def list_group_inline_keyboard(): # инлайн клавиатура списка групп предлагающася студенту у которого уже есть аккаунт
    flag = 0
    group_ikb = InlineKeyboardMarkup(resize_keyboard=True)
    group_list = await Get_Group_list('group', 'Group_students')
    for el in group_list:
        if not flag:
            group_ikb.add(InlineKeyboardButton(text=el, callback_data=el))
            flag += 1
        else:
            group_ikb.insert(InlineKeyboardButton(text=el, callback_data=el))
            flag -= 1

    return group_ikb