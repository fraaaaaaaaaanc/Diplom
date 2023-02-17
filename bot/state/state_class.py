from aiogram.dispatcher.filters.state import StatesGroup, State


class Student(StatesGroup):
    student = State()


class Student_SignUp_State(StatesGroup):
    Student_Inpout_Group = State()
    Student_Inpout_Name = State()
    Student_Inpout_Password = State()
    Student_SignUp_End = State()


class Student_LogIn_State(StatesGroup):

     Student_Сhoice_Group = State()
     Student_Inpout_Name = State()
     Student_Inpout_Password = State()


class Teacher(StatesGroup):

    teacher = State()


class Teacher_SignUp_State(StatesGroup):

    Teacher_SignUp_Start = State()
