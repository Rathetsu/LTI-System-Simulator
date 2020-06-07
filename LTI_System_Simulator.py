"""
The GUI file and the main driver of the program.
It should allow the user to:
    1. Enter system paramaters like n, m, a's and b's.
    2. Select the input signal type (unit impulse, unit step).
    3. Plotting the input and output signals.
    4. Plotting the system states (X_1(t), X_2(t), X_3(t), ...., X_n(t)).
"""
from tkinter import *
from random import *
import matplotlib.pyplot as plt
import SSR
import Solver2

HEIGHT = 680
WIDTH = 880

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
root.resizable(False, False)
img_title = PhotoImage(file = 'UI assets/title.png')
img_bg = PhotoImage(file = 'UI assets/bg.png')
#root.geometry("700x500")
#root.configure(bg='#1C1C1C')

canvas = Canvas(root, height = HEIGHT, width = WIDTH )
canvas.pack()

frame1 = Frame(root, bg = '#1C1C1C')
frame2 = Frame(root, bg = '#1C1C1C')
frame1.place(relwidth = 1, relheight = 1)
#frame2.pack(side = BOTTOM)
bg_label = Label(frame1, image = img_bg)
bg_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

parameter_entry_widgets = []
a = []
b = [0]
# The zero is a place holder that we clear later in the event of calling the parameters_window function.
# Its purpose is to bypass the IndexError "list index out of range".

def parameters_window():
    new_window = Toplevel(root)
    new_window.title("Enter System Parameters")
    new_window.configure(bg='#1C1C1C')
    new_window.resizable(False, False)
    global n
    n = int(n_input.get())
    m = int(m_input.get())
    # r & c are placement variables 
    r = 0
    c = 0
    new_window.grid_rowconfigure(r, minsize = 30)
    r += 1
    for i in range(n + 1):
        var_name = "a" + str(n - i)
        create_label_widget(new_window, var_name, r, c)
        c += 1
        parameter_entry_widgets.append(create_entry_widget(new_window, r, c))
        c += 1

    b.clear()
    r += 1
    new_window.grid_rowconfigure(r, minsize = 30)
    r += 1
    c2 = 0      # c2 is a new placement variable so we can use c for placing the confirm button
    for i in range(m + 1):
        var_name = "b" + str(m - i)
        create_label_widget(new_window, var_name, r, c2)
        c2 += 1
        #create_entry_widget(new_window)
        parameter_entry_widgets.append(create_entry_widget(new_window, r, c2))
        c2 += 1

    # State-Space Matrices
    def confirm_parameters():
        global A
        global B
        global C
        global D

        for i in range(n + 1):
            a.append(float(parameter_entry_widgets[i].get()))
        for i in range(m + 1):
            b.append(float(parameter_entry_widgets[i + n + 1].get()))
            
        SSR.standard_form(a, b)
        A = SSR.setA(a)
        B = SSR.setB(n)
        C = SSR.setC(a, b)
        D = SSR.setD(n, m, a, b)
        print(A)
        print(B)
        print(C)
        print(D)

        new_window.destroy()
    
    def randomize_parameters():
        for i in range(n + 1):
            parameter_entry_widgets[i].delete(0, END)
            parameter_entry_widgets[i].insert(0, str(round(uniform(0, 20), 0)))

        for i in range(m + 1):
            parameter_entry_widgets[i + n + 1].delete(0, END)
            parameter_entry_widgets[i + n + 1].insert(0, str(round(uniform(0, 20), 0)))

    rand_button = Button(new_window, text = "Randomize", bg = 'white', fg = 'black', font =("Georgia", 15, 'bold'), bd = 5, command = randomize_parameters)
    confirm_button = Button(new_window, text = "Confirm", bg = 'white', fg = 'black', font =("Georgia", 15, 'bold'), bd = 5, command = confirm_parameters)
    r += 1
    c += 1
    new_window.grid_rowconfigure(r, minsize = 10)
    new_window.grid_columnconfigure(c, minsize = 30)
    r += 1
    c += 1
    rand_button.grid(row = r, column = c)
    r += 1
    confirm_button.grid(row = r, column = c)
    new_window.mainloop()

def set_u(selection):
    global u_type
    u_type = selection

#def p_input():
    #if u_type == "Unit Step":
        
    #else:
        
def p_response():
    plt.close('all')
    if u_type == "Unit Step":
        p_response_if_step()
    else:
        p_response_if_impulse()

def p_response_if_step():
    max_t = int(maximum_time_entry.get())
    Foo = Solver2.SS_SSEB(n, 1, A, B, C, D, max_t)
    bar = Foo[0]
    t = Foo[3]
    plt.figure(num = "System Response")
    plt.plot(t, bar)
    plt.grid(True)
    plt.show()

def p_response_if_impulse():
    max_t = int(maximum_time_entry.get())
    Foo = Solver2.SS_SSEB(n, 2, A, B, C, D, max_t)
    bar = Foo[0]
    t = Foo[3]
    plt.figure(num = "System Response")
    plt.plot(t, bar)
    plt.grid(True)
    plt.show()

def p_states():
    plt.close('all')
    if u_type == "Unit Step":
        p_states_if_step()
    else:
        p_states_if_impulse()

def p_states_if_step():
    max_t = int(maximum_time_entry.get())
    Foo = Solver2.SS_SSEB(n, 1, A, B, C, D, max_t)
    bar = Foo[1]
    t = Foo[3]

    plt.figure(num = "System States")
    for i in range(n):
        state_name = "X"
        state_name += str(i + 1)
        plt.plot(t, bar[i], label = state_name)
    plt.grid()
    plt.legend()
    plt.show()

def p_states_if_impulse():
    max_t = int(maximum_time_entry.get())
    Foo = Solver2.SS_SSEB(n, 2, A, B, C, D, max_t)
    bar = Foo[2]
    t = Foo[3]

    plt.figure(num = "System States")
    for i in range(n):
        state_name = "X"
        state_name += str(i + 1)
        plt.plot(t, bar[i], label = state_name)
    plt.grid()
    plt.legend()
    plt.show()


# main frame definitions and functionality
n_label = Label(frame1, text = "n = ", font = ("Georgia", 22), fg = 'white', bg='#1C1C1C')
m_label = Label(frame1, text = "m = ", font = ("Georgia", 22), fg = 'white', bg='#1C1C1C')
n_input = Entry(frame1, width = 5, font = ("Times New Roman", 20), fg = 'black', bd = 5)
m_input = Entry(frame1, width = 5, font = ("Times New Roman", 20), fg = 'black', bd = 5)
parameters_button = Button(frame1, text = "Input & Output Parameters", bg = 'white', fg = 'black', font =("Georgia", 15, 'bold'), bd = 6, command = parameters_window)
signal_type_label = Label(frame1, text = "Input Signal Type: ", font = ("Georgia", 22), fg = 'white', bg='#1C1C1C')
selection = StringVar()
#selection.set("Unit Step")
signal_type_menu = OptionMenu(frame1, selection, "Unit Step", "Unit Impulse", command = set_u)
maximum_time_label = Label(frame1, text = "Maximum Time: ", font = ("Georgia", 22), fg = 'white', bg='#1C1C1C')
maximum_time_entry = Entry(frame1, width = 5, font = ("Times New Roman", 20), fg = 'black', bd = 5)
maximum_time_entry.insert(0, "10")
plot_output = Button(frame1, text = "Plot System Response", bg = 'white', fg = 'black', font =("Georgia", 15, 'bold'), bd = 6, command = p_response)
plot_states = Button(frame1, text = "Plot States", bg = 'white', fg = 'black', font =("Georgia", 15, 'bold'), bd = 6, command = p_states)

# Widget placement
frame1.grid_rowconfigure(0, minsize = 240)
frame1.grid_columnconfigure(0, minsize = 30)
n_label.grid(row = 1, column = 1)
n_input.grid(row = 1, column = 2)
frame1.grid_columnconfigure(3, minsize = 80)
m_label.grid(row = 1, column = 4)
m_input.grid(row = 1, column = 5)
frame1.grid_rowconfigure(2, minsize = 30)
frame1.grid_columnconfigure(6, minsize = 50)
parameters_button.grid(row = 3, column = 7)
frame1.grid_rowconfigure(4, minsize = 50)
#frame2.grid_rowconfigure(0, minsize = 200)
#signal_type_label.grid(row = 5, column = 1)
#signal_type_menu.grid(row = 5, column = 2)
signal_type_label.place(x = 30, y = 410)
signal_type_menu.place(x = 310, y = 417)
maximum_time_label.place(x = 30, y = 480)
maximum_time_entry.place(x = 310,y = 480)
plot_output.place(x = 480, y = 520)
plot_states.place(x = 530, y = 580)

root.mainloop()
