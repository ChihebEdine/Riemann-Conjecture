from mpmath import*
import matplotlib.pyplot as plt
import numpy as np

#recherche graphique des zero
#2D
#image de la famille en 'a' des droites de la forme (a+it) t dans R

a=0.4
T=list(np.linspace(0,40,1000))
Y1=[float(re(zeta(a+j*x))) for x in T]
Y2=[float(im(zeta(a+j*x))) for x in T]

plt.plot(T,Y1)
plt.plot(T,Y2,color='r')
plt.grid()
plt.show()
