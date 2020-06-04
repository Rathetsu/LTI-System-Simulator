import numpy as np
import matplotlib.pyplot as plt
import SSR
import plot


n = 2
m = 1
a = [1, 4, 25]
b = [50]

A = SSR.setA(a)
B = SSR.setB(n)
C = SSR.setC(a, b)
D = SSR.setD(n, m, a, b)


#A = np.array([[-7]])
#B = np.array([[1]])
#C = np.array([-20])
#D = np.array([4])
#A = np.array([[0, 1], [-2, -3]])
#B = np.array([[0], [5]])
#A = np.array([[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [-0.125, -0.125, -0.375, -0.125]])
#B = np.array([[0], [0], [0], [1]])
#C = np.array([0.125, 1.25, 0.5, 0.875] )
#


def step_h(tk=10, k=1000):
    h = tk / k
    return h


def func_B(x, u_type, A, B):
    """

    :return:
    """
    B_i = A.dot(x) + B.dot(u_type) #replace (1) with the input
    return B_i


def SS_SSEB(n, u_type, k=1000, tk=10):
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

    for j in range(0, k+1, 2):


        #Getting B1
        x_temp = x_t
        B1 = func_B(x_temp, u, A, B)

        #Getting B2
        x_temp = x_t + step_h(tk, k) * B1
        B2 = func_B(x_temp, u, A, B)

        #Getting B3
        x_temp = x_t + (step_h(tk, k)/2) * B1 + (step_h(tk, k)/2) * B2
        B3 = func_B(x_temp, u, A, B)

        #Getting B4
        x_temp = x_t + 2 * step_h(tk, k) * B3
        B4 = func_B(x_temp, u, A, B)

        #Getting B5
        x_temp = x_t + (step_h(tk, k) / 12) * (5 * B1 + 8 * B3 - B4)
        B5 = func_B(x_temp, u, A, B)

        #Getting B6
        x_temp = x_t + (step_h(tk, k) / 3) * (B1 + B4 + 4 * B5)
        B6 = func_B(x_temp, 1, A, B)


        #Getting x(j+1) and x(j+2)
        x_j1 = x_t + (step_h(tk, k) / 12) * (5 * B1 + 8 * B3 - B4)
        x_j2 = x_t + (step_h(tk, k) / 3) * (B1 + 4 * B5 + B6)

        #Appending the 2 previous values to the array that contains all the values of the state vars
        x_s = np.append(x_s, x_j1, axis=1)
        x_s = np.append(x_s, x_j2, axis=1)

        #x_j2 ==> x_t
        x_t = x_j2

        if u_type == 1:
            u = 1
        else:
            u = 0

    for j in range(k+3):
        #A list that contains all the time samples
        t = np.append(t, j * step_h(tk, k))
    print(x_s.shape)
    y_t = C.dot(x_s) + D.dot(plot.generate_input(u_type))


    print(x_t)
    print(x_temp)
    print(B1)
    print(B2)
    print(B3)
    print(B4)
    print(B5)
    print(B6)
    print(x_j1)
    print(x_j2)
    print(x_s.shape)

    print(y_t)

    plt.plot(t, y_t)
    plt.grid(True)
    plt.show()

SS_SSEB(n, 2,1000, 10)