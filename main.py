# Imports from FindRoots
from FindRoots import fixPoint 
from FindRoots import bisection 
from FindRoots import falsPos 
from FindRoots import newRap 
from FindRoots import secant
from FindRoots import multipleRoot
from FindRoots import intervals
from FindRoots import derivatives

# Imports from integrals
from Integrals import Riemann
from Integrals import trapecio
from Integrals import Simpson
from Integrals import Romberg
from Integrals import gaussSeidel
from Integrals import jacobi
from Integrals import jacobiMatriz

# imports for operations
import math
import matplotlib.pyplot as plt
import numpy as np

# Menus
def menu1():
    print("-------------------------Menú Principal-------------------------")
    print(" 1. Raíces y Derivadas\n",
          "2. Integrales\n",
          "3. Matirces\n")

def menu2():
    print("----------------------------------------------------------------")
    print(" 1. Encontrar derivadas\n",
          "2. Buscar Raíces\n")

def menu3():
    print("--------------------------Menú Raíces---------------------------")
    print(" 1. Método de Punto Fijo (Modificar para g(x))\n",
          "2. Método de Bisección\n",
          "3. Método de Falsa Posición\n",
          "4. Método de Newton-Raphson\n",
          "5. Método de la Secante\n",
          "6. Método de Raíces Múltiples (Newton-Raphson modificado)")
    
def menu4():
    print("-------------------------Menú Integrales------------------------")
    print(" 1. Integral por Riemann\n",
          "2. Integral por Trapecios\n",
          "3. Integral por Simpson\n",
          "4. Integral por Romberg\n")
    
def menu5():
    print("-------------------------Menú Matrices--------------------------")
    print(" 1. Matriz de GaussSeidel\n",
          "2. Matriz de Jacobi (Lambdas)\n",
          "3. Matriz de Jacobi (Algebra Matricial)\n")
    
# Grafic Function
def graphic_function(f : callable, x_range = (-20, 20), step = 0.1):
    x = np.arange(x_range[0], x_range[1], step)
    y = []

    for val in x:
        try:
            y_val = f(val)
            y.append(y_val)
        except:
            y.append(float('nan'))

    plt.figure(figsize = (8,6))
    plt.plot(x, y)
    plt.title('Gráfico de la función')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()
    
# Function
def f(x):
    return x**2
    #return math.exp(-x)-x
    #return math.cos(x)
    #return math.sin(x)

menu1()
mainMenu = int(input("Qué acción quiere realizar?\n"))

if mainMenu == 1: # Derivatives and Find roots
    menu2()
    menuRaizDeri = int(input("Qué acción quiere realizar?\n"))

    if menuRaizDeri== 1:
        valueX = float(input("En que valor de X quiere la aproximación?\n"))

        derivatives.mainDerivates(f, valueX)
        graphic_function(f)

    elif menuRaizDeri == 2:
        menu3()
        rootMetod = int(input("Qué método desea usar?\n")) # Options to select metod

        # Fixed Point Metod
        if rootMetod == 1:
            x0 = 1
            fixPoint.fix_point(x0, f)
            graphic_function(f)

        # Bisection Metod
        elif rootMetod == 2:
            intervals = intervals.Search_Interval(f, -100, 100)
            if intervals:
                x0, x1 = intervals[-1]
                bisection(x0, x1, f)
            else:
                print("No se encontraron intervalos para aplicar el método de bisección.")
            graphic_function(f)

        # False Position Metod
        elif rootMetod == 3:
            intervals = intervals.Search_Interval(f, -100, 100)
            if intervals:
                x0, x1 = intervals[-1]
                falsPos.false_position(x0, x1, f)
            else:
                print("No se encontraron intervalos para aplicar el método de falsa posición.")
            graphic_function(f)

        # Newton-Raphson Metod
        elif rootMetod == 4:
            x0 = 0
            newRap.newton_raphson(x0, f)
            graphic_function(f)

        # Secant Metod
        elif rootMetod == 5:
            intervals = intervals.Search_Interval(f, -100, 100)
            if intervals:
                x0, x1 = intervals[-1]
                secant.sec(x0, x1, f)
            else:
                print("No se encontraron intervalos para aplicar el método de la secante.")
            graphic_function(f)

        # Multiple Roots
        elif rootMetod == 6:
            x0 = 0
            multipleRoot.mul_New_Rap(x0, f)
            graphic_function(f)

        else:
            print("Método no reconocido.")

elif mainMenu == 2: # Integrals
    menu4()
    integralMetod = int(input("Qué método desea usar?\n")) # Options to select metod

    # Riemann Metod
    if integralMetod == 1:
        Riemann.RiemannLeftExt(0, 3, 5, f)
        Riemann.RiemannMid(0, 3, 5, f)
        Riemann.RiemannRightExt(0, 3, 5, f)

    # Trapeze Metod
    elif integralMetod == 2:
        trapecio.trapeze(0, 3, 5, f)
        trapecio.ntrapeze(0, 3, 5, f)

    # Simpson Metod
    elif integralMetod == 3:
        Simpson.Simpson(0, 3, 3, f)
        Simpson.nSimpson(0, 3, 8, f)

    # Romberg Metod
    elif integralMetod == 4:
        Romberg.Romberg(0,3,4,f)

elif mainMenu == 3: # Matrixs
    menu5()
    matrixMetod = int(input("Qué método desea usar?\n")) # Options to select metod

    # Gauss-Seidel Matrix
    if matrixMetod == 1:
        A = np.array([[3, 1, 2],
                      [2, 1, 1],
                      [1, 4, 6]])
        b = np.array(
            [4, 6, 2]
        )
        gaussSeidel.gaussSeidel(A, b, 10, 2, tol= 0.001)

    # Jacobi Matrix (With Lambdas)
    if matrixMetod == 2:
        f1 = lambda x, y ,z: (4-y-2*z)/3 #3x, f1--> x 
        f2 = lambda x, y ,z: (6-2*x-z)/1 #y, f2--> y
        f3 = lambda x, y ,z: (2-x-4*y)/6 #6z, f3--> z

        jacobi.jacobi(f1, f2, f3)

    # Jacobi Matrix (Matrix Algebra)
    if matrixMetod == 3:
        A = np.array([[3, 1, 2],
                      [2, 1, 1],
                      [1, 4, 6]])
        b = np.array(
            [4, 6, 2]
        )
        jacobiMatriz.jacobiMatriz(A, b, 10, 2)