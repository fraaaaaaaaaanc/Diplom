

description = {
    'lab1': {
        'task1': """
        Для того чтобы приступить к проверки вашего задания, создайте новый файл си, скопируйте логику решения из вашего \
файла и вставьте его в эту конструкцию вместо "...", Важно! Ваша программа должна выводить "Да", если В больше остальных \
чисел, и "Нет" если В меньше хотя бы одного числа.\n
#include "hed.h"
#include <stdio.h>

int funk(int A, int B, int C)
{
 ...
}
Послего чего, просто отправьте новый файл сюда."""
}
}


async def get_description(state):
    async with state.proxy() as data:
        lab = data['number_lab']
        task = data['number_task']

    return description['lab' + lab]['task' + task]
