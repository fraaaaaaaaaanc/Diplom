from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def login_inline_keyboard(): # стартовая илайн клавиатура
    login_ikb = InlineKeyboardMarkup(resize_keyboard=True, inline_keyboard=[
        [InlineKeyboardButton('Cтудент', callback_data='Student'),
         InlineKeyboardButton('Преподаватель ', callback_data='Teacher')],
    ])

    return login_ikb


def list_group_inline_keyboard(): # инлайн клавиатура списка групп предлагающася студенту у которого уже есть аккаунт
    flag = 0
    group_ikb = InlineKeyboardMarkup(resize_keyboard=True)
    group_list = Get_List_Date_Table('group', 'Group_students')
    for el in group_list:
        if not flag:
            group_ikb.add(InlineKeyboardButton(text=el, callback_data=el))
            flag += 1
        else:
            group_ikb.insert(InlineKeyboardButton(text=el, callback_data=el))
            flag -= 1

    return group_ikb