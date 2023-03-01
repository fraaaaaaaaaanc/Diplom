from .lab1 import lab1
from .lab2 import lab2


async def test_start(state):

    labs = {
        '1': lab1,
        '2': lab2
    }

    async with state.proxy() as data:
        lab = data['number_lab']

    return await labs[lab](state)




    # stroka = f'#include "hed.h"\n'
    #
    # with open(f'{file_c}', "r+", encoding="UTF-8") as file:
    #     for line in file:
    #         stroka += line
    #
    # with open("C:\\pythonProject\\Main_Diplom\\Test_Package\\test_lab\\documents\\test.c", "w",
    #           encoding="UTF-8") as file:
    #     file.write(stroka)
    #
    # command = f"gcc test.c text.c"
    # subprocess.call(command, shell=True)

    # def free_library(handle):
    #     kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
    #     kernel32.FreeLibrary.argtypes = [ctypes.wintypes.HMODULE]
    #     kernel32.FreeLibrary(handle)



















    # lib = ctypes.CDLL("C:\\pythonProject\\Main_Diplom\\Test_Package\\documents\\libtest.so")
    #
    # async with state.proxy() as data:
    #     lab = data['number_lab']
    #
    # quantity_true_test = await labs[lab](state, test_list, lib)
    # free_library(lib._handle)
    #
    # сommand = "del C:\\pythonProject\\Main_Diplom\\Test_Package\\documents\\libtest.so;" \
    #           f"del {file_c}"
    # res = subprocess.call(сommand, shell=True)
    #
    # if quantity_true_test == len(test_list):
    #     return 'Тесты пройдены успешно, ваше задание выполнено верно.'
    # return 'Ваше задание не прошло тесты( Попробуйте решить его по другому.'

