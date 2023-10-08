# Center, Forward, Back Derivates

import math 
import numpy as np
import matplotlib.pyplot as plt

def front_difference(x, h, f):
    return ((f(x + h) - f(x)) / h)

def sec_front_difference(x, h, f):
    return ((f(x + (2 * h)) - (2 * f(x + h)) + f(x)) / math.pow(h, 2))

def back_difference(x, h, f):
    return ((f(x) - f(x - h)) / h)

def sec_back_difference(x, h, f):
    return ((f(x) - (2 * f(x - h)) + f(x - (2 * h))) / math.pow(h, 2))

def center_difference(x, h, f):
    return ((f(x + h) - f(x - h)) / (2 * h))

def sec_center_difference(x, h, f):
    return ((f(x + h) - (2 * f(x)) + f(x - h)) / math.pow(h, 2))

def error(x1, x2):
    return abs(x1 - x2)

def mainDerivates(f, x):
    h = 0.001
    #x = 1.05

    print(f"\nDerivada de Adelante: { front_difference(x, h, f) }")
    print(f"Derivada de Atrás: { back_difference(x, h, f) }")
    print(f"Derivada Central: { center_difference(x, h, f) }")

    print(f"\nSegunda Derivada de Adelante: { sec_front_difference(x, h, f) }")
    print(f"Segunda Derivada de Atrás: { sec_back_difference(x, h, f) }")
    print(f"Segunda Derivada Central: { sec_center_difference(x, h, f) }")

    print(f"\nError de la Derivada de Adelante: { error(front_difference(x, h, f), (1 / 1.05)) }")
    print(f"Error de la Derivada de Atrás: { error(back_difference(x, h, f), (1 / 1.05)) }")
    print(f"Error de la Derivada Central: { error(center_difference(x, h, f), (1 / 1.05)) }")

    print(f"\nError de la Segunda Derivada de Adelante: { error(sec_front_difference(x, h, f), -(1 / math.pow(1.05, 2))) }")
    print(f"Error de la Segunda Derivada de Atrás: { error(sec_back_difference(x, h, f), -(1 / math.pow(1.05, 2))) }")
    print(f"Error de la Segunda Derivada Central: { error(sec_center_difference(x, h, f), -(1 / math.pow(1.05, 2))) }")