import numpy as np

"""
The Algorithm used to solve here is called the SS-SSEB Algorithm which is the most effiecient way for
finding the numerical solution for the Single-Input-Single-Output-State-Space-Equation (SISO-SSE) using the Block method.

"""

def Fi(i, j):
    # This function denotes the ith linear functional relationship.


def Block(num, i , j):
    Block_Result = Fi(i, j)
    return Block_Result

def SS_SSEB():
    "main driver"
    # Step 1: Define k and h
    k = 0       # (k + 1) is the number of the time points.
    h = (t_k - t_0) / k     # t_k is the last time point. t_0 is the initial state.

    # Step 2: get the state space equation of the system 


    #Step 3:
    # A list to store computational results of the block function.
    results = [2][k]

    for j in range(k):      # j is the number of time points.
        for i in range(n):
            """
            results.append(Block(1, i, j))
            results.append(Block(2, i, j))
            results.append(Block(3, i, j))
            results.append(Block(4, i, j))
            results.append(Block(5, i, j))
            results.append(Block(6, i, j))
            """




"""
def one_output_step():
    while x < xend :
        if xend - x < h :
            h = xend - x
        RungeKutta(x, y, n, h)

def derivative(y, t, k): 
    # For a model dy/dt = -k * y(t)
    dydt = -k * y
    return dydt

# initial condition
y0 = 5

# time points
t = np.linspace(0, 20)

#def reduce_order(model, ):
    
def RungeKutta(x0, y0, x, h): 
    n = (int)((x - x0)/h)
    y = y0 
    for i in range(1, n + 1): 
        k1 = h * dydx(x0, y) 
        k2 = h * dydx(x0 + 0.5 * h, y + 0.5 * k1) 
        k3 = h * dydx(x0 + 0.5 * h, y + 0.5 * k2) 
        k4 = h * dydx(x0 + h, y + k3) 
 
        y = y + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4) 
        x0 = x0 + h 
    return y 

x0 = 0
y = 1
x = 2
h = 0.2
print(rungeKutta(x0, y, x, h))

"""