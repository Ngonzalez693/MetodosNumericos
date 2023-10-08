# Newton-Raphson Metod

def newton_raphson(x0, f, tol = 0.000001):
    print("\nMétodo de Newton-Raphson\n")

    anterior = x0
    
    for i in range(50):
        actual = anterior - (f(anterior) / derivate(anterior, f))

        error = abs((actual - anterior) / actual) 

        if error <= tol:
            break
        else:
            anterior = actual
    
        print('{:<6} {:<22} {:<25}'.format(i, actual, error))

def derivate(x0, f, h = 0.001):
    return ((f(x0 + h) - f(x0)) / h)