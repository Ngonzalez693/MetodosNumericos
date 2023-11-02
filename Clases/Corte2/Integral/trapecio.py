# Trapeze

import numpy as np

def f(x):
    return x**2

def trapeze(a, b, n):
    dx = (b - a) / n

    areaT = 0

    for i in range(n-1):
        areaX = dx * (f(a)+f(b)/2)
        areaT = areaT + areaX
        
    print("Trapecio: ",areaT)

trapeze(0,3,5)

# n Trapezes

def ntrapeze(a, b, n):
    xi = np.linspace(a,b,n+1)

    count = 0

    for i in range(1, len(xi) - 1):
        count += f(xi[i])

    integral = (b-a)*(f(xi[0])+f(xi[n])+2*count)/(2*n)

    print("n Trapecios: ",integral)

ntrapeze(0,3,5)