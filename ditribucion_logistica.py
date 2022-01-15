from mpl_toolkits.mplot3d import Axes3D  #gradico tridimencional
import matplotlib.pyplot as plt
from matplotlib import cm #acceder a diferentes paletas de colores
import numpy as np
import pandas as pd
import seaborn as sns

def likelihood(y,yp):
    return yp*y+(1-yp)*(1-y)

if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.gca(projection='3d') #permite genrear una caja de ejes de 3d
    y = np.arange(0, 1, 0.01) #valores de 0 a 1 de a pasos 0.01
    yp = np.arange(0, 1, 0.01)
    y, yp = np.meshgrid(y,yp) #generamos una cuadricula o malla 
    z = likelihood(y,yp) #generamos la verimilitud de los valores y and yp.

    surf = ax.plot_surface(y,yp,z,cmap=cm.coolwarm)
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.show() 



