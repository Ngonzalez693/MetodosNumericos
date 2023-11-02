# Riemann with Left side

import numpy as np

def f(x):
    return x**2

def RiemannLeftExt(a, b, n):
    dx = (b - a) / n
    xi = np.linspace(a,b,n+1)

    areaT = 0

    for i in range(n):
        areaX = dx * f(xi[i])
        areaT = areaT + areaX
        
        print(areaT) 

RiemannLeftExt(0,3,5)