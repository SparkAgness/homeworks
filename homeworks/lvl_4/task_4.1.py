# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:
import sqlite3
 
def TableView():
    con = sqlite3.connect('teatchers.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM Students")
    con.commit()
    return cur.fetchall()
    
 
def TableCreator():
    try:
        con = sqlite3.connect('teatchers.db')
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS Students(Student_ID INT UNIQUE, Student_NAME TEXT NOT NULL, School_ID INT PRIMARY KEY)""")
        con.commit()
        con.close()
    except (Exception, sqlite3.Error) as error:
        print(f"Error: {error}")
 
def TableFill(my_values):
    try:
        con = sqlite3.connect('teatchers.db')
        cur = con.cursor();
        cur.execute("""INSERT INTO Students VALUES (?, ?, ?)""", my_values)
        con.commit()
        con.close()
    except (Exception, sqlite3.Error) as error:
        print(f"Error: {error}")
 
def Join(id):
    try:
        con = sqlite3.connect('teatchers.db')
        cur = con.cursor()
        id_rec = 'SELECT Student_ID, Student_Name, School.School_Id, School.School_name FROM Students JOIN School ON Students.School_id = School.School_id WHERE Student_ID = ?'
        cur.execute(id_rec, (id,))
        info = cur.fetchone()
        print(f"Student' ID: {info[0]}")
        print(f"Name: {info[1]}")
        print(f"School ID: {info[2]}")
        print(f"School's title: {info[3]}")         
    except (Exception, sqlite3.Error) as error:
        print(f"Error: {error}")
 

my_values = (
    (202, 'Петр', 2),
    (201, 'Иван', 1),
    (203, 'Анастасия', 3),
    (204, 'Игорь', 4))
TableCreator()
for value in my_values:
    TableFill(value)
Join(int(input('Input student\'s id ')))
