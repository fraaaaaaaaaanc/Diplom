import os
import subprocess
from subprocess import check_output


error_list = '"Не прошло тесты для чисел '


async def compilation_file(state):

    async with state.proxy() as data:

        command = f"gcc -o {data['user_chat_id']} {data['file_path']} C:\\pythonProject\\Main_Diplom\\Test_Package\\{'lab' + data['number_lab']}" \
                  f"\\documents\\text.c"
        try:
            check_output(command, encoding="UTF-8") 
        except:
            return '"Ошибка компиляции файла!"'
        subprocess.call(command, shell=True)
        return 0


async def delete_file(file_path):
    os.remove(file_path)
    if os.path.isfile('C:\\pythonProject\\Main_Diplom\\a.exe'):
        os.remove('C:\\pythonProject\\Main_Diplom\\a.exe')


async def create_file(file_path, number_lab):

    stroka = f'#include "hed.h"\n'

    with open(f'{file_path}', "r+", encoding="UTF-8") as file:
        for line in file:
            stroka += line

    with open(f"{file_path}", "w", encoding="UTF-8") as file:
        file.write(stroka)