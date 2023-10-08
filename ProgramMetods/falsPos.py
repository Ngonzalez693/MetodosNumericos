# False Position Metod
from math import exp
def false_position(x0, x1, f, tol = 0.000001):
    print("\nMétodo de Falsa Posición\n")

    anterior = x0
    error = 0

    for i in range(50):
        if (f(x0) * f(x1)) < 0:
            pos = (x0 - (((x0 - x1) * f(x0)) / (f(x0) - f(x1))))

        error = abs((pos - anterior) / pos) 

        if error <= tol:
            break

        if (f(x0) * f(pos)) < 0:
            x1 = pos
            anterior = x1
        else:
            x0 = pos
            anterior = x0
    
        print('{:<6} {:<22} {:<25}'.format(i, pos, error))


