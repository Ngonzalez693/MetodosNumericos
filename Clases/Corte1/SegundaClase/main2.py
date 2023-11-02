# Fix Point Metod

import math

def g(x):
    return math.exp(-x)

def fix_point(x0, g, tol = 0.000001):
    xold = x0

    for i in range(50):
        xnew = g(xold)
        error = abs((xnew - xold) / xnew)

        print('{:<3} {:<20} {:<25}'.format(i, xnew, error))

        if error<= tol:
            break
        else:
            xold = xnew

def main():
    x0 = 1

    fix_point(x0, g)

main()