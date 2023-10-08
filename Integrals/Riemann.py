import numpy as np

def f(x):
    return x**2

# Riemann with Left side
def RiemannLeftExt(a, b, n):
    dx = (b - a) / n
    xi = np.linspace(a,b,n+1)

    areaT = 0

    for i in range(n):
        areaX = dx * f(xi[i])
        areaT = areaT + areaX
        
        print(areaT) 

RiemannLeftExt(0,3,5)

# Riemann with MidPoint
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

# Riemann with Right side
def RiemannRightExt(a, b, n):
    dx = (b - a) / n
    xi = np.linspace(a,b,n+1)

    areaT = 0

    for i in range(n):
        areaX = dx * f(xi[i+1])
        areaT = areaT + areaX
        
        print(areaT) 

RiemannRightExt(0,3,5)