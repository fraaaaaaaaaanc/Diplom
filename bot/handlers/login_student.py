from aiogram import types, Dispatcher


from ..state import Student_SignUp_State, list_group_inline_keyboard
from ..db_work import Search_One_Data_In_DB


async def Login_Student(callback: types.CallbackQuery):
    if await Search_One_Data_In_DB('user_chat_id', 'Students_info', callback.from_user.id):
        await callback.message.edit_text('Вы уже авторизированны. Для продолжения работы выберете свою группу!',
                             reply_markup=list_group_inline_keyboard())
        await Student_SignUp_State.Student_SignUp.set()
    else:
        await callback.message.edit_text('У вас нет профиля в данном боте('
                             'Для того чтобы начать работу с ним, вам нужно авторизироваться!'
                             'Отправьте команду /SignUp для начала авторизации.')
        await Student_Login_State.Student_Login_Group_State.set()