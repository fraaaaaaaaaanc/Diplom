import os
import openpyxl
from openpyxl import load_workbook

from bot.state import Student


Main_Student_Menu_Text =  '''
<b>/GetTask</b> - <em>Команда для получения задания на лабораторную работу.</em>
<b>/GetManual</b> - <em>Команда для получения методического материала по лабороторной работе.</em>
<b>/CheckLab</b> - <em>Команда для проверки лабораторных работ.</em>
<b>/ChangeName</b> - <em>Команда для изменения фамилии и имени.</em>
<b>/Stop</b> - <em>Команда которая остановит команду выбранную вами ранее.</em>
<b>/Exit</b> - <em>Команда для выхода из профиля.</em>
'''


List_Student_State = [
    Student.student_get_task,
    Student.student_get_manual,
    Student.student_change_name,
    Student.student_input_lab_number,
    Student.student_send_file,
    Student.test_file
]

async def Get_File_Path(file_name, state):
    async with state.proxy() as data:
        destination_dir = f'C:\\pythonProject\\Main_Diplom\\Test_Package\\' \
                          f'lab{data["number_lab"]}\\documents'
        file_name = file_name
        file_path = os.path.join(destination_dir, file_name)

    return file_path

