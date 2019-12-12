from tkinter import *

root = Tk()

l = Label(root)
e = Entry(root, width=30, justify='center')
l.pack()
e.pack()

def get_color(text_color, hex_color):
    l['text'] = text_color
    e.delete(0, END)
    e.insert(0, hex_color)

btn_red = Button(root, bg="#ff0000", command=lambda: get_color('red', '#ff0000')).pack(fill=X)
btn_orange = Button(root, bg="#ff7d00", command=lambda: get_color('orange', '#ff7d00')).pack(fill=X)
btn_yellow = Button(root, bg="#ffff00", command=lambda: get_color('yellow', '#ffff00')).pack(fill=X)
btn_green = Button(root, bg="#00ff00", command=lambda: get_color('green', '#00ff00')).pack(fill=X)
btn_blue = Button(root, bg="#007dff", command=lambda: get_color('blue', '#007dff')).pack(fill=X)
btn_dark_blue = Button(root, bg="#0000ff", command=lambda: get_color('dark blue', '#0000ff')).pack(fill=X)
btn_violet = Button(root, bg="#7d00ff", command=lambda: get_color('violet', '#7d00ff')).pack(fill=X)


root.mainloop()