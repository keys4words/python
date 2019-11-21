import time

def get_email_from_user(attempts=3, sleep_duration=10):
    email = input('Enter your email: ')
    i = 1

    while email.find("@") == -1:
        print("Wrong email. Try again")
        i = i + 1
        email = input('Try #' + str(i) + ' Enter your email: ')
        if i%attempts == 0:
            print('So many tries. Wait ' + str(sleep_duration) + ' sec')
            time.sleep(sleep_duration)
    return email

def extract_username_from_email(email):
    return email.split("@")[0].lower()