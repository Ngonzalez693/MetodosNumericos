# Bisection Metod

def bisection(x0, x1, f, tol=0.000001):
    print("\nMétodo de Bisección\n")

    anterior = x0
    medio = ((x0 + x1) / 2)
    error = 0

    for i in range(50):
        if (f(x0) * f(x1)) < 0:
            medio = ((x0 + x1) / 2)

        error = abs((medio - anterior) / medio)

        if error <= tol:
            break

        if (f(x0) * f(medio)) < 0:
            x1 = medio
            anterior = x1
        else:
            x0 = medio
            anterior = x0

        print('{:<6} {:<22} {:<20}'.format(i, medio, error))


