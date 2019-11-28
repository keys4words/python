import sqlite3

conn = sqlite3.connect('db_w4myself.sqlite')

cursor = conn.cursor()
# cursor.execute('''
# INSERT INTO users
#     (name, email)
#     VALUES('Иванов Иван Иваныч', 'ivanov@gmail.com'
#         )
# ''')

# cursor.execute('''
# INSERT INTO users
#     (name, email)
#     VALUES('Петров Петр Иваныч', 'petrov@gmail.com'
#         )
# ''')

# cursor.executescript('''
# INSERT INTO users (name, email) VALUES('Иванов Иван Иваныч', 'sidor@gmail.com');
# INSERT INTO users (name, email) VALUES('Пупкин Вася', 'pupkin@ya.ru');
# INSERT INTO users (name, email) VALUES('John Dow', 'j.dow@yahoo.com');
# ''')

users = [
    ('user1', 'user1@ya.com'),
    ('user2', 'use2131@ya.com'),
    ('user3', 'user2341234211@ya.com'),
]

cursor.executemany("INSERT INTO users (name, email) VALUES (?, ?)", users)

conn.commit()

conn.close()