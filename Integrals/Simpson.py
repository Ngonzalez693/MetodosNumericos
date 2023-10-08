# Simpson 1/3

import numpy as np

def f(x):
    return x**2

def Simpson(a,b,n):
    xi = np.linspace(a,b,n)

    integral = (b-a)*((f(xi[0])+4*f(xi[1])+f(xi[2]))/6)

    print("Simpson 1/3: ",integral)

Simpson(0,3,3)

# Simpson n intervals

def nSimpson(a,b,n):
    xi = np.linspace(a,b,n+1)

    countOdd = 0
    countEven = 0

    for i in range(1, len(xi) - 1,2):
        countOdd += f(xi[i])
    
    for j in range(2, len(xi) - 2,2):
        countEven += f(xi[j])
    
    integral = (b-a)*(f(xi[0])+f(xi[n])+4*countOdd+2*countEven)/(3*n)

    print("Simpson 1/3 n intervals: ",integral)

nSimpson(0,3,8)

# Simpson 3/8

def Simpson3(a,b,n):

    integral = (b-a)*((f(a)+3*f(2*a+b/3)+3*f(a+2*b/32)+f(b))/8)

    print("Simpson 3/8: ",integral)

Simpson3(0,3,3)

# Simpson 3/8 n intervals

def Simpson3n(a,b,n):
    xi = np.linspace(a,b,n+1)

    integral = (b-a)*((f(a)+3*f(2*a+b/3)+3*f(a+2*b/32)+f(b))/8)

    print("Simpson 3/8 n intervals: ",integral)

Simpson3n(0,3,3)