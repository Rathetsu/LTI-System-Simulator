"""
Converting an i/o differential equation into it's correspondent SSR using the CCF method
"""
import numpy as np

def setA(n, a):
    """
    Sets the matrix A with dimensions n*n
    :param n: number of state vars
    :param a: output coefficients provided as a list

    :returns: a NumPy 2D array A
    """
    A = []
    for row in range(0, n):
        A.append([])
        if not row == n-1:
            for col in range (0, n):
                if col == row+1:
                    A[row].append(1)
                else:
                    A[row].append(0)
        else:

            A[row] = [element * -1 for element in a]
    A = np.array(A)
    return A


def setB(n):
    """
    Sets matrix B with dimensions n*1
    :param n: number of state vars
    :return: a NumPy 2D array B
    """
    B = []
    for row in range(0, n):
        B.append([])
        if not row == n-1:
            B[row].append(0)
        else:
            B[row].append(1)
    B = np.array(B)
    return B


def setC(n, m, a, b):
    """
     Sets matrix c with dimensions 1*n
    :param n: number of state vars
    :param m: highest order of input derivatives
    :param a: list of output coefficients
    :param b: list of input coefficients
    :return: a NumPy 2D array c
    """
    C = []
    if m == n:
        for col in range(0, n):
            C.append(b[col]-a[col]*b[n-col-1])
    else:
        for col in range(0, m):
            C.append(b[col])
    C = np.array(C)
    return C


def setD(n, m, b):
    """
         Sets matrix c with dimensions 1*n
        :param n: number of state vars
        :param m: highest order of input derivatives
        :param b: list of input coefficients
        :return: a NumPy 2D array D
        """
    if m == n:
        D = [b[-1]]
    else:
        D = [0]
    D = np.array(D)
    return D


#print(setA(4, [4, 3, 2, 1]))
#print(setB(5))
#print(setC(3, 3, [3, 2, 1], [5, 6, 7]))
#print(setD(3, 3, [1, 2, 3]))





