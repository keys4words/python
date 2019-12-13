from tkinter import *

root = Tk()

colors = {
    "#ff0000": 'red',
    "#ff7d00": 'orange',
    "#ffff00": 'yellow',
    "#00ff00": 'green',
    "#007dff": 'blue',
    "#0000ff": 'dark blue',
    "#7d00ff": 'violet'
}

l = Label(root)
e = Entry(root, width=30, justify='center')
l.pack()
e.pack()

def get_color(text_color, hex_color):
    l['text'] = text_color
    e.delete(0, END)
    e.insert(0, hex_color)

for k, v in colors.items():
    Button(root, bg=k, command=lambda text=v, hex=k: get_color(text, hex)).pack(fill=X)

root.mainloop()