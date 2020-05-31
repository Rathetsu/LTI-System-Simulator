import matplotlib.pyplot as plt
import numpy as np

def generate_input(type, t: float, K: float):
    """
    parameter type can either be 1 or 2 to choose signal type.
    parameter t has to be a numerical value representing the shift amount
    parameter K represents the max number to plot for in the x axis.
    returns a list u containing the y axis values of the function. 
    """
    t = int(t * 100)
    K = int(K * 100)
    u = [0] * K

    shift = abs(t) * ( t < 0 )

    if type == 1:   # Unit Step
        u[(shift):] = [1] * (K - shift)

    if type == 2:   # Unit Impulse
        u[shift] = 1
    
    u = np.array(u).reshape(1, K)
    return u


"""a = generate_input(1, 0.01 , 10)
print(a)

t = []
t = np.arange(0, 1000)

plt.plot(t, generate_input(2, 0.01, 10))
plt.grid(True)
plt.show()"""