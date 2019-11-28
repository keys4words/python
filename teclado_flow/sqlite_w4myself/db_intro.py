import sqlite3

conn = sqlite3.connect('db_w4myself.sqlite')

cursor = conn.cursor()
cursor.execute('''CREATE TABLE users 
    (id INTEGER PRIMARY KEY, 
    name TEXT NOT NULL, 
    email TEXT NOT NULL UNIQUE)''')

conn.close()