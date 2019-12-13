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

class RainbowBtn:
    def __init__(self, window, btn_text, btn_color):
        self.btn_text = btn_text
        self.btn_color = btn_color
        self.btn = Button(window, bg=btn_color, command=self.set_btn_action)
        self.btn.pack(fill=X)

    def set_btn_action(self):
        l['text'] = self.btn_text
        e.delete(0, END)
        e.insert(0, self.btn_color)

l = Label(root)
e = Entry(root, width=30, justify='center')
l.pack()
e.pack()

for k, v in colors.items():
    RainbowBtn(root, v, k)

root.mainloop()