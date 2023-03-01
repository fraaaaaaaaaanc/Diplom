import os


async def delete_file(file_path):
    os.remove(file_path)
    os.remove('C:\\pythonProject\\Main_Diplom\\a.exe')


async def create_file(file_path, number_lab):

    stroka = f'#include "hed.h"\n'

    with open(f'{file_path}', "r+", encoding="UTF-8") as file:
        for line in file:
            stroka += line

    with open(f"{file_path}", "w", encoding="UTF-8") as file:
        file.write(stroka)