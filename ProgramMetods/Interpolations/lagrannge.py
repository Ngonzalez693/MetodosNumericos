# Lagrannge Interpolation

import numpy as np

def Lagrannge(a, b, n, f, x):
    print("-------------------Interpolación por Lagrange-------------------")
    xi = np.linspace(a, b, n)

    # Lagrange Interpolation
    LagranngeInter = 0
    for i in range(n):
        term = f(xi[i])
        for j in range(n):
            if j != i:
                term *= (x - xi[j]) / (xi[i] - xi[j])
        LagranngeInter += term

    return LagranngeInter