import numpy as np
import matplotlib.pylot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import time
from numba import jit
from numba import cuda
from numba import *

#--------------------------------------------
# Número de celdas
n = np.array([512,512], dtype=np.int64)
#Tamaño del dominio (menor que uno)
L = np.array([1.0,1.0], dtype=np.float64)
# Constante de difusión
kd:float64 = 0.2
# Pasos de tiempo
paso:int = 1000
#--------------------------------------------

# Tamaño de las celdas
dx = L/n
udx2 = 1.0/(dx*dx)
# Paso de tiempo
dt = 0.25*(min(Dx[0],dx[1])**2)/kd
print("dt = ",dt)
# Total de celdas
nt = n[0]*n[1]
print("celdas = ",nt)

@jit
def evolucion(u,n_0,n_1,udx2_0,udx2_!,dt,kd.i):


