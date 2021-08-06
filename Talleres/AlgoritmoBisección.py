#Pablo Santander
#Andres Alarcon 
#Nicolas Barragan 
#Gabriel De Souza


import numpy as np
from math import *

#Declaracion de funcion
def f(x):
  return  x*cos(x**2)+1

#Funcion de Biseccion
def Biseccion(a,b,tolerancia):
  m1 = a
  m = b
  iteracion = 0
  
  if(f(a) * f(b)) >0:
    print('La función no cambia de signo ')
  else:

    while(abs(m1-m)>tolerancia):

       m1=m
       m=(a+b)/2
       if(f(a) * f(m) < 0):
         b = m
       
       if(f(m) * f(b) < 0):
         a=m
       print("El intervalo es [{},{}]".format(a,b))
       iteracion=iteracion+1

    print(f'Iteración {iteracion}' + f' = {m} ' + ' es una buena aproximación')


#Ingreso de datos (Main)
while(1):
  a = float(input('Ingresar punto a: '))
  b = float(input('Ingresar punto b: '))
  tolerancia = float(input('Ingresar tolerancia: '))


  Biseccion(a,b,tolerancia)  


  

  
    

   
    




  
    



