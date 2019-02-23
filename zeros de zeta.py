from mpmath import*
import matplotlib.pyplot as plt
import numpy as np


def zetzer(n):
    #trace les n premiers zeros de zeta et leur conjugué
    Z=[zetazero(i) for i in range(-n,n) if i!=0]
    Y=[im(t) for t in Z]
    X=[re(t) for t in Z]
    X1=[1]*1000
    X2=[0]*1000
    Y1=list(np.linspace(-60,60,1000))
    plt.grid()
    plt.xlabel('partie réele')
    plt.ylabel('partie imaginaire')
    plt.scatter(X,Y)
    plt.plot(X1,Y1)
    plt.plot(X2,Y1)
    plt.show()

def zeta_seg_zero(n,p,ch):
    #trace l'image du segment entre 2 zero successives
    #p nombre de points a afficher
    #pas de plt.show() il faut l'ajouter chaque fois 
    a=float(im(zetazero(n)))
    b=float(im(zetazero(n+1)))
    X=[float(re(zeta(0.5+j*(a+t*(b-a)/p)))) for t in range(p+1)]
    Y=[float(im(zeta(0.5+j*(a+t*(b-a)/p)))) for t in range(p+1)]
    plt.grid()
    plt.plot(X,Y,color=ch)



