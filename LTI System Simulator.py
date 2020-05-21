"""
The GUI file.
It should allow the user to:
    1. Enter system paramaters like n, m, a's and b's.
    2. Select the input signal type (unit impulse, unit step).
    3. Plotting the input and output signals.
    4. Plotting the system states (X_1(t), X_2(t), X_3(t), ...., X_n(t)).
"""
from tkinter import *

root = Tk()
root.title("LTI System Simulator")
root.geometry("1000x700")
root.configure(bg='#1C1C1C')

img = PhotoImage(file = 'UI assets/title.png')
title = Label(root, image = img, bg='#1C1C1C').pack()
#title.grid(row = 0, column = 10)   

#signature = Label(root, text = "Created by")

click = Button(root, text = "Simulate", bg = 'white', fg = 'black', font =("Georgia", 15, 'bold'), bd = 6).pack()

a_input = Entry(root, width = 10, font = ("Times New Roman", 20), fg = 'black', bd = 6).pack(side = LEFT, pady = 15, padx = 25)
b_input = Entry(root, width = 10, font = ("Times New Roman", 20), fg = 'black', bd = 6).pack(side = LEFT, pady = 15, padx = 25)
n_input = Entry(root, width = 10, font = ("Times New Roman", 20), fg = 'black', bd = 6).pack(side = LEFT, pady = 15, padx = 25)
m_input = Entry(root, width = 10, font = ("Times New Roman", 20), fg = 'black', bd = 6).pack(side = LEFT, pady = 15, padx = 25)



root.mainloop()
