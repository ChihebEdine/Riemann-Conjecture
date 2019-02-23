from mpmath import*
import matplotlib.pyplot as plt



def disc(a,R,p1,p2):
    #p1 nombre de cercles
    #p2 nombre de points par cercle 
    points=[a+(k1*R/p1)*(float(cos(2*k2*pi/p2))+j*float(sin(2*k2*pi/p2))) for k1 in range(p1+1) for k2 in range(p2+1)]
    return(points)


D=disc(3+j,1,50,100)

X0=[re(z) for z in D]
Y0=[im(z) for z in D]

X1=[re(zeta(z)) for z in D]
Y1=[im(zeta(z)) for z in D]

plt.grid()
plt.scatter(X0,Y0)
plt.scatter(X1,Y1,color='r')
plt.show()

