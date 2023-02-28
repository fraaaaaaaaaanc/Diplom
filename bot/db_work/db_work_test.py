import sqlite3 as sq


async def db_start(number):  # Подключение к базе дыннх и создание таблиц
    global db, cur

    db = sq.connect(f'Test_Lab№{number}.db')
    cur = db.cursor()

    return cur


async def Search_Task_DB(state):

    async with state.proxy() as data:
        await db_start(data['number_lab'])
        if cur.execute(f"""SELECT "id" FROM "task_table" 
                       WHERE "id" == '{data['number_task']}'""").fetchall():
            estimation = cur.execute(f"""SELECT estimation FROM "task_table" 
                        WHERE "id" == "{data['number_task']}" """).fetchone()
            db.close()
            return estimation[0]
        db.close()


async def Get_Test_DB(state):

    async with state.proxy() as data:
        await db_start(data['number_lab'])
        test_list = cur.execute(f"""SELECT * FROM task_test_{data['number_task']}""").fetchall()
        return test_list

