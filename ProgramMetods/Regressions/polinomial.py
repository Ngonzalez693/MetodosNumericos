# Polinomial regression

import numpy as np
import matplotlib.pyplot as plt

# Matrix
def Gauss(sumXY, sumXX, sumXXX, sumXXXX, sumXXY, sumX, sumY, n):
    A = np.array(([n, sumX, sumXX],
                 [sumX, sumXX, sumXXX],
                 [sumXX, sumXXX, sumXXXX]))

    b = np.array([sumY, sumXY, sumXXY])

    solutionVector = np.dot(np.linalg.inv(A),b)

    return solutionVector

def minSqr(x, y, m, n):
    print("Mostrando gráfica de Regresión Polinomial:")

    # Sumatories
    sumX = 0; sumXX = 0; sumXXX = 0; sumXXXX = 0; sumY = 0; sumXY = 0; sumXXY = 0

    for i in range(len(x)):
        sumXY += x[i]* y[i]
        sumXX += x[i]**2
        sumXXX += x[i]**3
        sumXXXX += x[i]**4
        sumXXY += x[i]**2 * y[i]
        sumX += x[i]
        sumY += y[i]

        a0, a1, a2 = Gauss(sumXY, sumXX, sumXXX, sumXXXX, sumXXY, sumX, sumY, n)

    return a0, a1, a2