import math 

def cos_function(x):
    return ((1 - math.cos(x)) / (math.pow(x, 2)))

def cos_function_rational(x):
    return ((math.sin(x) / x) * (math.sin(x) / x) * (1 / (1 + math.cos(x))))

def cos_function_lhopital(x):
    return (math.sin(x) / (2 * x))

def main():
    print("Cos function: ")
    
    for i in range(15):
        x = (1.2 * math.pow(10, -i))
        
        print(f"{ i }. x = { x } ; function = { cos_function(x) }")
    
    print("\nCos function rational: ")
    
    for i in range(15):
        x = (1.2 * math.pow(10, -i))
        
        print(f"{ i }. x = { x } ; function = { cos_function_rational(x) }")
    
    print("\nCos function l'Hopital: ")
    
    for i in range(15):
        x = (1.2 * math.pow(10, -i))
        
        print(f"{ i }. x = { x } ; function = { cos_function_lhopital(x) }")

main()