# Multiple Roots

def mul_New_Rap(x0, f, tol = 0.000001):
    print("\nMétodo de Raíces Múltiples\n")
    
    for i in range(50):
        
        derivative = der(x0,f)
        secDerivative = secDer(x0,f)

        pos = x0 -f(x0)*derivative/(derivative**2-f(x0)*secDerivative)
        error = abs((pos - x0)/pos)

        if error <= tol:
            break
        else:
            x0 = pos
    
        print('{:<6} {:<22} {:<25}'.format(i, pos, error))

def der(x0, f, h = 0.001):
    return ((f(x0 + h) - f(x0)) / h)

def secDer(x0, f, h=0.0001):
    return (f(x0+2*h)-2*f(x0+h)+f(x0))/h**2