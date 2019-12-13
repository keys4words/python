from tkinter import *

root = Tk()
root.geometry('600x400+1000+300')

# frame_top = Frame(root)
# frame_bottom = Frame(root)
# frame_top.pack()
# frame_bottom.pack()

# frame_top = LabelFrame(root, text='Top frame', padx=10, pady=10)
# frame_bottom = LabelFrame(root, text='Bottom frame', padx=10, pady=10)
# frame_top.pack(pady=10)
# frame_bottom.pack()
#
#
# l1 = Label(frame_top, text="1", font="15", fg="#fff", bg="#3498db", width=8, height=4).pack(side=LEFT)
# l2 = Label(frame_top, text="2", font="15", fg="#fff", bg="#2ecc71", width=8, height=4).pack(side=LEFT)
# l3 = Label(frame_bottom, text="3", font="15", fg="#fff", bg="#f1c40f", width=8, height=4).pack(side=LEFT)
# l4 = Label(frame_bottom, text="4", font="15", fg="#fff", bg="#34495e", width=8, height=4).pack(side=LEFT)

l1 = Label(root, text="1", font="15", fg="#fff", bg="#3498db", width=8, height=4).pack(expand=1, fill=Y)

root.mainloop()