import numpy as np

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

def reduce_order(model, ):
    



def RungeKutta(x0, y0, x, h): 
    # Count number of iterations using step size or 
    # step height h 
    n = (int)((x - x0)/h)  
    # Iterate for number of iterations 
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