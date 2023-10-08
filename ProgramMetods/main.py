from fixPoint import fix_point 
from bisection import bisection 
from falsPos import false_position 
from newRap import newton_raphson 
from secant import sec
from multipleRoot import mul_New_Rap
from intervals import Search_Interval
from derivatives import mainDerivates
import matplotlib.pyplot as plt
import numpy as np

# Test functions (to find errors)
# 20**x+x --> punto fijo(despejar para g(x))
# x**5-5 --> punto fijo, newrap, multiples (Creo que no converge)
# 0.5**4-x --> punto fijo(despejar para g(x))

def menu1():
    print(" 1. Encontrar derivadas\n",
          "2. Buscar Raíces\n")

def menu2():
    print(" 1. Método de Punto Fijo\n",
          "2. Método de Bisección\n",
          "3. Método de Falsa Posición\n",
          "4. Método de Newton-Raphson\n",
          "5. Método de la Secante\n",
          "6. Método de Raíces Múltiples (Newton-Raphson modificado)")

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

menu1()
menu = int(input("Qué acción quiere realizar?\n"))

if menu== 1:
    function = input("Ingrese una función en términos de 'x': ") # Ask for function
    f = lambda x: eval(function) # Convert function in terms of lambda x
    valueX = float(input("En que valor de X quiere la aproximación?\n"))

    mainDerivates(f, valueX)
    graphic_function(f)

elif menu == 2:
    function = input("Ingrese una función en términos de 'x': ") # Ask for function
    f = lambda x: eval(function) # Convert function in terms of lambda x

    menu2()
    metod = int(input("Qué método desea usar?\n")) # Options to select metod

    # Fixed Point Metodo
    if metod == 1:
        x0 = 1
        fix_point(x0, f)
        graphic_function(f)

    # Bisection Metod
    elif metod == 2:
        intervals = Search_Interval(f, -100, 100)
        if intervals:
            x0, x1 = intervals[-1]
            bisection(x0, x1, f)
        else:
            print("No se encontraron intervalos para aplicar el método de bisección.")
        graphic_function(f)

    # False Position Metod
    elif metod == 3:
        intervals = Search_Interval(f, -100, 100)
        if intervals:
            x0, x1 = intervals[-1]
            false_position(x0, x1, f)
        else:
            print("No se encontraron intervalos para aplicar el método de falsa posición.")
        graphic_function(f)

    # Newton-Raphson Metod
    elif metod == 4:
        x0 = 0
        newton_raphson(x0, f)
        graphic_function(f)

    # Secant Metod
    elif metod == 5:
        intervals = Search_Interval(f, -100, 100)
        if intervals:
            x0, x1 = intervals[-1]
            sec(x0, x1, f)
        else:
            print("No se encontraron intervalos para aplicar el método de la secante.")
        graphic_function(f)

    # Multiple Roots
    elif metod == 6:
        x0 = 0
        mul_New_Rap(x0, f)
        graphic_function(f)

    else:
        print("Método no reconocido.")