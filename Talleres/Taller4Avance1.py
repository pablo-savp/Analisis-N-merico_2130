# Simpson's 3/8 Rule
import math
# Define function to integrate
def f(x):
    return 4+(math.cos(x+1))
def g(x):
    return (e**x)*math.sin(x)

# Implementing Simpson's 3/8
def simpson38(x0,xn,n):
    # calculating step size
    h = (xn - x0) / n
    
    # Finding sum 
    integration = f(x0) + f(xn)
    
    for i in range(1,n):
        k = x0 + i*h
        
        if i%2 == 0:
            integration = integration + 2 * f(k)
        else:
            integration = integration + 3 * f(k)
    
    # Finding final integration value
    integration = integration * 3 * h / 8
    
    return integration
    
# Input section
lower_limit = float(input("Entrar el limite inferior: "))
upper_limit = float(input("Entrar el limite superior: "))
sub_interval = int(input("# de sub intervalos: "))

# Call trapezoidal() method and get result
result = simpson38(lower_limit, upper_limit, sub_interval)
print("Resultado usando Simpson's 3/8 metodo es: %0.6f" % (result) )