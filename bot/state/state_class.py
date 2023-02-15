from aiogram.dispatcher.filters.state import StatesGroup, State


class Student(StatesGroup):
    student = State()


class Student_SignUp_State(StatesGroup):
    Student_SignUp = State()