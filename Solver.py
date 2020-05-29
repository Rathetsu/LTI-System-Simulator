import numpy as np
import SSR


n = 4
m = 3
A = np.array([[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1],[-0.125, -0.125, -0.375, -0.125]])
B = np.array([[0], [0], [0], [1]])
C = np.array([0.125, 1.25, 0.5, 0.875])
D = np.array([0])
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

def func_B(B_i, x_temp, A, B, n):
    for i in range(n):
        B_i.append(A.dot(x_temp) + B) #Modify for the input u later



def SS_SSEB(n, k =1000):
    """

    :return:
    """
    x_t = []
    x_temp = []
    B1 = []
    B2 = []
    B3 = []
    B4 = []
    B5 = []
    B6 = []
    x_j1 = []
    x_j2 = []
    x_s = []
    y_t = []
    for i in range(n):
        x_s.append([])
    for j in range(k):
        if j == 0:
            for i in range(n):
                x_t.append([])
                x_t[i].append(0.0)
        #x_t = np.array(x_t)
        x_temp = np.array(x_t) #Temp x_t to change whenever needed to get the values of B(1 to 6)
        x_s = np.array(x_s) #All the values of the state variables over the specified time
        x_s = np.append(x_s, x_t, axis=1)



        #Getting B1
        func_B(B1, x_temp, A, B, n)

        #Getting B2
        for i in range(n):
            x_temp = x_t + get_h() * B1[i]
        func_B(B2, x_temp, A, B, n)

        #Getting B3
        for i in range(n):
            x_temp = x_t + (get_h()/2)*(B1[i]+B2[i])
        func_B(B3, x_temp, A, B, n)

        #Getting B4
        for i in range(n):
            x_temp = x_t + 2 * get_h() * B3[i]
        func_B(B4, x_temp, A, B, n)

        #Getting B5
        for i in range(n):
            x_temp = x_t + (get_h()/12) * (5 * B1[i] + 8 * B3[i] - B4[i])
        func_B(B5, x_temp, A, B, n)

        #Getting B6
        for i in range(n):
            x_temp = x_t + (get_h()/3) * (B1[i] + B4[i] + 4 * B5[i])
        func_B(B6, x_temp, A, B, n)

        #Setting the values fot the state variables
        for i in range(n):
            x_j1 = np.append(x_j1, (x_t[i] + (get_h()/12) * (5 * B1[0][i] + 8 * B3[0][i] - B4[0][i])))
            #x_j2 = np.append(x_j2, (x_t[i] + (get_h()/3) * (B1[0][i] + 4 * B5[0][i] + B6[0][i])))

        # x_j1 ==> x_t
        x_t = []
        for i in range(n):
            x_t.append([])
            x_t[i].append(x_j1[i])
        x_j1 = []

    #Add the term ( D.dot(u) ) after adding the input
    y_t = C.dot(x_s)

    #print(x_j1)
    print(y_t)
    print(x_s)
    #print(x_t)
    #print(x_temp)
    print(B1[10])

SS_SSEB(n, 1000)


#Step 2:

#Step 3:
"""
def f_B(B_i, A, B, x_temp, n):
    #add a prameter to modify input u later
    for i in range(0, n):  # Setting array B_1
        B_i.append(A.dot(x_temp) + B)
    B_i=np.array(B_i)
    """





"""
def block(n, u, k=1000):
    
    B_1 = []
    B_2 = []
    B_3 = []
    B_4 = []
    B_5 = []
    B_6 = []
    x_t = []
    x_temp = []

    #Add the input later
    for j in range(0, k):
        if j == 0:
            for i in range(0, n):
                x_t.append([])
                x_t[i].append(0.0)
            x_t = np.array(x_t)
        x_temp = x_t
        f_B(B_1, A, B, x_temp, n) # Setting array B_1
        for i in range(0, n):
            x_temp[i][0] = x_t[i][0] + get_h()*B_1[i][0]
        f_B(B_2, A, B, x_temp, n) # Setting array B_2

        for i in range(0, n): # Setting array B_3
            x_temp[i][0] = x_t[i][0] + (get_h()/2) * B_1[i][0] + (get_h()/2) * B_2[i][0]
        f_B(B_3, A, B, x_temp, n) # Setting array B_3

        for i in range(0, n): # Setting array B_4
            x_temp[i][0] = x_t[i][0] + 2*get_h()*B_3[i][0]
        f_B(B_4, A, B, x_temp, n) # Setting array B_

        for i in range(0, n): # Setting array B_5
            x_temp[i][0] = x_t[i][0] + (get_h()/12)*(5*B_1[i][0] + 8*B_3[i][0] - B_4[i][0])
        f_B(B_5, A, B, x_temp, n)  # Setting array B_5

        for i in range(0, n):
            x_temp[i][0] = x_t[i][0] + (get_h()/3)*(B_1[i][0] + B_4[i][0] + B_5[i][0])
        f_B(B_6, A, B, x_temp, n)  # Setting array B_6
    print(x_t[0][0])
    print(get_h())

block(n, 1, 10)
"""