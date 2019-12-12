from tkinter import *

def add_str():
    e.insert(END, e.get())

def del_str():
    e.delete(0, END)


def get_str():
    l2['text'] = e.get()



root = Tk()
root.title('Первое приложение')
root.iconbitmap('py.ico')
root.geometry('600x400+700+300')
root.resizable(False, False)

l = Label(root, text='Поле ввода')
l.pack()

e = Entry(root)
# e.insert(0, 'Hello')
# e.insert(END, ' world')
e.pack()

btn_add = Button(root, text="Add", command=add_str).pack()
btn_del = Button(root, text="Delete", command=del_str).pack()
btn_add = Button(root, text="Get", command=get_str).pack()

l2 = Label(root, bg='blue', fg='white')
l2.pack(fill=X)


root.mainloop()