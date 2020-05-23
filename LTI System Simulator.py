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

#title.grid(row = 0, ipadx = 10)   
def create_entry_widget(window):
    entry_widget = Entry(window, width=10, font=("Times New Roman", 20), fg = 'black', bd = 6)
    entry_widget.pack()
    return entry_widget

def create_label_widget(window, var_name):
    label_widget = Label(window, text = var_name, font = ("Times New Roman", 20), fg = 'black', bd = 6)
    label_widget.pack()
    return label_widget

def parameters_window():
    n = int(n_input.get())
    m = int(m_input.get())
    new_window = Toplevel(root)
    new_window.title("Enter Parameters")
    #new_window.geometry("500x500")
    entries = []
    labels = []
    for i in range(n):
        var_name = "a" + str(i)
        create_label_widget(new_window, var_name)
        create_entry_widget(new_window)

    for i in range(m):
        var_name = "b" + str(i)
        labels.append(create_label_widget(new_window, var_name))
        entries.append(create_entry_widget(new_window))



#signature = Label(root, text = "Created by")


n_input = Entry(root, width = 10, font = ("Times New Roman", 20), fg = 'black', bd = 6)
m_input = Entry(root, width = 10, font = ("Times New Roman", 20), fg = 'black', bd = 6)

n_input.pack(side = LEFT, pady = 15, padx = 25)
m_input.pack(side = LEFT, pady = 15, padx = 25)


click = Button(root, text = "get parameters", bg = 'white', fg = 'black', font =("Georgia", 15, 'bold'), bd = 6, command = parameters_window).pack()

root.mainloop()
