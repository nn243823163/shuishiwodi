from Tkinter import *

master = Tk()

group = LabelFrame(master, text="Group", padx=5, pady=5)
group.pack(padx=100, pady=10)

w = Entry(group)
w.pack()

mainloop()
