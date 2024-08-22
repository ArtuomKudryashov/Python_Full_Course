import sqlite3
import os
import time

DB_NAME = "sqlite_db.db"

with sqlite3.connect(DB_NAME) as sqlite_conn:
    print(sqlite_conn)
    print(sqlite3.sqlite_version)

print("<<<<<<<<<<<<<<<<<create new table>>>>>>>>>>>>>>>>>>>>>>")
with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = """Create Table if not exists courses (
    id integer PRIMARY KEY,
     title text NOT NULL,
     students_qty integer,
     reviews_qty integer
     );"""
    sqlite_conn.execute(sql_request)


courses = [
    (352,"JavaScript course", 415, 100),
    (614,"C++ course", 161, 10),
    (721,"Python course", 100, 35),
    (251,"Math course", 100, 30)
]
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sqlite_conn.execute("DELETE FROM courses")
#     sqlite_conn.commit()
# print("<<<<<<<<<<<<<<Connecting to the database and added records>>>>>>>>>>>>>>>>>>")
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = "INSERT INTO courses VALUES(?,?,?,?)"
#     sqlite_conn.execute(sql_request,(252,"Python course", 100, 30))
#     for course in courses:
#         sqlite_conn.execute(sql_request, course)
#     sqlite_conn.commit()


# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sqlite_conn.execute("DELETE FROM courses")
#     sqlite_conn.commit()
#
#
print("<<<<<<<<<<reading from  DB>>>>>>>>>>>>>>>")

with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = "Select * From courses"
    sql_cursor = sqlite_conn.execute(sql_request)
    for record in sql_cursor:
        print(record)
        print(record[1])


time.sleep(2)
if os.path.exists(DB_NAME):
    try:

        os.remove(DB_NAME)  # Удаляем файл
        print(f"База данных '{DB_NAME}' успешно удалена.")
    except PermissionError as e:
        print(f"Ошибка при удалении базы данных: {e}")
else:
    print(f"База данных '{DB_NAME}' не найдена.")

# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sqlite_conn.execute("DELETE FROM courses")
#     sqlite_conn.commit()