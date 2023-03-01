import os

from aiogram.dispatcher import FSMContext
import subprocess
from subprocess import check_output
from bot.db_work import Get_Test_DB
from ..misk import create_file, delete_file


async def test_task1(state):

    error_list = 'Не прошло тесты для массива '

    async with state.proxy() as data:
        await create_file(data['file_path'], data['number_lab'])

        command = f"gcc {data['file_path']} C:\\pythonProject\\Main_Diplom\\Test_Package\\lab1\\documents\\text.c"
        subprocess.call(command, shell=True)

        test_list = await Get_Test_DB(state)
        for tuple in test_list:
            command = f"C:\\pythonProject\\Main_Diplom\\a.exe {tuple[0]}"
            try:
                if not check_output(command, encoding='UTF-8', timeout=10) == tuple[1]:
                    error_list += f"({tuple[0]}), "
                    return error_list
            except subprocess.TimeoutExpired:
                return "'При выполнении вашей программы сработал таймаут.'"
            except "error":
                return "'Ошибка компиляции файла.'"
        return 0



async def lab2(state):

    tasks = {
        '1': test_task1
    }

    async with state.proxy() as data:
        task = data['number_task']

    result_test = await tasks[task](state)
    return result_test