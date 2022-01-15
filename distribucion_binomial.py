'''
DISTRIBUCIONES DISCRETAS
Procure entender esta programacion con el ejemplo del lanzamiento de 3 monedas simultaneas 

'''
import numpy as np #manejo de matrices y arreglos
from numpy.random import binomial #generador aletorio de numero basado en la distribucion bonimial
from scipy.stats import binom #impleentar la funcion binomial para distribuciones binomiales. 
from math import factorial 
import matplotlib.pyplot as plt #desarrolar visualizaciones. 

def my_bynomial(k,n,p):
    return factorial(n)/factorial(k)*factorial(n-k)*pow(p,k)*pow(1-p,n-k) # Funcion de distribucion Binomial.


def plot_hist(num_intentos):

    p = 0.5 
    n= 3
    values=[0,1,2,3] #"el numero de caras de un lanzamiento de 3 monedas pueden ser estos"
    
    arr=[]
    for _ in range(num_intentos):
        arr.append(binomial(n,p))#simula las ocurrencias dentro de una distribucion binomial, en este caso simula el numero de caras obtenidas en 100 lanzamientos, cada lanzamiento con 3 monedas.
    
    count_arr=np.unique(arr, return_counts=True)  #Esta funcion cuenta las repeticiones en un vector, arroja un array con los valores unicos, y otro del numero de repeticiones. 
    vals=count_arr[0] # array con valores unicos
    rep=count_arr[1] # array con numero de repeticiones por casa valor.

    prob_simulada=count_arr[1]/len(arr) #probabilidades simuladas
    prob_teorica=[binom(3,0.5).pmf(k) for k in values] #probabilidades teoricas

    plt.bar(values,prob_simulada, color='red')
    plt.bar(values,prob_teorica,alpha=0.5,color='blue')
    plt.title('{} experimentos'.format(num_intentos))
    plt.show()


    return f'''* Si se lanzan 3 monedas simultaneamete, el numero de caras obtenidas podrian ser: {vals}. 
* Realizando esto para {num_intentos} lazamientos, el numero de repeticiones por cada valor es {rep}.
* Asi, la probabilidad simulada de sacar un  numero de caras para {num_intentos} repeticiones es  {prob_simulada}. 
* Ahora realizando la distribucion de probabilidad teorica se tiene {prob_teorica}'''



if __name__=='__main__':

    ''' Densidad de probabilidad'''

    dist=my_bynomial(2,3,0.5) 
    print(dist)
    

    #otra manea de ralizar lo mismo es
    dist2= binom(3,0.5).pmf(2) 
    print(dist2) 
    print('_'*60)

    '''
    Realiazando la funcion de densidad acumulada:
        * calcula la distribucion de probabilidad  acumulada de que
        mi variable tome valores menores o iguales a dos.
    '''
    prob_acu = binom(3,0.5).cdf(2) 
    print(prob_acu)
    print('_'*60)


    '''simulacion con 100 lanzamientos de  3 monedas 
    simulataneamente, obteniendo el numero de caras obtenido en cada lanzamiento. '''
    arr = []
    p = 0.5 
    n= 3
    for _ in range (100):
        distr_binomial=binomial(n,p) #lanza aleatoriamente el numero de caras de un lanzamiento de 3 monedas. 
        arr.append(distr_binomial)
    print(arr)
    print('_'*60)


    '''Realizando la prob simulada y la prob teorica para diferentes numero de repeticiones se tiene: '''
    plot = plot_hist(100)
    plot2 = plot_hist(10000)
    plot3 = plot_hist(100000)

    print(plot)
    print('_'*60)
    print(plot2)
    print('_'*60)
    print(plot3)
    print('_'*60)













