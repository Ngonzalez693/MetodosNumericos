# Bisection Metod

import math

def bisection(a, b, f, tol = 0.000001):
    anterior = a
    error = 0

    for i in range(50):
        if (f(a) * f(b)) < 0:
            medio = ((a + b) / 2)

        error = abs((medio - anterior) / medio) 

        if error <= tol:
            break

        if (f(a) * f(medio)) < 0:
            b = medio
            anterior = b
        else:
            a = medio
            anterior = a
    
        print('{:<6} {:<22} {:<20}'.format(i, medio, error))

def g(x):
    return (math.exp(-x) - x)

def main():
    bisection(0, 1, g)

main()