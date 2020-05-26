import numpy as np
import SSR
import LTISysSym as lti

n = 3
m = 3
A = np.array([[0, 1, 0], [0, 0, 1], [-6, -11, -6]])
B = np.array([[2], [-6], [16]])
C = np.array([1, 0, 0])
D = np.array([1])
#Step 1:
def get_h(k=1000, t_k=10.0, t_0=0.0):
    """
    :param t_k: Final time (set to 10 by default)
    :param t_0: Initial time (set to 0 by default)
    :param k: Total number of time steps excluding the last step. Total no. of time steps is (k+1)
    :return: The factor h
    """
    h = (t_k - t_0)/k
    return h


#Step 2:

#Step 3:
def f_B(B_i, A, B, x_temp, n):
    #add a prameter to modify input u later
    for i in range(0, n):  # Setting array B_1
        B_i.append(A.dot(x_temp) + B)






def block(n, u, k=1000):
    """
    :return:
    """
    B_1 = []
    B_2 = []
    B_3 = []
    B_4 = []
    B_5 = []
    B_6 = []
    x_t = []
    x_temp = []

    #Add the input later
    for j in range(0,k):
        if j == 0:
            x_t = [0 * element for element in range(0, n)]
            x_t = np.array(x_t)
            x_temp = x_t
        f_B(B_1, A, B, x_temp, n) # Setting array B_1

        for i in range (0,n):
            x_temp[i]=x_t[i] + get_h()*B_1[i]
        f_B(B_2, A, B, n) # Setting array B_2

        for i in range(0, n): # Setting array B_3
            x_temp[i] = x_t+ (get_h()/2) * B_1[i] + (get_h()/2) * B_2[i]
        f_B(B_3, A, B, x_temp, n) # Setting array B_3

        for i in range(0, n): # Setting array B_4
            x_temp[i] = x_t[i] + 2*get_h()*B_3[i]
        f_B(B_4, A, B, x_temp, n) # Setting array B_

        for i in range(0, n): # Setting array B_5
            x_temp[i] = x_t[i] + (get_h()/12)*(5*B_1[i]+8*B_3[i]-B_4[i])
        f_B(B_5, A, B, x_temp, n)  # Setting array B_5

        for i in range(0, n):
            x_temp[i] = x_t[i] +(get_h()/3)*(B_1 + B_4 + B_5)
        f_B(B_6, A, B, x_temp, n)  # Setting array B_6