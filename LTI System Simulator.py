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
#import Solver

def create_entry_widget(window):
    entry_widget = Entry(window, width=10, font=("Times New Roman", 20), fg = 'black', bd = 6)
    entry_widget.pack()
    return entry_widget

def create_label_widget(window, var_name):
    label_widget = Label(window, text = var_name, font = ("Times New Roman", 20), fg = 'black', bd = 6)
    label_widget.pack()
    return label_widget

root = Tk()
root.title("LTI System Simulator")
root.geometry("1000x700")
root.configure(bg='#1C1C1C')
img = PhotoImage(file = 'UI assets/title.png')
title = Label(root, image = img, bg='#1C1C1C').pack()

n_input = Entry(root, width = 10, font = ("Times New Roman", 20), fg = 'black', bd = 6)
m_input = Entry(root, width = 10, font = ("Times New Roman", 20), fg = 'black', bd = 6)

n_input.pack(side = LEFT, pady = 15, padx = 25)
m_input.pack(side = LEFT, pady = 15, padx = 25)
 

# State-Space Matrices
def confirm_parameters():
    n = int(n_input.get())
    m = int(m_input.get())
    print(n, m)
    for i in range(n + 1):
        a.append(int(parameter_entry_widgets[i].get()))
    for i in range(m + 1):
        b.append(int(parameter_entry_widgets[i + n].get()))

    A = SSR.setA(a)
    B = SSR.setB(n)
    C = SSR.setC(a, b)
    D = SSR.setD(n, m, b)
    new_window.destroy()


parameter_entry_widgets = []
a = []
b = [0]
 # The zero is a place holder that we clear later in the event of calling the parameters_window function.
 # Its purpose is to bypass the IndexError "list index out of range".     

 
def parameters_window():
    new_window = Toplevel(root)
    new_window.title("Enter Parameters")
    n = int(n_input.get())
    m = int(m_input.get())
    for i in range(n + 1):
        var_name = "a" + str(n - i)
        create_label_widget(new_window, var_name)
        #create_entry_widget(new_window)
        parameter_entry_widgets.append(create_entry_widget(new_window))

    b.clear()
    for i in range(m + 1):
        var_name = "b" + str(m - i)
        create_label_widget(new_window, var_name)
        #create_entry_widget(new_window)
        parameter_entry_widgets.append(create_entry_widget(new_window))

    # State-Space Matrices
    def confirm_parameters():
        print(n, m)
        for i in range(n + 1):
            a.append(int(parameter_entry_widgets[i].get()))
        for i in range(m + 1):
            b.append(int(parameter_entry_widgets[i + n].get()))

        A = SSR.setA(a)
        B = SSR.setB(n)
        C = SSR.setC(a, b)
        D = SSR.setD(n, m, b)

        print(A)
        print(B)
        print(C)
        print(D)

        new_window.destroy()

    confirm_button = Button(new_window, text = "Confirm", bg = 'white', fg = 'black', font =("Georgia", 15, 'bold'), bd = 6, command = confirm_parameters)
    confirm_button.pack()

    new_window.mainloop()

parameters_button = Button(root, text = "get parameters", bg = 'white', fg = 'black', font =("Georgia", 15, 'bold'), bd = 6, command = parameters_window)
parameters_button.pack()


#signature = Label(root, text = "Created by")

root.mainloop()
