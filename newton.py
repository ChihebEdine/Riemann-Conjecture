from mpmath import*

def derive(f,x0,h):
    return((f(x0+h)-f(x0))/h)

def newton(f,x0):
    h=0.000000000000001
    h1=0.000000000000001
    x=x0
    while abs(f(x))>h1:
        x=x-f(x)/derive(f,x,h)
    return(float(x))

a=0.5

f1=lambda x:float(re(zeta(a+j*x)))
f2=lambda x:float(im(zeta(a+j*x)))
