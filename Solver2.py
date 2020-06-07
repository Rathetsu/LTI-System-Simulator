import numpy as np
import matplotlib.pyplot as plt
import SSR


def generate_input(u_type, k =1000):
    """
    returns a list u containing the y axis values of the function. 
    """
    u = []
    if u_type == 1:
        return 1
    elif u_type == 2:
        u = np.zeros(k + 3).reshape(1, k + 3)
        u[0][0] = 1
        return u

def step_h(tk=10, k=1000):
    h = tk / k
    return h


def func_B(x, u,A, B):
    """

    :return:
    """
    B_i = A.dot(x) + B.dot(u) #replace (1) with the input
    return B_i


def SS_SSEB(n, u_type,  A, B, C, D, tk, k=1000):
    """

    :param n:
    :param k:
    :return:
    """
    B1 = []
    B2 = []
    B3 = []
    B4 = []
    B5 = []
    B6 = []
    x_t = np.zeros(n).reshape(n, 1)
    x_temp = []
    x_s = np.zeros(n).reshape(n, 1)
    x_j1 = []
    x_j2 = []
    t = []
    u = 1
    y_t = []
    xh_s = np.zeros(n * (k+3)).reshape(n, k+3)

    for j in range(0, k+1, 2):


        #Getting B1
        x_temp = x_t
        B1 = func_B(x_temp, u,A, B)

        #Getting B2
        x_temp = x_t + step_h(tk, k) * B1
        B2 = func_B(x_temp, u, A, B)

        #Getting B3
        x_temp = x_t + (step_h(tk, k)/2) * B1 + (step_h(tk, k)/2) * B2
        B3 = func_B(x_temp, u,A, B)

        #Getting B4
        x_temp = x_t + 2 * step_h(tk, k) * B3
        B4 = func_B(x_temp, u, A, B)

        #Getting B5
        x_temp = x_t + (step_h(tk, k) / 12) * (5 * B1 + 8 * B3 - B4)
        B5 = func_B(x_temp, u, A, B)

        #Getting B6
        x_temp = x_t + (step_h(tk, k) / 3) * (B1 + B4 + 4 * B5)
        B6 = func_B(x_temp, u, A, B)


        #Getting x(j+1) and x(j+2)
        x_j1 = x_t + (step_h(tk, k) / 12) * (5 * B1 + 8 * B3 - B4)
        x_j2 = x_t + (step_h(tk, k) / 3) * (B1 + 4 * B5 + B6)

        #Appending the 2 previous values to the array that contains all the values of the state vars
        x_s = np.append(x_s, x_j1, axis=1)
        x_s = np.append(x_s, x_j2, axis=1)

        #x_j2 ==> x_t
        x_t = x_j2

        """
        if u_type == 1:
            u = 1
        else:
            u = 0
        """
    for j in range(k+3):
        #A list that contains all the time samples
        t = np.append(t, j * step_h(tk, k))

    for i in range(n):
        for j in range(k+2):
            xh_s[i][j] = (x_s[i][j+1] - x_s[i][j]) / step_h(tk, k)

    if u_type == 1:
        y_t = C.dot(x_s) + D.dot(1)
    elif u_type == 2:
        y_t = C.dot(xh_s) + D.dot(generate_input(u_type))

    Foo = [y_t, x_s, xh_s, t]
    return Foo
