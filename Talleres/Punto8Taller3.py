#!/usr/bin/env python
# coding: utf-8

# In[31]:


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 3, 15)
y = np.exp(x)

plt.figure()
plt.plot(x, y)
plt.xlabel('$x$')
plt.ylabel('$\exp(x)$')
plt.show()


# In[ ]:


get_ipython().system('pip install gekko ')


# In[15]:


from gekko import gekko
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps

def f(x):
    return np.exp(x)

# Creo modelo con GEKKO
c = gekko()

# Spline Cubico
x = c.Var(value=1,lb=0,ub=3)
y = c.Var()
x_data = np.random.rand(15)*3+0.06
y_data = f(x_data)
c.cspline(x,y,x_data,y_data,True)
c.Obj(y)

# Opciones de Gekko
c.options.IMODE = 3
c.options.CSV_READ = 0
c.options.SOLVER = 3
c.solve()

# Espacio para el plot
z = np.linspace(0,3,20)


# Check if solved successfully
if c.options.SOLVESTATUS == 1:
    plt.figure()
    plt.plot(z,f(z),'r-',label='original')
    plt.scatter(x_data,y_data,18,'b',label='dato')
    plt.scatter(x.value,y.value,200,'k','x',label='minimo')
    plt.legend(loc='best')
else:
    print ('No converge')
    plt.figure()
    plt.plot(z,f(z),'r-',label='original')
    plt.scatter(x_data,y_data,7,'b')
    plt.legend(loc='best')

plt.title("Spline cubico y Área bajo la curva")
plt.fill_between(z,f(z),color='c',alpha =0.4)
plt.show()

#Area bajo la curva
print("Area abajo la curva")

area = simps(y_data)
area=float("{:.9f}".format(area))
print("Mediante metodo de simpson, area =", area)

#Calculo de los errores



# In[ ]:




