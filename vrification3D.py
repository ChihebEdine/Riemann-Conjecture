from mpmath import*
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

#trace Re(zeta(z)) et Im(zeta(z)) 
#pour z dans la partie a<Re(z)<b et c<Im(z)<d

a,b,c,d=0.1,0.9,20,40
fig = plt.figure()
ax = fig.gca(projection='3d')
X=np.linspace(a,b,10)
Y=np.linspace(c,d,10)
Xf=[x for x in X for y in Y]
Yf=[y for x in X for y in Y]
Z=[float(re(zeta(x+j*y))) for x in X for y in Y]
ax.plot(Xf,Yf,Z)
plt.show()
