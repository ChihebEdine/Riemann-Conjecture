from mpmath import *
import matplotlib.pyplot as plt


def zeta_seg(a,b,p):
    #trace l'image d'un segment[a,b] en le décomposant avec un pas p
    points=[(k/p)*a+(1-k/p)*b for k in range(p+1)]
    X1=[float(re(z)) for z in points]
    Y1=[float(im(z)) for z in points]
    X=[float(re(zeta(z))) for z in points]
    Y=[float(im(zeta(z))) for z in points]
    plt.grid()
    plt.plot(X1,Y1,color='blue')
    plt.plot(X,Y,color='red')
    plt.show()

##a=0.5
##
##f = lambda t: re(zeta(a+j*t))
##g = lambda t: im(zeta(a+j*t))
##
##X1=[float(f(0.1*t)) for t in range(101)]
##Y1=[float(g(0.1*t)) for t in range(101)]
##
##X2=[float(f(0.1*t)) for t in range(100,201)]
##Y2=[float(g(0.1*t)) for t in range(100,201)]
##
##X3=[float(f(0.1*t)) for t in range(200,301)]
##Y3=[float(g(0.1*t)) for t in range(200,301)]
##
##X4=[float(f(0.1*t)) for t in range(300,401)]
##Y4=[float(g(0.1*t)) for t in range(300,401)]
##
##X5=[float(f(0.1*t)) for t in range(400,500)]
##Y5=[float(g(0.1*t)) for t in range(400,500)]
##
##plt.plot(X1,Y1,color='red')
##plt.plot(X2,Y2,color='blue')
##plt.plot(X3,Y3,color='green')
##plt.plot(X4,Y4,color='black')
##plt.plot(X5,Y5,color='brown')
##
##plt.xlabel( 'partie réele' )
##plt.ylabel( 'partie imaginaire' )
##
##plt.title( 'image d une droite ' )
##plt.grid()
##plt.show()



