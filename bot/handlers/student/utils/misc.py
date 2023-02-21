from bot.state import Student


Main_Student_Menu_Text =  '''
<b>/GetTask</b> - <em>Команда для получения задания на лабораторную работу.</em>
<b>/GetManual</b> - <em>Команда для получения методического материала по лабороторной работе.</em>
<b>/CheckLab</b> - <em>Команда для проверки лабораторных работ.</em>
<b>/Stop</b> - <em>Команда которая остановит команду выбранную вами ранее.</em>
<b>/Exit</b> - <em>Команда для выхода из профиля.</em>
'''


List_Student_State = [
    Student.student_get_task,
    Student.student_get_manual,
    Student.student_check_lab
]