import math 

def sqrt_function(x):
    return (math.sqrt(x + 1) - math.sqrt(x))

def main():
    print("Sqrt function: ")
    
    for i in range(50):
        x = (1.2 * math.pow(10, i))
        
        print(f"{ i }. x = { x } ; function = { sqrt_function(x) }")

main()