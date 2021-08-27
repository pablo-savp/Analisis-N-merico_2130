#!/usr/bin/env python
# coding: utf-8

# In[42]:


import numpy as np
import matplotlib.pyplot as plt

print('\n\t\tNewton Rhapson \n')

#Funcion original
def f(x):
    return (x**3)+(2*x)+2

#Derivada de la funcion
def df(x):
    return (3*x**2)+2


xi = 1 #Punto Inicial
tol = 1e-8
it=1
cabecera= "{:<8} {:<8} {:<8} {:<8}".format('Itera', 'x_i', 'x_i+1', 'Eabs')
print(cabecera)

while True:
    if( df(xi) == 0 ):
        xi = float(input('La derivada en evaluada en este punto es 0 \n Ingresar otro punto:'))
        continue
    
    xi1 = xi- (f(xi)/df(xi))
    Ea = abs(xi1 - xi)
    fila= "{:<8} {:<8.4g} {:<8.4g} {:<8.4g} ".format(it, xi, xi1, Ea)
    print(fila)
    xi = xi1
    it+=1
    
    if ( Ea < tol ):
        print("Raiz encontrada:")
        print("{:<8.4g}".format(xi1) )
        break
        
x = np.linspace(-3,8,100)
plt.figure(num="Newton")
plt.xlim(-5, 5)
plt.ylim(-3, 6)
plt.plot(x, df(x), label='df(x)')
plt.plot(x, f(x), label='f(x)')
plt.axvline(xi1,label = f"f(x)=0, x={xi1:.6f}", color = 'r')
plt.legend(loc = 'upper right')
plt.grid('on')
plt.show()



# In[ ]:




