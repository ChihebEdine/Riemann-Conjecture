from mpmath import*
import matplotlib.pyplot as plt
import numpy as np

X=np.linspace(-20,20,20000)
Y=[float(zeta(x)) for x in list(X) if x!=1]

plt.plot(X,Y)
plt.grid()
plt.show()

