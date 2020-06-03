import matplotlib.pyplot as plt
import numpy as np

def generate_input(u_type, t):

    k = 1000

    if u_type == 1:
        return 1

    elif u_type == 2:
        u = np.zeros(k).reshape(1, k)
        u[0] = 1
        return u




"""a = generate_input(1, 0.01, 10)
#print(a)

t = []
t = np.arange(0, 10, 0.01).reshape(1000)

print(a.shape, a.shape)


plt.plot(t, a)
plt.grid(True)
plt.show()"""