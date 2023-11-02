# Riemann with Right side

import numpy as np

def f(x):
    return x**2

def RiemannRightExt(a, b, n):
    dx = (b - a) / n
    xi = np.linspace(a,b,n+1)

    areaT = 0

    for i in range(n):
        areaX = dx * f(xi[i+1])
        areaT = areaT + areaX
        
        print(areaT) 

RiemannRightExt(0,3,5)