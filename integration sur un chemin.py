import numpy as np
import matplotlib.pyplot as plt
from time import clock

from mpmath import*
import scipy.integrate as si

#segment [a,b]
s=lambda a,b,t:complex(t*b+(1-t)*a)

#calcule l integrale d une fonction à variable complexe suivant un segment [a,b]
def integrale_seg(f,a,b):
    g=lambda t:f(s(a,b,t))*(b-a)
    g1=lambda t:re(g(t))
    g2=lambda t:im(g(t))
    I1=si.quad(g1,0,1)[0]
    I2=si.quad(g2,0,1)[0]
    I=I1+j*I2
    return(complex(I))

#donne le nombre de zeros de zeta à l intérieur d'un polygône abcd
def nbrzero1(a,b,c,d):
    #a,b,c,d sommets
    g=lambda z:complex(((1/(2*j*pi))*((zeta(z,1,1))/(zeta(z)))))
    I1=integrale_seg(g,a,b)
    I2=integrale_seg(g,b,c)
    I3=integrale_seg(g,c,d)
    I4=integrale_seg(g,d,a)
    return((I1+I2+I3+I4).real)

def nbrzero2(h,d,e):
    a=0.5-e/2+j*h
    b=0.5+e/2+j*h
    c=0.5+e/2+j*(h+d)
    d=0.5-e/2+j*(h+d)
    return((complex(nbrzero1(a,b,c,d)).real))


#cercle de centre a de rayan r
c=lambda a,r,t:complex(a+r*complex(exp(j*t)))

#calcule l integrale d une fonction à variable complexe suivant un cercle
def integrale_cercle(f,a,r):
    g=lambda t:complex(f(c(a,r,t))*r*j*complex(exp(j*t)))
    g1=lambda t:re(g(t))
    g2=lambda t:im(g(t))
    I1=si.quad(g1,0,2*pi)[0]
    I2=si.quad(g2,0,2*pi)[0]
    I=I1+j*I2
    return(complex(I))






#trace les n premiers zeros de zeta et leur conjugué
def zetzer(n):
    Z=[zetazero(i) for i in range(1,n) if i!=0]
    Y=[im(t) for t in Z]
    X=[re(t) for t in Z]
    plt.grid()
    plt.xlabel('partie réele')
    plt.ylabel('partie imaginaire')
    plt.scatter(X,Y)


def dicotomie(h,d,e):
    n=round(nbrzero2(h,d,e))
    if n==1:
        return([(h,d,e)])
    elif n==0:
        return([])
    else:
        return(dicotomie(h,d/2,e)+dicotomie(h+d/2,d/2,e))


def tracechemin(h,d,e):
    a=0.5-e/2+j*h
    b=0.5+e/2+j*h
    c=0.5+e/2+j*(h+d)
    d=0.5-e/2+j*(h+d)
    X=[float(re(a)),float(re(b)),float(re(c)),float(re(d)),float(re(a))]
    Y=[float(im(a)),float(im(b)),float(im(c)),float(im(d)),float(im(a))]
    plt.grid()
    plt.plot(X,Y)

D=[(10,10,1),(20,5,1),(25,5,1)]
for i in D :
    tracechemin(i[0],i[1],i[2])
zetzer(5)
plt.show()

##print('dicotomie(10,20,1)=',D)
##print('dt=',t2-t1)

