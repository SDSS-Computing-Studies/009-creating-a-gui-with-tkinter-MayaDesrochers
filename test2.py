import tkinter as tk 
from tkinter import *

window = tk.Tk()

window.title("T-Town Veterinary Clinic Database")
dogphoto = PhotoImage(file="dog.png")



label1=tk.Label(window, text="Name", bg='white')
label2=tk.Label(window, text="Type", bg='white')
label3=tk.Label(window, text="Breed", bg='white')
label4=tk.Label(window, text="Owner", bg='white')
label5=tk.Label(window, text="Birthdate", bg='white')
label6=tk.Label(window, text="Client Database", bg='white')
label7=tk.Label(window, image=dogphoto, bg='white')


entry1=tk.Entry(window, text="Entry text can be typed in")
entry2=tk.Entry(window, text="Entry text can be typed in")
entry3=tk.Entry(window, text="Entry text can be typed in")
entry4=tk.Entry(window, text="Entry text can be typed in")
entry5=tk.Entry(window, text="Entry text can be typed in")
entry6=tk.Entry(window, text="Entry text can be typed in")

button1=tk.Button(window, text="Search by Name")
button2=tk.Button(window, text="<Previous")
button3=tk.Button(window, text=">Next")
button4=tk.Button(window, text="Save Entry",width=8, height=2 )



label1.grid(row = 7, column = 1)
label2.grid(row = 7, column = 2)
label3.grid(row = 7, column = 3)
label4.grid(row = 7, column = 4)
label5.grid(row = 7, column = 5)
label6.grid(row = 1, column = 3)
label7.grid(row = 1, column = 1)
#grid

entry1.grid(row=8, column = 1)
entry2.grid(row=8, column = 2)
entry3.grid(row=8, column = 3)
entry4.grid(row=8, column = 4)
entry5.grid(row=8, column = 5)
entry6.grid(row=0, column = 5)

button1.grid(row=0, column=4)
button2.grid(row=9, column = 1, sticky="W")
button3.grid(row=9, column = 5, sticky="E")
button4.grid(row=9, column = 3)

window.configure(bg='white')


#,columnspan="""")
#, rowspan = 2)
window.mainloop()








 

