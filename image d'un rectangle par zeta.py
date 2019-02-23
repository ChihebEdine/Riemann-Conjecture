from mpmath import*
import matplotlib.pyplot as plt

def rectangle(a,b,c,d,p1,p2):
    points=[(1-k1/p1)*((1-k2/p2)*a+(k2/p2)*d)+(k1/p1)*((1-k2/p2)*b+(k2/p2)*c)for k1 in range(p1+1) for k2 in range(p2+1)]
    return(points)

def zetaset(r):
    X=[float(re(zeta(z))) for z in r]
    Y=[float(im(zeta(z))) for z in r]
    plt.scatter(X,Y,color='r')


    
r=rectangle(0.6-10*j,0.9-10*j,0.9+10*j,0.6+10*j,100,100)
X=[float(re(z)) for z in r]
Y=[float(im(z)) for z in r]
plt.scatter(X,Y)
plt.grid()
zetaset(r)
plt.show()
