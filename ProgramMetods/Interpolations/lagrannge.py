# Lagrannge Interpolation

import numpy as np
import math

# Function
def f(x):
    #return math.log(x)
    return x**2

def Lagrannge(a, b, n, f, x):
    # Matrix
    A = np.zeros((n,n))
    xi = np.linspace(a, b, n+1)