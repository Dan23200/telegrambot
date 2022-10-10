import sqlite3

try:
    conn = sqlite3.connect('telebot.db')
    cursor = conn.cursor()

    # создаем пользователя c users_id = 1000
    cursor.execute('CREATE TABLE IF NOT EXISTS table2 (`something` int(2))')
    # cursor.execute('CREATE DATABASE IF NOT EXIST CREATE TABLE IF NOT EXISTS users (`user_id` int(2))', (1000,))
    # cursor.execute("INSERT OR IGNORE INTO 'users' ('user_id') VALUES (?)", (1000,))

    # Считываем всех пользователей
    users = cursor.execute("SELECT * FROM 'users'")
    print(users.fetchall())

    # Подтверждаем изменения
    conn.commit()

except sqlite3.Error as error:
    print('Error', error)

finally:
    if (conn):
        conn.close()
