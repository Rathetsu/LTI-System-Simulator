import matplotlib.pyplot as plt
import numpy

def generate_input(type, t: float, k: float):
    """
    parameter type can either be 1 or 2 to choose signal type.
    parameter t has to be a numerical value representing the shift amount
    parameter k is the total number of time steps excluding the last step.
    returns a list u containing the y axis values of the function. 
    """
    t = int(t * 100)
    k = int(k * 100)
    u = [0] * k

    shift = abs(t) * ( t < 0 )

    if type == 1:   # Unit Step
        u[(shift):] = [1] * (k - shift)

    if type == 2:   # Unit Impulse
        u[shift] = 1
    
    return u


print(generate_input(1, 0.01 , 10))
