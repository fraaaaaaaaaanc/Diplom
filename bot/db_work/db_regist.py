import sqlite3 as sq


async def db_start():  # Подключение к базе дыннх и создание таблиц
    global db, cur

    db = sq.connect('DIPLOM.db')
    cur = db.cursor()


    cur.execute("CREATE TABLE IF NOT EXISTS Group_students(id INTEGER PRIMARY KEY, 'group' TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS Students_info(id INTEGER PRIMARY KEY, user_chat_id INTEGER, 'group' TEXT, name TEXT, password TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS Teacher_profile(id INTEGER PRIMARY KEY, user_chat_id INTEGER, name TEXT, password TEXT)")

    db.commit()


async def Search_One_Data_In_DB(column, name_table, data_column): # функция проверяющая есть ли аккаунт у пользователя начавшего работу с ботом
    if cur.execute(f"""SELECT "{column}" FROM '{name_table}' WHERE "{column}" == '{data_column}'""").fetchall():
        return True
    # cur.execute(f"""INSERT INTO Students_info ("user_chat_id") VALUES ('{user_id}')""")
    # db.commit()
    return False