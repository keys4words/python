def func():
    # global x
    x=50
    def inner_func():
        # nonlocal x
        global x
        x=100

    print('1----', x)
    # x = 'local'
    inner_func()
    print('2----', x)

# x = 'global'
x=20
func()
print('3----', x)


