# Secant Metod

def sec(x0, x1, f, tol = 0.000001):
    print("\nMétodo de la Secante\n")
    
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

def der(x0, x1, f, h = 0.001):
    return ((f(x0) - f(x1)) / (x0-x1))
