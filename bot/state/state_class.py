from aiogram.dispatcher.filters.state import StatesGroup, State


class Student(StatesGroup):

    student = State()


class Student_LogIn_State(StatesGroup):

    Student_Inpout_Name = State()
    Student_Inpout_Password = State()
    Student_End_Login = State()


class Student_SignUp_State(StatesGroup):

    Student_Inpout_Group = State()
    Student_Inpout_Name = State()
    Student_Inpout_Password = State()
    Student_SignUp_End = State()


class Teacher(StatesGroup):

    teacher = State()
    teacher_add_group = State()
    teacher_delete_group = State()
    teacher_get_list_student = State()
    teacher_delete_student = State()


class Teachet_LogIn_State(StatesGroup):

    Teacher_Input_Login = State()
    Teacher_Inpout_Password = State()
    Teacher_End_Login = State()

class Teacher_SignUp_State(StatesGroup):

    Teacher_Input_Login = State()
    Teacher_Inpout_Password = State()
    Teacher_End_SignUp = State()
