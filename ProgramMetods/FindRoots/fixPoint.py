# Fix Point Metod

def fix_point(x0, f, tol=0.000001):
    print("\nMétodo de Punto Fijo\n")

    for i in range(50):
        x1 = f(x0)
        error = abs((x1 - x0) / x1)

        if error <= tol:
            break
        else:
            x0 = x1

        print('{:<3} {:<20} {:<25}'.format(i, x1, error))