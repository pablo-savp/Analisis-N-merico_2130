
#Interpolación por segundo y tercer grado para 

import numpy as np 
#import matplotlib.pyplot as pt

#Valor auxliar diferente de 0
tol = 1e-16

#Interpolación de segundo grado. 
#Declaramos la matriz con las bases imponibles donde cada campo representa un polinomio
Bases = np.array([[4410000*4410000, 4410000, 1],
                  [4830000*4830000,4830000,1],
                  [5250000*5250000,5250000,1]])
#Declaramos la matriz con las cuotas integras
Cuotas = np.array([[1165978],
                   [1329190],
                   [1501474]])

Bases = np.array(Bases,dtype=float) 
BasesXCuotas = np.concatenate((Bases,Cuotas),axis=1)
aumentada = np.copy(BasesXCuotas)

#Almacenamos el tamaño de matrices
tam = np.shape(BasesXCuotas)
a = tam[0] 
b = tam[1] 

    
for i in range(0,a-1):
    col = abs(BasesXCuotas[i:,i])
    max = np.argmax(col)
    if (max !=0):
        temporal = np.copy(BasesXCuotas[i,:])
        BasesXCuotas[i,:] = BasesXCuotas[max+i,:]
        BasesXCuotas[max+i,:] = temporal
        
pivoteoParcial = np.copy(BasesXCuotas)

for i in range(0,a-1):
    pivotes = BasesXCuotas[i,i]
    adelante = i + 1
    for k in range(adelante,a,1):
        factor = BasesXCuotas[k,i]/pivotes
        BasesXCuotas[k,:] = BasesXCuotas[k,:] - BasesXCuotas[i,:]*factor
eliminacion_atras = np.copy(BasesXCuotas)

ult_fila = a-1
ult_column = b-1

for i in range(ult_fila,-1,-1):
    pivote = BasesXCuotas[i,i]
    atras = i-1 
    for k in range(atras,-1,-1):
        factor = BasesXCuotas[k,i]/pivote
        BasesXCuotas[k,:] = BasesXCuotas[k,:] - BasesXCuotas[i,:]*factor
    BasesXCuotas[i,:] = BasesXCuotas[i,:]/BasesXCuotas[i,i]
result_doble = np.copy(BasesXCuotas[:,ult_column])
result_doble = np.transpose([result_doble])

#print("Solucion por interpolacion de segundo grado:")
#print(result_doble)

V=5000000
valor_final=V*V*result_doble[0]+V*result_doble[1]+result_doble[2]
print("________________________________________________")
print("Valor final (segundo grado):", valor_final)


print(" ")
print("         /////////////////////////////")
print(" ")


#Interpolación tercer grado. 
#Declaramos la matriz de acuerdo al tercer grado 
#EL nombre3 indica que es de grado 3 
Bases3 = np.array([[4410000*4410000*4410000,4410000*4410000, 4410000, 1],
                   [4830000*4830000*4830000,4830000*4830000,4830000,1],
                   [5250000*5250000*5250000,5250000*5250000,5250000,1],
                   [5670000*5670000*5670000,5670000*5670000,5670000,1]])

Cuotas3 = np.array([[1165978],
                    [1329190],
                    [1501474],
                    [1682830]])

Bases3 = np.array(Bases3,dtype=float) 

Bases3XCuotas3 = np.concatenate((Bases3,Cuotas3),axis=1)
aumentada3 = np.copy(Bases3XCuotas3)

taman = np.shape(Bases3XCuotas3)
a3 = taman[0] 
b3 = taman[1] 


for i in range(0,a3-1):
    colum = abs(Bases3XCuotas3[i:,i])
    max = np.argmax(colum)
    if (max !=0):
        temp = np.copy(Bases3XCuotas3[i,:])
        Bases3XCuotas3[i,:] = Bases3XCuotas3[max+i,:]
        Bases3XCuotas3[max+i,:] = temp
        
pivoteo_parcial3 = np.copy(Bases3XCuotas3)

for i in range(0,a3-1):
    pivotes3 = Bases3XCuotas3[i,i]
    adelante3 = i + 1
    for k in range(adelante3,a3,1):
        factor = Bases3XCuotas3[k,i]/pivotes3
        Bases3XCuotas3[k,:] = Bases3XCuotas3[k,:] - Bases3XCuotas3[i,:]*factor
eliminacion_atras3 = np.copy(Bases3XCuotas3)

ult_fila3 = a3-1
ult_col3 = b3-1
for i in range(ult_fila3,-1,-1):
    pivot = Bases3XCuotas3[i,i]
    backwards = i-1 
    for k in range(backwards,0-1,-1):
        factor = Bases3XCuotas3[k,i]/pivot
        Bases3XCuotas3[k,:] = Bases3XCuotas3[k,:] - Bases3XCuotas3[i,:]*factor

    Bases3XCuotas3[i,:] = Bases3XCuotas3[i,:]/Bases3XCuotas3[i,i]
    
    
    
result_triple = np.copy(Bases3XCuotas3[:,ult_col3])
result_triple = np.transpose([result_triple])

#print('Solucion por interpolacion de tercer grado ')
#print(X)

valor_final3=V*V*V*result_triple[0],V*V*result_triple[1]+V*result_triple[2]+result_triple[3]


print('Valor final (Tercer grado)', valor_final3[1])
print("________________________________________________")


#Conclusiones
print(" ")
print("                Conclusion      ")
optimo = 0
if valor_final3[1] > valor_final: 
    optimo = valor_final3[1]
else: 
    optimo = valor_final
    
print("La mejor opcion para el contribuyente es : ", optimo)

















