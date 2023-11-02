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

dataX = np.array([1.1, 2.1, 3.01, 4, 4.98, 6.1, 7.02, 8, 9, 10])
dataY = np.array([4.1, 5.2, 12.2, 19, 31, 43, 52, 71, 84.6, 104])

m = 2; n = len(dataX)
if n < m + 1:
    print('Pocos datos (n < m + 1)')
else:
    a0, a1, a2 = minSqr(dataX, dataY, m, n)

resol = 100
xx = np.linspace(-2, 12, resol)
yy = a0 + a1*xx + a2*xx**2

fig, ax = plt.subplots()
ax.plot(xx, yy, 'r')
ax.plot(dataX, dataY, 'o')
plt.grid()
plt.show()