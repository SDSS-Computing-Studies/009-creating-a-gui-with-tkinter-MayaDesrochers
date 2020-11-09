import tkinter as tk 
from tkinter import *

window = tk.Tk()

window.title("Example")
window.geometry("300x150")
dogphoto = PhotoImage(file="dog.png")




label1=Label(window, text="Pochacco!", bg='white')
label2=Label(window, text="A cuddly little puppy! This is from the same\n creators who brought you Keropi and Kero Kero", bg='pale turquoise')

label3=tk.Label(window, image=dogphoto, bg='white')

label3.place(x=75, y=10)
label1.place(x=150, y=50)
label2.place(x=0, y=115)

window.configure(bg='white')

mainloop()