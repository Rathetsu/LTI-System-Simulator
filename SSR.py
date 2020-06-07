"""
Converting an i/o differential equation into it's correspondent SSR using the CCF method
"""
import numpy as np

def standard_form(a=[], b=[]):
    """
    :param a: O/P coeffs
    :param b: I/P coeffs
    :return: The coeffs on the standard form with the coeff of the highest order of the o/p = 1
    """
    a_0 = a[0]
    for i in range(len(a)):
        a[i] /= a_0
    for i in range(len(b)):
        b[i] /= a_0
    #an = [(element / a_0) for element in a]
    #bn = [(element / a_0) for element in b]
    #return [an, bn]


def setA(a):
    """
    Sets the matrix A with dimensions n*n
    :param a: output coefficients provided as a list
    :returns: a NumPy 2D array A
    """
    standard_form(a)
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
    standard_form(a, b)
    C = []
    if len(b) == 1 and len(a) > 2:
        C.append(b[0])
        for col in range(len(a)-2):
            C.append(0.0)
    elif len(a) == len(b):
        for col in range(0, len(a)-1):
            C.append(b[len(a)-col-1] - a[len(a)-col-1]*b[0])
    else:
        for col in range(0, len(a)-1):
            C.append(b[len(b)-col-1])
    C = np.array(C)
    return C


def setD(n, m, a, b):
    """
         Sets matrix c with dimensions 1*n
        :param n: highest order of output derivatives
        :param m: highest order of input derivatives
        :param b: list of input coefficients
        :return: a NumPy 2D array D
        """
    standard_form(a, b)
    if m == n:
        D = [float(b[0])]
    else:
        D = [0]
    D = np.array(D)
    return D





