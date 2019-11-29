from tkinter import *
import time

def clicked():
    print('Clicked')

def check_time():
    btn_time['text'] = time.strftime('%H:%M:%S')

cnt = 0
def counter():
    global cnt
    cnt += 1
    # btn_cnt['text'] = cnt
    root.title(f'Counter: {cnt}')

root = Tk()
root.title('Первое приложение')
root.iconbitmap('py.ico')
root.geometry('600x400+700+300')
root.resizable(False, False)
root.config(bg='grey')

# btn = Button(root, text='кнопка', command=clicked, width=20, font='Arial 20 italic')
# btn = Button(root, text='кнопка', command=clicked, width=20, font=('Comic Sans MS', 20))
# btn = Button(root, text='кнопка1\n343', justify='left')
# btn = Button(root, text='кнопка1')
# btn.configure(width=30, height=5)
# btn['font'] = 'Arial 15'
# btn.pack()

btn_time = Button(root, text='Check time', command=check_time)
# btn_time.pack()

btn_cnt = Button(root, text='count', command=counter)
btn_cnt.pack()

# l = Label(root, text="Текст в строке 1\nстрока 2\nстрока 3",
#           bg='red',
#           fg='#fff',
#           font=("comic Sans MS", 18, 'bold'),
#           justify='left',
#           width=30,
#           height=10,
#           anchor='se')
# l.pack()

img =PhotoImage(file='pic2.png')
l_logo = Label(root, image=img)
l_logo.pack()


root.mainloop()