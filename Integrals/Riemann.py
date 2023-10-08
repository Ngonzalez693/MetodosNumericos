import numpy as np

# Riemann with Left side
def RiemannLeftExt(a, b, n, f):
    print("-------------------------Método Riemann-------------------------")
    dx = (b - a) / n
    xi = np.linspace(a,b,n+1)

    areaT = 0

    for i in range(n):
        areaX = dx * f(xi[i])
        areaT = areaT + areaX
        
    print("Riemann por izq: ",areaT) 

# Riemann with MidPoint
def RiemannMid(a, b, n, f):
    dx = (b - a) / n
    xi = np.linspace(a,b,n+1)
    areaT = 0

    for i in range(1, n+1):
        mid = (xi[i] + xi[i-1])/2
        areaX = dx * f(mid)
        areaT = areaT + areaX
        
    print("Riemann por cen: ",areaT) 

# Riemann with Right side
def RiemannRightExt(a, b, n, f):
    dx = (b - a) / n
    xi = np.linspace(a,b,n+1)

    areaT = 0

    for i in range(n):
        areaX = dx * f(xi[i+1])
        areaT = areaT + areaX
        
    print("Riemann por der: ",areaT)