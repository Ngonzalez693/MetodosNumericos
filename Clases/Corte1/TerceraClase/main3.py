# Newton-Raphson Metod

import math

def newton_raphson(x, f, tol = 0.000001):
    anterior = x
    
    for i in range(50):
        actual = anterior - (f(anterior) / derivate(anterior, f))

        error = abs((actual - anterior) / actual) 

        if error <= tol:
            break
        else:
            anterior = actual
    
        print('{:<6} {:<22} {:<25}'.format(i, actual, error))

def g(x):
    return (math.exp(-x) - x)

def derivate(x, f, h = 0.001):
    return ((f(x + h) - f(x)) / h)

def main():
    newton_raphson(1, g)

main()