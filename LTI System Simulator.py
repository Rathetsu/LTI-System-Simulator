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
root.geometry("1000x700")
root.configure(bg='#2a2a2a')

img = PhotoImage(file = 'UI/title.png')
title = Label(root, image = img, bg='#2a2a2a').grid(row = 0, column = 10)   

#signature = Label(root, text = "Created by")




root.mainloop()
