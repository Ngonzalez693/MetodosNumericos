# Riemann with MidPoint

import numpy as np

def f(x):
    return x**2

def RiemannMid(a, b, n):
    dx = (b - a) / n
    xi = np.linspace(a,b,n+1)
    areaT = 0

    for i in range(1, n+1):
        mid = (xi[i] + xi[i-1])/2
        areaX = dx * f(mid)
        areaT = areaT + areaX
        
        print(areaT) 

RiemannMid(0,3,5)