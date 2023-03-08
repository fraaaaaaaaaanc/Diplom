import subprocess
from subprocess import check_output

from bot.db_work import Get_Test_DB
from ..misk import delete_file, create_file, compilation_file
import time


async def test_task1(state):

    error_list = '"Не прошло тесты для чисел '

    async with state.proxy() as data:
        await create_file(data['file_path'], data['number_lab'])

        res_compilation = await compilation_file(state)
        time.sleep(25)

        if res_compilation:
            return res_compilation

        test_list = await Get_Test_DB(state)
        for tuple in test_list:
            command = f"C:\\pythonProject\\Main_Diplom\\{data['user_chat_id']}.exe {tuple[0]} {tuple[1]} {tuple[2]}"
            try:
                if not check_output(command, encoding='UTF-8', timeout=10) == tuple[3]:
                    error_list += f'({tuple[0]}, {tuple[1]}, {tuple[2]})" ,'
                    return error_list
            except subprocess.TimeoutExpired:
                return "'При выполнении вашей программы сработал таймаут.'"
            except Exception:
                return "'Ошибка компиляции файла.'"
        return 0


async def test_task10(state):

    error_list = '"Не прошло тесты для чисел '

    async with state.proxy() as data:
        await create_file(data['file_path'], data['number_lab'])

        res_compilation = await compilation_file(state)

        if res_compilation:
            return res_compilation

        test_list = await Get_Test_DB(state)
        for tuple in test_list:
            try:
                command = f"C:\\pythonProject\\Main_Diplom\\a.exe {tuple[0]} {tuple[1]} {tuple[2]}"
                if not check_output(command, encoding='UTF-8', timeout=10) == tuple[3]:
                    print(check_output(command, encoding='UTF-8', timeout=10))
                    error_list += f"({tuple[0]}, {tuple[1]}, {tuple[2]}), "
                    return error_list
            except subprocess.TimeoutExpired:
                return '"При выполнении вашей программы сработал таймаут."'
        return 0


async def lab1(state):

    tasks = {
        '1': test_task1,
        '10': test_task1
    }

    async with state.proxy() as data:
        task = data['number_task']

    result_test = await tasks[task](state)
    await delete_file(data['file_path'])

    return result_test