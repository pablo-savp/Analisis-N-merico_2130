import numpy as np
import math

#Funciones
def fx(x,indicador):  
  if(indicador==1):
    return (np.cos(x)**2)-(x**2)
  if(indicador==2):
    return np.exp(x)-x-1
  if(indicador==3):
    return (x**3)-(2*(x**2))+(1.33*x)-(0.30)
  if(indicador==4):
    return (x**3)-(2*x)-5
  if(indicador==5):
    return (((667.38/x)*(1-(np.exp(-0.146843*x))))-40)
  if(indicador==6):
    return 3*(np.sin(x**3))-1


def gx(x,indicador):
  if(indicador==1):
    return np.cos(x)
  if(indicador==2):
    return np.log(x+1)
  if(indicador==3):
    return np.cbrt((2*(x**2)-(4/3*x)+(8/27)))
  if(indicador==4):
    return np.cbrt(2*x+5)
  if(indicador==5):
    return (-677.38+(40*x))/((np.exp(-0.146843*x))*x)
  if(indicador==6):
    return 4*(np.sin(x))*(np.cos(x))


#STEFFENSEN 
def steffensen(tol,p0, No,opcion):
    print("\n--Metodo de Steffensen--")
    p0=1
    iteraciones = 0
    No = 1000 #Maximas iteraciones
  
    while iteraciones < No:
        p1=gx(p0,opcion)
        p2=gx(p1,opcion)
        p=p2-((p2-p1)**2)/(p2-(2*(p1+p0)))


        
        if abs(p-p0)<tol:
            print("El valor de x, tal que f(x)=0 es: {} ".format(p))
            print("Las iteraciones fueron: ", iteraciones)
            return p;
        
        iteraciones = iteraciones + 1
        p0=p
    
    print("Proceso finalizado con iteraciones: ", iteraciones)

#PUNTO FIJO 
def puntofijo(Tolerancia,a,b,opcion):
  print("--Metodo de Punto fijo--")
  c=1
  if gx(a,opcion) > a and gx(b,opcion) < b: 

    if c==1: 

      xi = 0
      Error = np.abs(gx(xi,opcion)-xi)
      i = 0 #Contador de iteraciones
            
      while (Error>Tolerancia and i<=100):

        #print(i,'  xi =',xi, '  f(xi)=',fx(xi,opcion), '  g(xi)=',gx(xi,opcion), '  Error= ', Error)
        if i > 0:
          Error = np.abs(gx(xi,opcion)-xi)

        xi=gx(xi,opcion)
        i+=1
             
      print("El valor de x, tal que f(x)=0 es: {} ".format(xi))
      print("Las iteraciones fueron: {} ".format(i))
    else:

      print("La funcion no converge")
  else:
    print("La funcion no converge")

#AITKEN   
def aitkenF(p0,tolerancia,opcion): 

    print("\n--Metodo de Aitken-")
    xi=0
    i=0
    iteraciones=0
    p1 = gx(p0,opcion) 
    p2 = gx(p1,opcion)
    Error = np.abs(gx(xi,opcion)-xi)

    while(Error>tolerancia and i<=100):
      
        Error = np.abs(gx(p1,opcion)-p1)
        P0 = p0-((p1-p0)**2) / (p2-2*p1+p0)
        p0 = p1
        p1=p2
        p2 = gx(p1,opcion)
        i+=i
        iteraciones+=1
    print(P0)
        
    print("El valor de x, tal que f(x)=0 es: {} ".format(P0))
    print("Las iteraciones fueron: ", iteraciones)
    print("\n")

#BISECCION   
def biseccion(a,b,TOL,No,opcion):
    print("\n--Metodo de Biseccion-")
    i=1
    while i<=No:
        p=a+((b-a)/2)
        if fx(p,opcion)==0 or (b-a)/2<TOL: 
           print("El valor de x, tal que f(x)=0 es: {} ".format(p))
           print("Las iteraciones fueron: ", i)
           return p
        
        i=i+1
        if(fx(a,opcion)*fx(p,opcion)>0):
            a=p; 
        else: 
            b=p; 
            
def paracaidista(opcion):
  
  print("\n--Paracaidista--\n ")
  i=1
  print("Ecuacion hallada: (((667.38/x)*(1-(np.exp(-0.146843*x))))-40)\n")
  print("Lista de valores encontrados, tras diferentes asignaciones de valor a x\n")
  while(i<20):
    p=fx(i,opcion)
    i+=1
    print("Valor de x: ",i)
    print("Resultado: ",p)

  print("El coeficiente de arrastre W hallado es: 14.375772149913587 ")

while(1):
#Menu principal
  print("\nSeleccionar una ecuacion: ")
  print("1. cos(x^2)-x^2")
  print("2. e^x-x-1")
  print("3. x^3-2x^2+4/3x-8/27")
  print("4. x^3-2x-5 ")
  print("5. Problema de paracaidista")
  print("6. f(x)=3sin^3(x)-1 | g(x)=4sin(x)cos(x) | x>=0")
  opcion=int(input())

  #Ingreso de parametros
  if opcion != 5:
    print("Ingresar una tolerancia: ")
    Tolerancia = float(input()) ##  
    print("Ingresar punto a: ")
    a = float(input())
    print("Ingresar punto b: ") 
    b = float(input())

    #Llamado de funciones
    puntofijo(Tolerancia,a,b,opcion)
    biseccion(a,b,Tolerancia,1000,opcion)
    steffensen(Tolerancia,1,1000,opcion)
    aitkenF(2,Tolerancia,opcion)
    
  if opcion==5:
    paracaidista(opcion)


