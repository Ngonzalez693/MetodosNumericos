# Lagrannge Interpolation

import numpy as np
import math

# Function
def f(x):
    #return math.log(x)
    return x**2

def Lagrannge(a, b, n, f, x):
    xi = np.linspace(a, b, n)

    # Lagrange Interpolation
    LagranngeInter = 0
    for i in range(n):
        term = f(xi[i])
        for j in range(n):
            if j != i:
                term *= (x - xi[j]) / (xi[i] - xi[j])
        LagranngeInter += term

    return LagranngeInter

x = 2
interpolation = Lagrannge(1,5,5,f,x)
error = abs(interpolation - f(2))/(f(2))
print("Interpolación por Lagrannge : ", interpolation,"\nError: ",error*100)