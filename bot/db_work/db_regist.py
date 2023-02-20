import sqlite3 as sq


async def db_start():  # Подключение к базе дыннх и создание таблиц
    global db, cur

    db = sq.connect('DIPLOM.db')
    cur = db.cursor()


    cur.execute("CREATE TABLE IF NOT EXISTS Group_students(id INTEGER PRIMARY KEY, 'group' TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS Students_info(id INTEGER PRIMARY KEY, user_chat_id INTEGER, 'group' TEXT, name TEXT, password TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS Teacher_profile(id INTEGER PRIMARY KEY, user_chat_id INTEGER, name TEXT, password TEXT)")

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


async def Get_Group_list(): # функция выдающая список групп
    group_list = []
    result = cur.execute(f"""SELECT "group" FROM Group_students""").fetchall()
    for row in result:
        group_list.append(row[0])

    return group_list


async def Add_New_Profile_Student(state): #  добавляет аккаунт студента в бд
    async with state.proxy() as data:
        cur.execute(f"""INSERT INTO Students_info ("user_chat_id", "group", "name", "password") VALUES 
                   ('{data['user_id']}', '{data['group']}', '{data['student_name']}', '{data['password']}')""")
        db.commit()
        return (f'Отлично! Вы добавлены в группу {data["group"].upper()}, под именем {data["student_name"]}!\n'
                    f'Для того чтобы узнать команды бота доступные студенту отправьте команду /Help.')


async def Add_New_Profile_Teacher(state):
    async with state.proxy() as data:
        cur.execute(f"""INSERT INTO Teacher_profile ("user_chat_id", "name", "password") VALUES 
                   ('{data['user_id']}', '{data['teacher_login']}', '{data['teacher_password']}')""")
        db.commit()
        return (f'Отлично! Вы создали акканут преподователя.'
                f'Чтобы узнать команды бота, отправьте команду /Help')


async def Delete_Record(table, column, data):
    cur.execute(f"""DELETE from {table} WHERE "{column}" == '{data}'""").fetchall()
    db.commit()


async def Add_Group(data):
    if not cur.execute(f"""SELECT "group" FROM Group_students WHERE "group" == '{data}'""").fetchall():
        cur.execute(f"""INSERT INTO Group_students ('group') VALUES ('{data}')""")
        db.commit()
        return True
    return False


async def Delete_Group(data):
    if cur.execute(f"""SELECT "group" FROM Group_students WHERE "group" == '{data}'""").fetchone():
        await Delete_Record('Group_students', 'group', data)
        return True
    return False


async def Delete_Student(data):
    if cur.execute(f"""SELECT "name" FROM Students_info WHERE "name" == '{data}'""").fetchone():
        await Delete_Record('Students_info', 'name', data)
        return True
    return False


async def Get_StudentList(data):
    if await Search_date_DB("group", 'Group_students', data):
        students_list = cur.execute(f"""SELECT "name" FROM Students_info WHERE "group" == '{data}'""").fetchall()
        return students_list
    return False


async def Close_DB():
    db.close()



