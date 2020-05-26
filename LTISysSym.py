"""
The GUI file and the main driver of the program.
It should allow the user to:
    1. Enter system paramaters like n, m, a's and b's.
    2. Select the input signal type (unit impulse, unit step).
    3. Plotting the input and output signals.
    4. Plotting the system states (X_1(t), X_2(t), X_3(t), ...., X_n(t)).
"""
from tkinter import *
import SSR
import Solver


root = Tk()
root.title("LTI System Simulator")
root.geometry("1000x700")
root.configure(bg='#1C1C1C')
img = PhotoImage(file = 'UI assets/title.png')
title = Label(root, image = img, bg='#1C1C1C').pack()

#title.grid(row = 0, ipadx = 10)   
def create_entry_widget(window):
    entry_widget = Entry(window, width=10, font=("Times New Roman", 20), fg = 'black', bd = 6)
    entry_widget.pack()
    return entry_widget

def create_label_widget(window, var_name):
    label_widget = Label(window, text = var_name, font = ("Times New Roman", 20), fg = 'black', bd = 6)
    label_widget.pack()
    return label_widget


n_input = Entry(root, width = 10, font = ("Times New Roman", 20), fg = 'black', bd = 6)
m_input = Entry(root, width = 10, font = ("Times New Roman", 20), fg = 'black', bd = 6)

n_input.pack(side = LEFT, pady = 15, padx = 25)
m_input.pack(side = LEFT, pady = 15, padx = 25)


<<<<<<< HEAD:LTI System Simulator.py
parameter_entry_widgets = []
a = [] 
=======
n = 0
m = 0
a = []
>>>>>>> 7124d5279fe79fe82c102d412a09e677acbc34ee:LTISysSym.py
b = [0]
 # The zero is a place holder that we clear later in the event of calling the parameters_window function.
 # Its purpose is to bypass the IndexError "list index out of range".       

def parameters_window():
    new_window = Toplevel(root)
    new_window.title("Enter Parameters")
    entries = []
    n = int(n_input.get())
    m = int(m_input.get())
    for i in range(n + 1):
        var_name = "a" + str(n-i)
        create_label_widget(new_window, var_name)
        #create_entry_widget(new_window)
        entries.append(create_entry_widget(new_window))
        a.append(entries[i].get())

    b.clear()
    for i in range(m + 1):
        var_name = "b" + str(m-i)
        create_label_widget(new_window, var_name)
        #create_entry_widget(new_window)
        entries.append(create_entry_widget(new_window))
        b.append(entries[i + n].get())

click = Button(root, text = "get parameters", bg = 'white', fg = 'black', font =("Georgia", 15, 'bold'), bd = 6, command = parameters_window)
click.pack()

# State-Space Matrices
A = SSR.setA(a)
B = SSR.setB(n)
C = SSR.setC(a, b)
D = SSR.setD(n, m, b)

print(a)
print(b)
print(A)
print(B)
print(C)
print(D)

#signature = Label(root, text = "Created by")

root.mainloop()
