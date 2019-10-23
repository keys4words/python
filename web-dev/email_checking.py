from auth import get_email_from_user, extract_username_from_email
from db import list_users

registered_users = list_users()
i = 0
while i < len(registered_users):
    username = registered_users[i][0]
    last_seen = registered_users[i][1]
    print(i + 1, username, last_seen.date)


email = get_email_from_user()
username = extract_username_from_email(email)
print("You loggin with name=" + username)
