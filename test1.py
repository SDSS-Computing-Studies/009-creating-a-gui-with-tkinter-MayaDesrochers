import tkinter as tk 
from tkinter import *

window = tk.Tk()

window.title("tk")
entry1 = tk.Entry(window,text="Entry widgets can be typed in")
label1 = tk.Label(window, text="x")
entry2 = tk.Entry(window, text="Entry widgets can be typed in")
button1 = tk.Button(window, text="=")
entry3 = tk.Entry(window, text="Entry widgets can be typed in")


entry1.pack(side=LEFT)
label1.pack(side=LEFT)
entry2.pack(side=LEFT)
button1.pack(side=LEFT)
entry3.pack(side=LEFT)

window.mainloop()