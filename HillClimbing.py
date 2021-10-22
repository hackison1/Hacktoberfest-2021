#HILLL CLIMBING
#Autor: Rodrigo Antonio Arciniega Mendoza

"""Este programa imprime los datos de 30 ejecuciones de Hill Climbing y al final su respectivo 
    diagrama de cajas."""

import random # Libreria necesaria para generar datos aleatorios
import math # Libreria necesaria para funciones trigonometricas
from time import time # Libreria necesaria para poder medir el timpo
import matplotlib.pyplot as plt # Libreria necesaria para el diagrama de cajas

MejoresCostos=[] # Listas en donde se guardan los 30 datos obtenidos
MejoresTiempos=[]

def FO(SolActual): # Definimos la Funcion Objetivo
    a=SolActual[0]
    b=SolActual[1]
    cte=418.9829*2
    f=cte-((a*math.sin(math.sqrt(math.fabs(a))))+(b*math.sin(math.sqrt(math.fabs(b)))))
    return f

for i in range (30):
    print("Desplegado del dato ", i+1)
    tiempo_inicial=time() # Comienzo a medir el tiempo
    SolActual = [round(random.uniform(-500,500),4),round(random.uniform(-500,500),4)] # Generamos una solucion inicial aleatoria
    print('la solucion aleatoria es: ',SolActual)
    CostoActual = FO(SolActual)     # Calculamos el costo de la solucion aleatoria
    print('Y tiene un costo de: ',CostoActual)
    e=100 # Este valor de epsilon nos permite tener un vecindario mas amplio
    SinMejora=0 # Inicializamos los contadores
    Ciclos=0
    
    while SinMejora<700000 and Ciclos<10000000:      # Comienza la busqueda del valor minimo
        Ciclos=Ciclos+1
        Vecin=[round(random.uniform(-1,1),4),round(random.uniform(-1,1),4)]
        Vecino=[e*Vecin[0],e*Vecin[1]] # Generamos un vecindario diferente por cada vez que se itere el ciclo
        SolVecina=[SolActual[0]+Vecino[0],SolActual[1]+Vecino[1]] # Ese vecindario cambiara de tamaño segun cada una de las soluciones obtenidas
        if SolVecina[0]>500 or SolVecina[0]<-500: # Validamos que nuestra solucion vecina este dentro del dominio de la funcion
            if SolVecina[0]>500:
                SolVecina[0]=500-(SolVecina[0]-500)
            else:
                SolVecina[0]=-500-(SolVecina[0]+500)
        if SolVecina[1]>500 or SolVecina[1]<-500:
            if SolVecina[1]>500:
                SolVecina[1]=500-(SolVecina[1]-500)
            else:
                SolVecina[1]=-500-(SolVecina[1]+500)
        CostoVecina=FO(SolVecina) # Obtenemos el costo de la solucion vecina
        if CostoVecina <= CostoActual: # Aplicamos los criterios del Hill Climbing
            if CostoVecina == CostoActual:
                SinMejora=SinMejora+1 # Si no vemos mejora, aun asi consideramos el resultado para no reducir nuestras posibles soluciones
            else:
                CostoActual = CostoVecina # Actualizamos los valores de las soluciones optimas 
                SolActual = SolVecina
                SinMejora=0
        else:
            SinMejora=SinMejora+1

    tiempo_final=time() # Dejamos de medir el tiempo
    tiempo_total=tiempo_final-tiempo_inicial # Guardamos el tiempo en una variable

    print("El mejor costo encontrado por el algoritmo es: ",CostoActual)  # Imprimimos nuestros resultados
    print('La mejor solucion encontrada es: ',SolActual)
    print('El tiempo de ejecucion del algoritmo es: ', round(tiempo_total,4),"segundos")
    MejoresCostos.append(CostoActual)       # Guardamos nuestros mejores costos
    MejoresTiempos.append(tiempo_total)     # Guardamos nuestros mejores tiempos
    print('\n')
    print('\n')


print('Los 30 mejores Costos son:', MejoresCostos)
print('Los 30 mejores tiempos son: ', MejoresTiempos)

plt.boxplot(MejoresCostos) # Obtenemos el diagrama de cajas para los costos
plt.title("Diagrama de cajas (COSTOS)")
plt.ylabel("Costo")
plt.figure()

plt.boxplot(MejoresTiempos) # Obtenemos el diagrama de cajas para los tiempos
plt.title("Diagrama de cajas (TIEMPOS)")
plt.ylabel("Tiempo (s)")
plt.show()
