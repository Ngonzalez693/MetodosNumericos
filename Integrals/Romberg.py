# Romberg Metod

import numpy as np

def f(x):
    return x**2

def ntrapeze(a, b, n):
    xi = np.linspace(a,b,n+1)

    count = 0

    for i in range(n-1):
        count += f(xi[i+1])
    area = (b-a)*(f(xi[0])+f(xi[n])+2*count)/(2*n)
    return area

def Romberg(a, b, n):

    matrix = np.zeros((n,n))

    for j in range(0,n):
        matrix[j,0] = ntrapeze(a,b,j+1)
    
    for k in range(1,n):
        for j in range(k,n):
            matrix[j][k] = (4**(k+1-1)*matrix[j+1-1][k-1]-matrix[j-1][k-1])/(4**(k+1-1)-1)
    
    print("Integral: ", matrix[n-1,n-1])
    print(matrix)

Romberg(0,3,4)