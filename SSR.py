"""
Converting an i/o differential equation into it's correspondent SSR using the CCF method
"""
import numpy as np

def setA(a):
    """
    Sets the matrix A with dimensions n*n
    :param a: output coefficients provided as a list
    :returns: a NumPy 2D array A
    """

    A = []
    for row in range(0, len(a)-1):
        A.append([])
        if not row == len(a)-2:
            for col in range(0, len(a)-1):
                if col == row+1:
                    A[row].append(1)
                else:
                    A[row].append(0)
        else:
            for col in range(0, len(a)-1):
                A[row].append(-1 * a[len(a)-col-1])
    A = np.array(A)
    return A


def setB(n):
    """
    Sets matrix B with dimensions n*1
    :param n: highest order of output derivatives
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


def setC(a, b):
    """
     Sets matrix c with dimensions 1*n
    :param a: list of output coefficients
    :param b: list of input coefficients
    :return: a NumPy 2D array c
    """
    C = []
    if len(a) == len(b):
        for col in range(0, len(a)-1):
            C.append(b[len(a)-col-1]-a[len(a)-col-1]*b[0])
    else:
        for col in range(0, len(b)-1):
            C.append(b[len(b)-col-1])
    C = np.array(C)
    return C


def setD(n, m, b):
    """
         Sets matrix c with dimensions 1*n
        :param n: highest order of output derivatives
        :param m: highest order of input derivatives
        :param b: list of input coefficients
        :return: a NumPy 2D array D
        """
    if m == n:
        D = [b[0]]
    else:
        D = [0]
    D = np.array(D)
    return D


#a = [1, 2, 3, 4]
#b = [10, 5, 7, 6]
#n = 3
#m = 3
#print(setA(a))
#print(setB(n))
#print(setC(a, b))
#print(setD(n, m, b))





