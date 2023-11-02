import math 

def taylor_series(x, N):
    result = 0
    
    for n in range(N):
        result += ((math.pow(-1, n) * math.pow(x, 2 * n)) / (math.factorial(2 * n)))
        
        print(f"{ n }. { result }")
    
    return result

def main():
    taylor_series((math.pi / 3), 10)

main()