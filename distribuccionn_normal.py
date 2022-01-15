'''
Distribuccion normal

    x = cada elemento de la distribuccion
    mu = media
    sigma = desviacion estandar
'''
import pandas as pd # version de excel para python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def gaussian(x,mu,sigma):
    return (1/(sigma*np.sqrt(2*np.pi)))*np.exp(-0.5*pow((x-mu)/sigma, 2))

if __name__ == '__main__':

    #calculando las forma de generar una distribucion normal = densidad de probabilidad normal
    x=np.arange(-4,4,0.1)
    mu = 0.0
    sigma = 1.0
    y=gaussian(x,mu,sigma)
    plt.plot(x,y)
    plt.title('Densidad de probabilidad 1')
    plt.grid()
    plt.show()

    #otra forma de hacerlo es usando scipy
    dist = norm(mu,sigma) #permite contruir una distribucion normal (media, desviacion estandar)
    x = np.arange(-4,4,0.1)
    y = [dist.pdf(value) for value in x] #pdf= funcion de densidad de probabilidad
    plt.plot(x, y)
    plt.title('Densidad de probabilidad 2')
    plt.grid()
    plt.show()

    #Calculando la funcion de  distribucion acumulada 
    dist = norm(mu, sigma)
    x = np.arange(-4,4,0.1)
    y=[dist.cdf(value) for value in x] #.cdf= 
    plt.title('Desidad o distribucion acumulada')
    plt.plot(x,y)
    plt.grid()
    plt.show()


    '''Con base a los datos de un archivo de excel, que muestra la longitud de las alas de diferentes mosquitos de la misma especie,
    se demostrara que sigue una distribucion normal. '''

    df = pd.read_excel('data.xls') # lea el archivo de excel
    print(df)
    print('*'*60)
    arr= df['Normally Distributed Housefly Wing Lengths'] #del dataframe lea solo esta columna = df['nombre que esta en la casila 1:1 del excel']
    print(arr)  
    print('*'*60) 
 
    arr2=df['Normally Distributed Housefly Wing Lengths'].values[3:] #de esta columna solo tome los valores ue van de la fila 3 en adelante (es decir los valores de las longitudes de las alas.)
    print(arr2)
    print('*'*60)
    
    values, dist = np.unique(arr2, return_counts=True) # generamos el conteo de las veces que se repitieron nuestros valores, esto no genera dos vectores [value, dist]
    plt.bar(values, dist) #generamos el grafico de barras
    plt.show()

    #estimando la distribucion
    mu=arr2.mean()
    sigma=arr2.std()
    dist=norm(mu,sigma)
    x = np.arange(30,60,0.1)
    y = [dist.pdf(value)for value in x]
    plt.plot(x,y)
    values, dist = np.unique(arr2, return_counts=True)
    plt.bar(values, dist/len(arr2)) # normailizmos el grafico
    plt.show()