import sqlite3 as sq


async def db_start():  # Подключение к базе дыннх и создание таблиц
    global db, cur

    db = sq.connect('DIPLOM.db')
    cur = db.cursor()

    return cur
    # cur.execute("CREATE TABLE IF NOT EXISTS Group_students(id INTEGER PRIMARY KEY, 'group' TEXT)")
    # cur.execute("CREATE TABLE IF NOT EXISTS Students_info(id INTEGER, user_chat_id INTEGER, 'group' TEXT, name TEXT, password TEXT)")
    # cur.execute("CREATE TABLE IF NOT EXISTS Teacher_profile(id INTEGER PRIMARY KEY, user_chat_id INTEGER, name TEXT, password TEXT)")
    # cur.execute("CREATE TABLE IF NOT EXISTS TOKEN(id INTEGER PRIMARY KEY, 'TOKEN' TEXT)")
    #
    # db.commit()
    # db.close()


# async def Close_DB():
#     db.close()


async def Search_date_DB(column, name_table, data_column): # функция проверяющая есть ли аккаунт у пользователя начавшего работу с ботом

    cur = await db_start()

    if cur.execute(f"""SELECT "{column}" FROM '{name_table}' WHERE "{column}" == '{data_column}'""").fetchall():
        db.close()
        return True
    db.close()
    return False




async def Search_userId_date_DB(name_table, column, user_id, data_column):

    cur = await db_start()

    if cur.execute(f"""SELECT * FROM '{name_table}' 
                   WHERE "user_chat_id" == '{user_id}' and "{column}" == '{data_column}'""").fetchone():
        db.close()
        return True
    db.close()
    return False


async def Get_Group_list(): # функция выдающая список групп

    cur = await db_start()

    group_list = []
    result = cur.execute(f"""SELECT "group" FROM Group_students""").fetchall()
    for row in result:
        group_list.append(row[0])

    db.close()
    return group_list


async def Add_New_Profile_Student(state): #  добавляет аккаунт студента в бд

    cur = await db_start()

    async with state.proxy() as data:
        cur.execute(f"""INSERT INTO Students_info ("user_chat_id", "group", "name", "password") VALUES 
                   ('{data['user_id']}', '{data['group']}', '{data['student_name']}', '{data['password']}')""")
        db.commit()
        db.close()
        return (f'Отлично! Вы добавлены в группу {data["group"].upper()}, под именем {data["student_name"]}!\n'
                    f'Для того чтобы узнать команды бота доступные студенту отправьте команду /Help.')



async def Add_New_Profile_Teacher(state):

    cur = await db_start()

    async with state.proxy() as data:
        cur.execute(f"""INSERT INTO Teacher_profile ("user_chat_id", "name", "password") VALUES 
                   ('{data['user_id']}', '{data['teacher_login']}', '{data['teacher_password']}')""")
        db.commit()
        db.close()
        return (f'Отлично! Вы создали акканут преподователя.'
                f'Чтобы узнать команды бота, отправьте команду /Help')


async def Delete_Record(table, column, data):

    cur = await db_start()

    cur.execute(f"""DELETE from {table} WHERE "{column}" == '{data}'""").fetchall()
    db.commit()
    db.close()


async def Add_Group(data):

    cur = await db_start()

    if not cur.execute(f"""SELECT "group" FROM Group_students WHERE "group" == '{data}'""").fetchall():
        cur.execute(f"""INSERT INTO Group_students ('group') VALUES ('{data}')""")
        db.commit()
        db.close()
        return True
    db.close()
    return False


async def Delete_Group(data):

    cur = await db_start()

    if cur.execute(f"""SELECT "group" FROM Group_students WHERE "group" == '{data}'""").fetchone():
        await Delete_Record('Group_students', 'group', data)
        db.close()
        return True
    db.close()
    return False


async def Delete_Student(data):

    cur = await db_start()

    if cur.execute(f"""SELECT "name" FROM Students_info WHERE "name" == '{data}'""").fetchone():
        await Delete_Record('Students_info', 'name', data)
        db.close()
        return True
    db.close()
    return False


async def Get_StudentList(data):

    cur = await db_start()

    if await Search_date_DB("group", 'Group_students', data):
        students_list = cur.execute(f"""SELECT "name" FROM Students_info WHERE "group" == '{data}'""").fetchall()
        db.close()
        return students_list
    db.close()
    return False


async def Change_Token(data):

    cur = await db_start()

    cur.execute(f"""UPDATE TOKEN SET "TOKEN" = '{data}'""")
    db.commit()
    db.close()


async def Change_Name(data):

    cur = await db_start()

    cur.execute(f"""UPDATE Students_info SET "name" = '{data}'""")
    db.commit()
    db.close()


async def Get_Record(table, column, data):

    cur = await db_start()

    record = cur.execute(f"""SELECT "{column}" FROM "{table}" WHERE "user_chat_id" == '{data}'""").fetchone()
    db.close()
    return record[0]




