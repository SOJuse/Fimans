import sqlite3


def Read_Login_db():
    try:
        connection = sqlite3.connect('Fimans_python.db')
        cursor = connection.cursor()
        print("Подключен к бд")
        cursor.execute("SELECT * FROM Login_db")
        data = cursor.fetchall()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if connection:
            connection.close()
            print("Соединение с SQLite закрыто")
            return data


def Write_Login_db(local_mail, local_password):
    try:
        connection = sqlite3.connect('Fimans_python.db')
        cursor = connection.cursor()
        print("Подключен к бд")
        cursor.execute("SELECT ID FROM Login_db")
        f = cursor.fetchall()
        ids = []
        for i in f:
            ids.append(i[0])
        ids.sort(reverse=True)
        id = ids[0] + 1
        print(id)
        values = (id, local_mail, local_password)
        # values = (0, '-', '-')
        sql = "INSERT INTO Login_db(ID,Mail,Password) VALUES (?, ?, ?)"
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if connection:
            connection.close()
            print("Соединение с SQLite закрыто")


def Change_Login_db(id, local_mail, local_password):
    try:
        connection = sqlite3.connect('Fimans_python.db')
        cursor = connection.cursor()
        print("Подключен к бд")
        values = (id, local_mail, local_password)
        sql = "REPLACE INTO Login_db(ID,Mail,Password) VALUES (?, ?, ?)"
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if connection:
            connection.close()
            print("Соединение с SQLite закрыто")


def Write_History_db(id, date, category, price):
    try:
        connection = sqlite3.connect('Fimans_python.db')
        cursor = connection.cursor()
        print("Подключен к бд")
        values = (id, date, category, price)
        sql = "INSERT INTO History_db(ID,Date,Category,Price) VALUES (?, ?, ?, ?)"
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if connection:
            connection.close()
            print("Соединение с SQLite закрыто")


def Read_History_db(id):
    try:
        connection = sqlite3.connect('Fimans_python.db')
        cursor = connection.cursor()
        print("Подключен к бд")
        cursor.execute(f"""SELECT * FROM History_db WHERE ID = {id}""")
        data = cursor.fetchall()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if connection:
            connection.close()
            print("Соединение с SQLite закрыто")
            return data


def Write_Payments_db(id, date, category, price):
    try:
        connection = sqlite3.connect('Fimans_python.db')
        cursor = connection.cursor()
        print("Подключен к бд")
        values = (id, date, category, price)
        sql = "INSERT INTO Payments_db(ID,Date,Category,Price) VALUES (?, ?, ?, ?)"
        cursor.execute(sql, values)
        connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if connection:
            connection.close()
            print("Соединение с SQLite закрыто")


def Read_Payments_db(id):
    try:
        connection = sqlite3.connect('Fimans_python.db')
        cursor = connection.cursor()
        print("Подключен к бд")
        cursor.execute(f"""SELECT * FROM Payments_db WHERE ID = {id}""")
        data = cursor.fetchall()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if connection:
            connection.close()
            print("Соединение с SQLite закрыто")
            return data


def Read_paths_graphics():
    with open('paths_graphics.txt') as f:
        s = f.readline().split('|')[:-1]
        return s


def Write_paths_graphics(x):
    with open('paths_graphics.txt', mode='w') as f:
        for i in x:
            f.write(i + '|')
