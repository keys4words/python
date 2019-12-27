from tkinter import *

root = Tk()
# root.geometry('600x400+1000+300')

# f = Frame(root)
# f.pack(pady=10)
#
# btn_list = [
#     '7',
#     '8',
#     '9',
#     '4',
#     '5',
#     '6',
#     '1',
#     '2',
#     '3',
#     '0'
# ]
#
# row = 0
# column = 0
#
# for i in btn_list:
#     if i == '0':
#         Button(f, text=i, padx=10, pady=5).grid(row=row, columnspan=3)
#     else:
#         Button(f, text=i, padx=10, pady=5).grid(row=row, column=column)
#         column += 1
#         if column == 3:
#             column = 0
#             row += 1


l_user = Label(root, text='Login:').grid(row=0, column=0, padx=10, pady=10, sticky=W)
e_user = Entry(root).grid(row=0, column=1, columnspan=2, padx=10, sticky=W+E)

l_pass = Label(root, text='Password:').grid(row=1, column=0, padx=10, sticky=W)
e_pass = Entry(root, show='*').grid(row=1, column=1, columnspan=2, padx=10, sticky=W+E)

btn_login = Button(root, text='Вход').grid(row=2, column=0, pady=10, padx=10, sticky=W+E)
btn_reg = Button(root, text='Регистрация').grid(row=2, column=1, pady=10, sticky=W+E)
btn_forgot = Button(root, text='Забыли пароль?').grid(row=2, column=2, pady=10, padx=20)

root.mainloop()