import numpy as np
from matplotlib import pyplot
from numpy.random import normal #generador aleatorio de numeros para impleentar una distribucion normal
from scipy.stats import norm
from numpy import hstack
from sklearn.neighbors import KernelDensity

if __name__=='__main__':

    sample = normal(size=100000) #generador aleatorio basado en la distribucion normal (datos artificiales)
    pyplot.hist(sample, bins=80) #histograma con 30 intervalos para generar la grafica de barras
    print(sample)
    print(len(sample))
    pyplot.show()
    
      
    '''
    Estimacion parametrica:
    '''
    sample = normal(loc=50,scale=5, size=1000) # mu = 50, sigma = 5 (desviacion estandar) 
    mu = sample.mean()
    sigma=sample.std()
    
    dist = norm(mu, sigma)
    x=[ value for value in range(30,70)] #valores
    y = [dist.pdf(value) for value in x] #probabilidades: generamos nuestra funcion de densidad de probbiliad
    
    pyplot.hist(sample, bins=80, density=True) #histograma con barras normailizado (density=true)
    pyplot.plot(x, y)#(valores, probabilidades)
    pyplot.show()

    #construimos una distribución bimodal
    sample1 = normal(loc=20, scale=5, size=300)
    sample2 = normal(loc=40, scale=5, size=700)
    sample = hstack((sample1, sample2))

    model = KernelDensity(bandwidth=2, kernel='gaussian')
    sample = sample.reshape((len(sample), 1))
    model.fit(sample)

    values = np.asarray([value for value in range(1, 60)])
    values = values.reshape((len(values), 1))
    probabilities = model.score_samples(values) #probabilidad logarítmica
    probabilities = np.exp(probabilities)  # inversión de probabilidad

    pyplot.hist(sample, bins=50, density=True) 
    pyplot.plot(values[:], probabilities)
    pyplot.show()
