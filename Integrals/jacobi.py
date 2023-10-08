import numpy as np
from numpy import linspace
import math

f1 = lambda x, y ,z: (4-y-2*z)/3 #3x, f1--> x 
f2 = lambda x, y ,z: (6-2*x-z)/1 #y, f2--> y
f3 = lambda x, y ,z: (2-x-4*y)/6 #6z, f3--> z



def jacobi(f1, f2, f3,tol = 0.001):
    iter = 5; p=2; 
    x0 = 0; y0= x0; z0 = x0

    for i in range(iter):

        x1 = f1(x0, y0, z0)
        y1 = f2(x0, y0, z0)
        z1 = f3(x0, y0, z0)
        error = abs  (math.sqrt((x1-x0)**p + (y1-y0)**p + (z1-z0)**p) / math.sqrt((x1 + y1 + z1)**p) )

        if error <= tol:
            break
        else: 
            x0 = x1
            y0 = y1
            z0 = z1
        
        print('{:d} \t {:.4f} \t {:.4f} \t {:.4f} \t {:.4f}'.format(i+1, x1, y1, z1, error))

#print("----------------------------Jacobi----------------------------")
#print('{:s} \t {:<10} \t {:<10} \t {:<10} \t {:s}'.format('Iter', 'x', 'y', 'z', 'error'))
#jacobi(f1, f2, f3)
        

    