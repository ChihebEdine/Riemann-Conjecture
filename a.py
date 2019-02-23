from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
from mpmath import*


fig = plt.figure()
ax = fig.gca(projection='3d')


X = np.linspace(0.1,0.9, 100)
Y = np.linspace(0, 50, 100)
Yf, Xf = np.meshgrid(Y,X)

Z=np.ravel([float(im(zeta(x+j*y))) for x in X for y in Y])
Zf=Z.reshape(Xf.shape)
Z2=[0 for x in X for y in Y]
Zf2=np.ravel(Z2).reshape(Xf.shape)


#ax.plot_surface(Xf, Yf, Zf)#plot avec frame
ax.plot_wireframe(Xf, Yf, Zf, rstride=1, cstride=1)
#ax.plot_surface(Xf, Yf, Zf2,color='r')#plot surface 



plt.show()
