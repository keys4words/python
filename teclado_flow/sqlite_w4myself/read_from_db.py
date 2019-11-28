import sqlite3

def dict_factory(cur, row):
    d = {}
    for idx, col in enumerate(cur.description):
        d[col[0]] = row[idx]
    return d

conn = sqlite3.connect('db_w4myself.sqlite')
conn.row_factory = dict_factory
cursor = conn.cursor()
email = 'pupkin@ya.ru'
# cursor.execute(f"SELECT * FROM users WHERE email = '{email}'")
# cursor.execute("SELECT * FROM users WHERE email = :email OR name = :name", {'email': email, 'name': 'John Dow'})
cursor.execute("SELECT * FROM users")
# res = cursor.fetchone()
# print(res[2])
# print(res)
# conn.commit()

res = cursor.fetchall()
# print(res)
for user in res:
    print(user['name'], user['email'])
conn.close()