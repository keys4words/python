from auth import get_email_from_user, extract_username_from_email
from db import list_users, query_user_last_seen
from datetime import datetime, timedelta

email = get_email_from_user()
login = extract_username_from_email(email)
registered_users = list_users()

i = 0
users_dataset = {}
while i < len(registered_users):
    users_dataset [registered_users[i][0]] = registered_users[i][1]
    i = i+1

if login in users_dataset:
    last_seen = query_user_last_seen(login)
    if last_seen.date() + timedelta(days=180) < datetime.now().date():
        print('Вам надо подтвердить логин')
    else:
        print('Ваш аккаунт подтвержден до', last_seen.date() + timedelta(days=180))
else:
    print('Вы с нами совсем недавно! Добро пожаловать')


