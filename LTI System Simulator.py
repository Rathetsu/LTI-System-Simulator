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

HEIGHT = 500
WIDTH = 700

def create_label_widget(window, var_name, r, c):
    label_widget = Label(window, text = var_name, font = ("Times New Roman", 20), fg = 'white', bg='#1C1C1C', bd = 6)
    label_widget.grid(row = r, column = c)
    return label_widget
    
def create_entry_widget(window, r, c):
    entry_widget = Entry(window, width = 5, font = ("Times New Roman", 20), fg = 'black', bd = 5)
    entry_widget.grid(row = r, column = c)
    return entry_widget


root = Tk()
root.title("LTI System Simulator")
#img = PhotoImage(file = 'UI assets/title.png')
#root.geometry("700x500")
#root.configure(bg='#1C1C1C')

canvas = Canvas(root, height = HEIGHT, width = WIDTH )
canvas.pack()

#title = Label(root, image = img, bg='#1C1C1C')
#title.pack(side = TOP)

frame1 = Frame(root, bg = '#1C1C1C')
frame1.place(relwidth = 1, relheight = 1)

#root.grid_columnconfigure(0, minsize = 20)
#title.grid(row = 0, column = 1 )
#root.grid_rowconfigure(1, minsize = 50)

n_label = Label(frame1, text = "n = ", font = ("Georgia", 22), fg = 'white', bg='#1C1C1C')
m_label = Label(frame1, text = "m = ", font = ("Georgia", 22), fg = 'white', bg='#1C1C1C')
n_input = Entry(frame1, width = 5, font = ("Times New Roman", 20), fg = 'black', bd = 6)
m_input = Entry(frame1, width = 5, font = ("Times New Roman", 20), fg = 'black', bd = 6)

frame1.grid_rowconfigure(0, minsize = 200)
frame1.grid_columnconfigure(0, minsize = 30)
n_label.grid(row = 1, column = 1)
n_input.grid(row = 1, column = 2)
frame1.grid_columnconfigure(3, minsize = 80)
m_label.grid(row = 1, column = 4)
m_input.grid(row = 1, column = 5)
frame1.grid_rowconfigure(2, minsize = 30)


parameter_entry_widgets = []
a = []
b = [0]
 # The zero is a place holder that we clear later in the event of calling the parameters_window function.
 # Its purpose is to bypass the IndexError "list index out of range".     

def parameters_window():
    new_window = Toplevel(root)
    new_window.title("Enter System Parameters")
    new_window.configure(bg='#1C1C1C')
    """   
    frame1 = Frame(new_window)
    frame2 = Frame(new_window)
    frame1.pack(side = BOTTOM, fill = x)
    frame2.pack(side = BOTTOM, fill = x)
    """
    n = int(n_input.get())
    m = int(m_input.get())

    # r & c are placement variables 
    r = 0
    c = 0
    r += 1
    for i in range(n + 1):
        var_name = "a" + str(n - i)
        create_label_widget(new_window, var_name, r, c)
        #create_entry_widget(new_window)
        c += 1
        parameter_entry_widgets.append(create_entry_widget(new_window, r, c))
        c += 1

    b.clear()
    r += 1
    new_window.grid_rowconfigure(r, minsize = 30)
    r += 1
    c = 0
    for i in range(m + 1):
        var_name = "b" + str(m - i)
        create_label_widget(new_window, var_name, r, c)
        c += 1
        #create_entry_widget(new_window)
        parameter_entry_widgets.append(create_entry_widget(new_window, r, c))
        c += 1

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

    confirm_button = Button(new_window, text = "Confirm", bg = 'white', fg = 'black', font =("Georgia", 15, 'bold'), bd = 5, command = confirm_parameters)
    r += 1
    c += 1
    new_window.grid_rowconfigure(r, minsize = 30)
    new_window.grid_columnconfigure(c, minsize = 30)
    r += 1
    c += 1
    confirm_button.grid(row = r, column = c)

    new_window.mainloop()

parameters_button = Button(frame1, text = "Input & Output Parameters", bg = 'white', fg = 'black', font =("Georgia", 15, 'bold'), bd = 6, command = parameters_window)
parameters_button.grid(row = 3, column = 5)

#signature = Label(root, text = "Created by")

root.mainloop()
