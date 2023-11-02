# False Position Metod

import math

def false_position(a, b, f, tol = 0.000001):
    anterior = a
    error = 0

    for i in range(50):
        if (f(a) * f(b)) < 0:
            pos = (a - (((a - b) * f(a)) / (f(a) - f(b))))

        error = abs((pos - anterior) / pos) 

        if error <= tol:
            break

        if (f(a) * f(pos)) < 0:
            b = pos
            anterior = b
        else:
            a = pos
            anterior = a
    
        print('{:<6} {:<22} {:<25}'.format(i, pos, error))

def g(x):
    return (math.exp(-x) - x)

def main():
    false_position(0, 2, g)

main()