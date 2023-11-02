# Multiple Roots

import math

def newton_raphson(x, f, tol = 0.000001):
    
    for i in range(50):
        
        derivative = der(x,f)
        secDerivative = secDer(x,f)

        pos = x -f(x)*derivative/(derivative**2-f(x)*secDerivative)
        error = abs((pos - x)/pos)

        if error <= tol:
            break
        else:
            x = pos
    
        print('{:<6} {:<22} {:<25}'.format(i, pos, error))

def f(x):
    return (math.exp(-x) - x)

def der(x, f, h = 0.001):
    return ((f(x + h) - f(x)) / h)

def secDer(x, f, h=0.0001):
    return (f(x+2*h)-2*f(x+h)+f(x))/h**2

newton_raphson(1, f)