# Newton Interpolation

import numpy as np
import math

# Function
def f(x):
    return math.log(x)

def Newton(a, b, n, f, x):
    # Matrix
    A = np.zeros((n,n))
    xi = np.linspace(a, b, n)

    # Products
    product = np.zeros(n)
    product[0] = 1
    product[1] = x - xi[1]
    for i in range(1, n):
        product[i] = product[i-1]*(x-xi[i-1])
    #print(product)

    # Add in matrix by row
    row = 0
    start = 0
    for j in range(n):
        if j==0:
            for i in range(n):
                A[i][j] = f(xi[i])
        else:
            for i in range(row, n):
                A[i][j] = (A[i][j-1] - A[i-1][j-1])/(xi[i] - xi[start])
                start += 1
            start = 0
        row += 1
    
    print(A)
    diagonal = np.diag(A)

    # Newton Interpolation
    NewtonInter = f(xi[0])
    for i in range(n):
        NewtonInter += diagonal[i]*product[i]

    return NewtonInter

x = 2
interpolation = Newton(1,5,5,f,x)
error = abs(interpolation - f(2))/(f(2))
print("Newton Interpolation: ", interpolation,"\nError: ",error*100)