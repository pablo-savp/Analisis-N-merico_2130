#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# Calcula n términos del polinomio de Taylor
# funcionx es simbólica
def politaylor(fx,x0,n):
    k = 0
    polinomio = 0
    while (k <= n):
        derivada   = fx.diff(x,k)
        derivadax0 = derivada.subs(x,x0)
        divisor   = np.math.factorial(k)
        terminok  = (derivadax0/divisor)*(x-x0)**k
        polinomio = polinomio + terminok
        k = k + 1
    return(polinomio)


# INGRESO

# variable x es simbólica
x = sym.Symbol('x')
fx = sym.sqrt(x+1)

x0 = 1
xi = 3/2 # donde se evalua el polinomio
n  = 3

# PROCEDIMIENTO

# Referencia, f(xi) real
fxi = fx.subs(x,xi)

# Aproximado con Taylor
polinomio = politaylor(fx,x0,n)
pxi = polinomio.subs(x,xi)

error_real = fxi - pxi

# SALIDA
print(' Taylor:     ', polinomio)
print(' xi:         ', xi)
print(' estimado  : ', pxi)
print(' real:       ', fxi)
print(' error real: ', error_real)

fxn = sym.lambdify(x,fx,'numpy')
pxn = sym.lambdify(x,polinomio,'numpy')

# intervalo usando xi como referencia
a = x0        # izquierda
b = x0 + 3*xi # derecha
muestras = 51

xin = np.linspace(a,b,muestras)
fxni = fxn(xin)
pxni = pxn(xin)

# Gráfica
plt.plot(xin,fxni,label='f(x)')
plt.plot(xin,pxni,label='p(x)')

plt.fill_between(xin,pxni,fxni,color='yellow')
plt.axvline(x0,color='green')

plt.title('Polinomio Taylor: f(x) vs p(x)')
plt.legend()
plt.xlabel('xi')
plt.show()


# In[ ]:




