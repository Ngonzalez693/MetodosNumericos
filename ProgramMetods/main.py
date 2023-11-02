# Imports from FindRoots
from FindRoots import fixPoint 
from FindRoots import bisection 
from FindRoots import falsPos 
from FindRoots import newRap 
from FindRoots import secant
from FindRoots import multipleRoot
from FindRoots import intervals
from FindRoots import derivatives

# Imports from Integrals
from Integrals import Riemann
from Integrals import trapecio
from Integrals import Simpson
from Integrals import Romberg
from Integrals import gaussSeidel
from Integrals import jacobi
from Integrals import jacobiMatriz

# Imports from Probabilities
from Probabilities import probabilities

# Imports from Regressions
from Regressions import linear
from Regressions import polinomial

# Imports from Interpolations
from Interpolations import newtonInter
from Interpolations import lagrannge

# imports for operations
import math
import matplotlib.pyplot as plt
import numpy as np

# Menus
def mainMenu():
    print("-------------------------Menú Principal-------------------------")
    print(" 1. Raíces y Derivadas\n",
          "2. Integrales\n",
          "3. Matirces\n",
          "4. Regresiones\n",
          "5. Interpolaciones\n",
          "6. Probabilidad\n")

def derivativesAndRootsMenu():
    print("----------------------------------------------------------------")
    print(" 1. Encontrar derivadas\n",
          "2. Buscar Raíces\n")

def rootsMenu():
    print("--------------------------Menú Raíces---------------------------")
    print(" 1. Método de Punto Fijo (Modificar para g(x))\n",
          "2. Método de Bisección\n",
          "3. Método de Falsa Posición\n",
          "4. Método de Newton-Raphson\n",
          "5. Método de la Secante\n",
          "6. Método de Raíces Múltiples (Newton-Raphson modificado)\n")
    
def integralsMenu():
    print("-------------------------Menú Integrales------------------------")
    print(" 1. Integral por Riemann\n",
          "2. Integral por Trapecios\n",
          "3. Integral por Simpson\n",
          "4. Integral por Romberg\n")
    
def matrixsMenu():
    print("-------------------------Menú Matrices--------------------------")
    print(" 1. Matriz de GaussSeidel\n",
          "2. Matriz de Jacobi (Lambdas)\n",
          "3. Matriz de Jacobi (Algebra Matricial)\n",
          "4. Matriz identidad")

def regressionsMenu():
    print("------------------------Menú Regresiones------------------------")
    print(" 1. Regresión Lineal\n",
          "2. Regresión Polinomial\n")
    
def interpolationsMenu():
    print("----------------------Menú Interpolaciones----------------------")
    print(" 1. Interpolación por Newton\n",
          "2. Interpolación por Lagrannge\n")
    
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
    #return x**2
    #return math.exp(-x**2)
    #return math.cos(x)
    #return math.sin(x)
    return math.log(x)

mainMenu()
mainMenu = int(input("Qué acción quiere realizar?\n"))

if mainMenu == 1: # Derivatives and Find roots
    derivativesAndRootsMenu()
    menuRaizDeri = int(input("Qué acción quiere realizar?\n"))

    if menuRaizDeri== 1:
        valueX = float(input("En que valor de X quiere la aproximación?\n"))

        derivatives.mainDerivates(f, valueX)
        graphic_function(f)

    elif menuRaizDeri == 2:
        rootsMenu()
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
            print("La opción elegida no existe")
            
    else:
        print("La opción elegida no existe")

elif mainMenu == 2: # Integrals
    integralsMenu()
    integralMetod = int(input("Qué método desea usar?\n")) # Options to select metod

    # Riemann Metod
    if integralMetod == 1:
        Riemann.RiemannLeftExt(0, 3, 5, f)
        Riemann.RiemannMid(0, 3, 5, f)
        Riemann.RiemannRightExt(0, 3, 5, f)

    # Trapeze Metod
    elif integralMetod == 2:
        trapecio.trapeze(0, 20000, 5, f)
        trapecio.ntrapeze(0, 20000, 5, f)

    # Simpson Metod
    elif integralMetod == 3:
        Simpson.Simpson(0, 20000, 3, f)
        Simpson.nSimpson(0, 20000, 8, f)

    # Romberg Metod
    elif integralMetod == 4:
        Romberg.Romberg(0,20000,4,f)

    else:
        print("La opción elegida no existe")


elif mainMenu == 3: # Matrixs
    matrixsMenu()
    matrixMetod = int(input("Qué método desea usar?\n")) # Options to select metod

    # Gauss-Seidel Matrix
    if matrixMetod == 1:
        A = np.array([[6, 2, 1],
                      [2, 3, 1],
                      [2, 1, 4]])
        b = np.array(
            [1, 0, 0]
        )
        gaussSeidel.gaussSeidel(A, b, 10, 2, tol= 0.001)

    # Jacobi Matrix (With Lambdas)
    elif matrixMetod == 2:
        f1 = lambda x, y ,z: (4-y-2*z)/3 #3x, f1--> x 
        f2 = lambda x, y ,z: (6-2*x-z)/1 #y, f2--> y
        f3 = lambda x, y ,z: (2-x-4*y)/6 #6z, f3--> z

        jacobi.jacobi(f1, f2, f3)

    # Jacobi Matrix (Matrix Algebra)
    elif matrixMetod == 3:
        A = np.array([[3, 1, 2],
                      [2, 1, 1],
                      [1, 4, 6]])
        b = np.array(
            [4, 6, 2]
        )
        jacobiMatriz.jacobiMatriz(A, b, 10, 2)

    #Matriz inversa e identidad
    elif matrixMetod == 4:
        
        A = np.array([[6, 2, 1, 0],
                      [2, 3, 1, 0],
                      [2, 1, 4, 2],
                      [1, 0, 0, 3]])
        
        B = np.linalg.inv(A)

        C = np.dot(A,B)

        print("Matriz")
        print(A)

        print("\nInversa")
        print(B)

        print("\nIdentidad")
        print (C)

    else:
        print("La opción elegida no existe")


elif mainMenu == 4: # Regressions
    regressionsMenu()
    regressionType = int(input("Qué tipo de regresión desea usar?\n")) # Options to select metod

    # Linear Regression
    if regressionType == 1:
        dataX = np.array([1.1, 2, 3.01, 4, 4.98, 6, 7.02, 8])
        dataY = np.array([2.5, 5.1, 8, 9.6, 10.8, 14, 15.1, 18])
        a0, a1 = linear.minSqr(dataX, dataY)

        # Graphic Linear Regression
        resol = 20
        xx = np.linspace(-1,12, resol)
        yy = a0 +a1*xx
        fig, ax = plt.subplots()
        ax.plot(xx, yy, 'b')
        ax.plot(dataX, dataY, 'o')
        plt.grid()
        plt.show()
    
    # Polinomial Regression
    elif regressionType == 2:
        dataX = np.array([1.1, 2.1, 3.01, 4, 4.98, 6.1, 7.02, 8, 9, 10])
        dataY = np.array([4.1, 5.2, 12.2, 19, 31, 43, 52, 71, 84.6, 104])
        m = 2; n = len(dataX)
        if n < m + 1:
            print('Pocos datos (n < m + 1)')
        else:
            a0, a1, a2 = polinomial.minSqr(dataX, dataY, m, n)

        # Graphic Polinomial Regression
        resol = 100
        xx = np.linspace(-2, 12, resol)
        yy = a0 + a1*xx + a2*xx**2

        fig, ax = plt.subplots()
        ax.plot(xx, yy, 'r')
        ax.plot(dataX, dataY, 'o')
        plt.grid()
        plt.show()
    
    else:
        print("La opción elegida no existe")


elif mainMenu == 5: # Interpolations
    interpolationsMenu()
    interpolMetod = int(input("Qué método desea usar?\n")) # Options to select metod

    # Interpolation for Newton
    if interpolMetod == 1:
        x = 2
        interpolation = newtonInter.Newton(1,5,5,f,x)
        error = abs(interpolation - f(2))/(f(2))
        print("Interpolación por Newton : ", interpolation,"\nError: ",error*100)
    
    elif interpolMetod == 2:
        lagrannge.Lagrannge()
    
    else:
        print("La opción elegida no existe")

#elif mainMenu == 6: # Probabilities

else:
    print("La opción elegida no existe")
    