# Center, Forward, Back Derivates

import math 
import numpy as np
import matplotlib.pyplot as plt

def front_difference(x, h):
    return ((math.log(x + h) - math.log(x)) / h)

def sec_front_difference(x, h):
    return ((math.log(x + (2 * h)) - (2 * math.log(x + h)) + math.log(x)) / math.pow(h, 2))

def back_difference(x, h):
    return ((math.log(x) - math.log(x - h)) / h)

def sec_back_difference(x, h):
    return ((math.log(x) - (2 * math.log(x - h)) + math.log(x - (2 * h))) / math.pow(h, 2))

def center_difference(x, h):
    return ((np.log(x + h) - np.log(x - h)) / (2 * h))

def sec_center_difference(x, h):
    return ((math.log(x + h) - (2 * math.log(x)) + math.log(x - h)) / math.pow(h, 2))

def calculate_tan(x0, x1, h):
    return (np.log(x1) + (center_difference(x0, h) * (x1 - x0)))

def error(x1, x2):
    return abs(x1 - x2)

def graphic(h):
    xx = np.linspace(0.5, 1.5, 100)
    y_derived = center_difference(xx, h)
    y_normal = np.log(xx)
    plt.figure()

    plt.plot(xx, y_normal, label = 'Log(x)', color = 'blue')
    plt.plot(xx, y_derived, label = 'Log`(x)', color = 'red')
    plt.plot(xx, calculate_tan(1.05, xx, h), label = 'Tan(x)', color = 'black')

    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graphic of Log(x)')
    plt.grid(True)

    plt.show()

def main():
    h = 0.001
    x = 1.05

    print(f"\nFront difference: { front_difference(x, h) }")
    print(f"Back difference: { back_difference(x, h) }")
    print(f"Center difference: { center_difference(x, h) }")

    print(f"\nSecond front difference: { sec_front_difference(x, h) }")
    print(f"Second back difference: { sec_back_difference(x, h) }")
    print(f"Second center difference: { sec_center_difference(x, h) }")
    
    print(f"\nError front difference: { error(front_difference(x, h), (1 / 1.05)) }")
    print(f"Error back difference: { error(back_difference(x, h), (1 / 1.05)) }")
    print(f"Error center difference: { error(center_difference(x, h), (1 / 1.05)) }")

    print(f"\nError second front difference: { error(sec_front_difference(x, h), -(1 / math.pow(1.05, 2))) }")
    print(f"Error second back difference: { error(sec_back_difference(x, h), -(1 / math.pow(1.05, 2))) }")
    print(f"Error second center difference: { error(sec_center_difference(x, h), -(1 / math.pow(1.05, 2))) }")
    
    graphic(h)

main()