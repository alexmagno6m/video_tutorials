import matplotlib
#matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt
#from pylab import *
import numpy as np
import time

n = 300
t= np.zeros((n,n))
t[0, 0:n] = 100
#t[1:n, n-1] =50
t1 = time.time()
for k in range(1, 1000):
    for j in range(1,n-1):
        for i in range(1, n-1):
            t[i, j]=(t[i+1, j]+ t[i-1, j] +t[i, j+1] + t[i, j-1])/4


t2 = time.time()
print(t2-t1)
#como es necesario cambiar el orden de las filas donde la ultima pase a ser
#la primera se usa el siguiente comando
T =np.flipud(t)


plt.pcolormesh(T)
plt.show()

