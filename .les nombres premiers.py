import matplotlib.pyplot as plt
from math import log,sqrt

##from PIL import Image
import numpy as np
from scipy.integrate import quad

def premier(n):
    if n==1 or n==0:
        return(False)
    elif n==2:
        return(True)
    else:
        d=2
        while n%d!=0 and d<=n/2:
            d+=1
        return(d>n/2)

def premiern(n):
    L=[]
    for i in range(n):
        if premier(i):
            L.append(i)
    return(L)

def niemepremier(n):
    L=[]
    k=0
    while len(L)<n:
        if premier(k):
            L.append(k)
            k+=1
        else:
            k+=1
    return(L[n-1])

    

def somme(L):
    s=0
    for i in L:
        s+=i
    return(s)

def ecart(L):
    n=len(L)
    m=1/n*somme(L)
    L1=[(i-m)**2 for i in L]
    e=sqrt(1/n*somme(L1))
    return(e)
def flu(L):
    return(len(L)*ecart(L)/somme(L))

def bitmap(n):
    M=np.array([[(255,255,255)]*n]*n)
    for i in range(n):
        for j in range(n):
            if premier(j+i*n):
                M[i,j]=(0,0,0)
    return(M)

def pii(x):
    if x>=0:
        s=0
        n=int(x)
        for i in range(n+1):
            if premier(i):
                s+=1
        return(s)
            
    else:
        print(x,'doit etre positif')

def Li(x):
    g=lambda t:1/log(t)
    if x>=2:
        return(quad(g,2,x)[0])
    else:
        print('x>=2')

X=np.linspace(2,1000,5000)

Y=[-pii(x)+Li(x) for x in X]
Y1=[sqrt(x)*log(x) for x in X]


plt.plot(X,Y)
plt.plot(X,Y1)
plt.grid()
plt.show()

##n=100
##img=Image.fromarray(bitmap(n))
##img.save('bitmap '+str(n))
##img.show()

##n=10000
##X=premiern(n)
##print('ecart type= ',ecart(X))
##Y=[0]*len(X)

##plt.scatter(X,Y)
##plt.grid()
##plt.show()



        
