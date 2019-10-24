from auth import get_email_from_user, extract_username_from_email
from db import list_users, query_user_last_seen

registered_users = list_users()
i = 0
while i < len(registered_users):
    username = registered_users[i][0]
    last_seen = registered_users[i][1]
    print(i + 1, username, last_seen.date)


existing_username = list_users()[0][0]
last_seen = query_user_last_seen(existing_username)
print("User", existing_username, "last visited", last_seen)
print("User John Doe", "last visited", query_user_last_seen('John Doe'))

