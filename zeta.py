from mpmath import*
import scipy.integrate as integrate


def zeta1(z,n):
    s=1
    for i in range(2,n+1):
        s+=exp(-z*ln(i))
    return(complex(s))

def dériv_zeta1(z,h):
    d=complex((zeta(z+h)-zeta(z-h))/(2*h))
    return(d)

def dériv_zeta2(z,n):
    s=0
    for i in range(2,n+1):
        s+=-ln(i)*exp(-z*ln(i))
    return(complex(s))
