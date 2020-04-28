n = int(input())
data = {'global': {'parent': None, 'variables': set()}}

def create():
    pass

def add():
    pass

def get():
    pass

for i  in range(n):
    cmd, namesp, arg = input().split()
    if cmd == "create":
        create()
    elif cmd == "add":
        add()
    elif cmd == "get":
        get()

print(data)