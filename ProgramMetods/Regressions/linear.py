# Linear regression

import numpy as np
import matplotlib.pyplot as plt

def minSqr(x, y):
    print("Mostrando gráfica de Regresión Lineal:")

    # Sumatories
    sumX = 0; sumXX = 0; sumXY = 0; sumY = 0
    n = len(x)

    for i in range(n):
        sumXY += x[i]* y[i]
        sumXX += x[i]**2
        sumX += x[i]
        sumY += y[i]

        a1 = (n*sumXY - sumX*sumY)/(n*sumXX - sumX**2)
        a0 = (sumY/n) - (a1*(sumX/n))

    return a1, a0