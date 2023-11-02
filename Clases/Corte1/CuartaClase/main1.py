# Secant Metod

import math

# Sec Function
def sec(x0, x1, f, tol = 0.000001):
    
    for i in range(50):
        
        derivative=der(x0, x1, f)
        pos = x0 - f(x0)/(derivative)
        error = abs((pos - x0)/pos)

        if error <= tol:
            break
        else:
            x0 = x1
            x1 = pos
    
        print('{:<6} {:<22} {:<25}'.format(i, pos, error))

# Functions
def f(x):
    #return (math.exp(-x) - x)
    return (20*math.exp(0.15*x)-100)

# Derivative
def der(x0, x1, f, h = 0.001):
    return ((f(x0) - f(x1)) / (x0-x1))

# Values
x0=0
x1=1

# Call Function
sec(x0,x1,f)