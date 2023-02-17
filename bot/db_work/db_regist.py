import sqlite3 as sq


async def db_start():  # Подключение к базе дыннх и создание таблиц
    global db, cur

    db = sq.connect('DIPLOM.db')
    cur = db.cursor()


    cur.execute("CREATE TABLE IF NOT EXISTS Group_students(id INTEGER PRIMARY KEY, 'group' TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS Students_info(id INTEGER PRIMARY KEY, user_chat_id INTEGER, 'group' TEXT, name TEXT, password TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS Teacher_profile(id INTEGER PRIMARY KEY, user_chat_id INTEGER, name TEXT, password TEXT)")
    cur.execute(f"CREATE TABLE IF NOT EXISTS 'ИДБ-19-01' (id INTEGER PRIMARY KEY, user_chat_id INTEGER, student_name TEXT)")

    db.commit()


async def Search_date_DB(column, name_table, data_column): # функция проверяющая есть ли аккаунт у пользователя начавшего работу с ботом
    if cur.execute(f"""SELECT "{column}" FROM '{name_table}' WHERE "{column}" == '{data_column}'""").fetchall():
        return True
    # cur.execute(f"""INSERT INTO Students_info ("user_chat_id") VALUES ('{user_id}')""")
    # db.commit()
    return False


async def Search_userId_date_DB(name_table, column, user_id, data_column):
    if cur.execute(f"""SELECT * FROM '{name_table}' WHERE "user_chat_id" == '{user_id}' and "{column}" == '{data_column}'""").fetchone():
        return True
    return False


async def Get_Group_list(column, table): # функция выдающая список групп
    group_list = []
    result = cur.execute(f"""SELECT "{column}" FROM '{table}'""").fetchall()
    for row in result:
        group_list.append(row[0])

    return group_list


async def Add_New_Profile_Student(state): #  добавляет аккаунт студента в бд
    async with state.proxy() as data:
        cur.execute(f"""INSERT INTO Students_info ("user_chat_id", "group", "name", "password") VALUES 
                   ('{data['user_id']}', '{data['group']}', '{data['student_name']}', '{data['password']}')""")
        cur.execute(f"""INSERT INTO '{data['group'].upper()}' ("student_name") VALUES ('{data['student_name']}')""")
        if cur.execute(f"""SELECT * FROM Students_info WHERE "user_chat_id" == '{data['user_id']}' and 
        "group" == '{data['group']}' and
        "name" == '{data['student_name']}' and
        "password" == '{data['password']}'""").fetchall():
            db.commit()
            return (f'Отлично! Вы добавлены в группу {data["group"].upper()}, под именем {data["student_name"]}!\n'
                    f'Теперь вы можете пользоваться функциями бота.')
        return False


async def Delete_Record(table, column, data):
    cur.execute(f"""DELETE from '{table}' WHERE '{column}' == '{data}'""").fetchall()
    db.commit()


