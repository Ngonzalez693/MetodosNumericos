# Linear regression

import numpy as np
import matplotlib.pyplot as plt

def minSqr(x, y):

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

# Data
dataX = np.array([1.1, 2, 3.01, 4, 4.98, 6, 7.02, 8])
dataY = np.array([2.5, 5.1, 8, 9.6, 10.8, 14, 15.1, 18])

# Graphic
a0, a1 = minSqr(dataX, dataY)

resol = 20
xx = np.linspace(-1,12, resol)
yy = a0 +a1*xx

fig, ax = plt.subplots()
ax.plot(xx, yy, 'b')
ax.plot(dataX, dataY, 'o')
plt.grid()
plt.show()