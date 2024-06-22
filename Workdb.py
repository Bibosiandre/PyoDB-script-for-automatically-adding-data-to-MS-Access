import pyodbc


db_path = r'C:\Users\VLAAA\PycharmProjects\Pyodb\Pyodb\UniDB.accdb' # Укажите путь к вашей базе данных MS Access/Specify the path to your MS Access database


conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + db_path) # Установите соединение с базой данных/Establish a connection to the database


cursor = conn.cursor()

# Создание таблиц/Creating tables

cursor.execute('''
    CREATE TABLE Преподаватели (
        [Табельный_номер] INTEGER PRIMARY KEY,
        [Фамилия] TEXT,
        [Имя] TEXT,
        [Отчество] TEXT,
        [Ученая_степень] TEXT,
        [Ученое_звание] TEXT
    )
''')

cursor.execute('''
    CREATE TABLE Место_работы (
        [Табельный_номер] INTEGER,
        [Кафедра] TEXT,
        [Должность] TEXT,
        [Ставок] FLOAT,
        FOREIGN KEY ([Табельный_номер]) REFERENCES Преподаватели([Табельный_номер])
    )
''')


cursor.execute('''
    CREATE TABLE Должности (
        [Должность] TEXT PRIMARY KEY,
        [Должностной_коэффициент_аудиторной_нагрузки] FLOAT
    )
''')


cursor.execute('''
    CREATE TABLE Ученые_степени (
        [Ученая_степень] TEXT PRIMARY KEY,
        [Надбавка_за_степень] INTEGER
    )
''')


cursor.execute('''
    CREATE TABLE Ученые_звания (
        [Ученое_звание] TEXT PRIMARY KEY,
        [Надбавка_за_звание] INTEGER
    )
''')


cursor.execute('''
    CREATE TABLE Премии (
        [Табельный_номер] INTEGER,
        [Премия] INTEGER,
        FOREIGN KEY ([Табельный_номер]) REFERENCES Преподаватели([Табельный_номер])
    )
''')

cursor.execute('''
    CREATE TABLE Совмещение (
        [Табельный_номер] INTEGER,
        [Надбавка_за_совмещение] INTEGER,
        FOREIGN KEY ([Табельный_номер]) REFERENCES Преподаватели([Табельный_номер])
    )
''')

conn.commit()

# Вставка необходимых данных/Inserting the required data

prepodavateli_data = [
    (1, 'Иванов', 'Иван', 'Иванович', 'кандидат наук', 'доцент'),
    (2, 'Петров', 'Петр', 'Петрович', 'доктор наук', 'профессор'),
    (3, 'Сидоров', 'Сидор', 'Сидорович', 'кандидат наук', 'доцент'),
    (4, 'Кузнецов', 'Кузьма', 'Кузьмич', 'доктор наук', 'профессор'),
    (5, 'Смирнов', 'Сергей', 'Сергеевич', 'кандидат наук', 'доцент'),
    (6, 'Васильев', 'Василий', 'Васильевич', 'доктор наук', 'профессор')
]

mesto_raboty_data = [
    (1, 'Кафедра математики', 'доцент', 1.0),
    (2, 'Кафедра физики', 'профессор', 0.5),
    (3, 'Кафедра информатики', 'доцент', 0.75),
    (4, 'Кафедра химии', 'профессор', 1.25),
    (5, 'Кафедра биологии', 'доцент', 1.5),
    (6, 'Кафедра истории', 'профессор', 0.25)
]

doljnosti_data = [
    ('ст. преподаватель', 0.9),
    ('доцент', 1.0),
    ('профессор', 1.1)
]

uchenye_stepeni_data = [
    ('кандидат наук', 3000),
    ('доктор наук', 6000)
]

uchenye_zvaniya_data = [
    ('доцент', 300),
    ('профессор', 600)
]

premii_data = [
    (1, 1000),
    (2, 1500),
    (3, 2000),
    (4, 2500),
    (5, 3000),
    (6, 3500)
]

sovmeshenie_data = [
    (1, 500),
    (2, 800),
    (3, 600),
    (4, 900),
    (5, 700),
    (6, 1000)
]

cursor.executemany('INSERT INTO Преподаватели VALUES (?, ?, ?, ?, ?, ?)', prepodavateli_data)
cursor.executemany('INSERT INTO Место_работы VALUES (?, ?, ?, ?)', mesto_raboty_data)
cursor.executemany('INSERT INTO Должности VALUES (?, ?)', doljnosti_data)
cursor.executemany('INSERT INTO Ученые_степени VALUES (?, ?)', uchenye_stepeni_data)
cursor.executemany('INSERT INTO Ученые_звания VALUES (?, ?)', uchenye_zvaniya_data)
cursor.executemany('INSERT INTO Премии VALUES (?, ?)', premii_data)
cursor.executemany('INSERT INTO Совмещение VALUES (?, ?)', sovmeshenie_data)

conn.commit()


conn.close()