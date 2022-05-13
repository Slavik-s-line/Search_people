import sqlite3

db_name = 'information.db'
conn = None
cursor = None


def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()


def close():
    cursor.close()
    conn.close()


def do(query):
    cursor.execute(query)
    conn.commit()


def clear_db():
    open()
    query = '''DROP TABLE IF EXISTS military'''
    do(query)
    close()


def create():
    open()
    cursor.execute('''PRAGMA foreign_keys=on''')

    do("""CREATE TABLE IF NOT EXISTS military(
    Name TEXT,
    Surname TEXT,
    Birthday_year INTEGER,
    Rank TEXT,
    Type_of_army TEXT,
    Awards TEXT,
    Place_of_duty TEXT);""")

    close()


def add_peoples():
    peoples = [('Олександр', 'Паркер', 2000, 'Капітан', 'Сухопутні війська', 'Герой України', 'Харків'),
               ('Максим', 'Іванов', 1990, 'Офіцер', 'Сухопутні війська', 'Медаль «10 років сумлінної служби»',
                'Гостомель'),
               ('Володимир', 'Богач', 1988, 'Солдат', 'Сухопутні війська', 'Немає', 'Херсон'),
               ('Іван', 'Коваль', 1978, 'Старший сержант', 'Сухопутні війська', 'Нагрудний знак «Учасник АТО»', 'Гуляйполе'),
               ('Ігор', 'Рубан', 1998, 'Лейтенант', 'Десантно-штурмові війська', 'Почесний десантник', 'Донецьк'),
               ('Георгій', 'Ткач', 1987, 'Полковник', 'Сухопутні війська', 'Медаль «10 років сумлінної служби»', 'Одеса'),
               ('Євген', 'Ковтун', 1970, 'Адмірал', 'Військово-морські сили', 'Герой України', 'Одеса'),
               ('Віктор', 'Маляр', 1965, 'Генерал-майор', 'Десантно-штурмові війська', 'Медаль «20 років сумлінної служби»', 'Житомир'),
               ('Володимир', 'Маляр', 1965, 'Полковник', 'Десантно-штурмові війська', 'Медаль «За воїнську доблесть»', 'Київ'),
               ('Олег', 'Мельник', 1995, 'Матрос', 'Військово-морські сили', 'Герой України', 'Маріуполь')]
    open()
    cursor.executemany("INSERT INTO military VALUES(?, ?, ?, ?, ?, ?, ?);", peoples)
    conn.commit()
    close()


def show():
    open()
    cursor.execute("SELECT * FROM military;")
    for i in cursor.fetchall():
        print(i)
    close()


def get_question_after(name, surname, age):
    open()
    query = '''
    SELECT * FROM military WHERE Name == ?
    AND Surname == ? AND Birthday_year == ?'''
    cursor.execute(query, [name, surname, age])
    result = cursor.fetchone()
    close()
    return result


def main():
    clear_db()
    create()
    add_peoples()
    show()