TOKEN_Teacher = '000'
from bot.state import Teacher
from openpyxl import load_workbook


Main_Teacher_Menu_Text =  '''
<b>/AddGroup</b> - <em>Команда для добавления новой группы в список групп.</em>
<b>/DeleteGroup</b> - <em>Команда для удаления группы из списка групп.</em>
<b>/GroupList</b> - <em>Команда для получения списка групп.</em>
<b>/StudentList</b> - <em>Команда для получения списка группы.</em>
<b>/DeleteStudent</b> - <em>Команда для удаления студента.</em>
<b>/ChangeToken</b> - <em>Команда для изменения токена.</em>
<b>/GetExcel</b> - <em>Команда для получения excel файла, со списком студентов в выбранной группы и информацией о
состоянии проверки их лабораторных работ.</em>
<b>/Stop</b> - <em>Команда которая остановит команду выбранную вами ранее.</em>
<b>/Exit</b> - <em>Команда для выхода из профиля.</em>
'''


List_State_Teacher = [
    Teacher.teacher_add_group,
    Teacher.teacher_delete_group,
    Teacher.teacher_get_list_student,
    Teacher.teacher_delete_student,
    Teacher.teacher_change_token,
    Teacher.teacher_get_excel_file
    ]





