import matplotlib.pyplot as pl
import numpy as np
from fractions import Fraction

N = 19
x = []
y = []
for n in range(N):
    a = 2*np.pi*(1/4-n/N)
    x.append(np.cos(a))
    y.append(np.sin(a))
x = 1.1*np.array(x)
y = 1.1*np.array(y)
pl.plot(x,y,'o',color='black',markersize=10)

r = []
def just(r,h,col):
    for p in h:
        for q in h:
            if p >= q:
                f = Fraction(p,q)
                while f < 1:
                    f *= 2
                while f > 2:
                    f /= 2
                if f not in r:
                    r.append(f)
                    lf = float(f)   
                    lf = np.log(lf)/np.log(2)
                    print(f,lf)
                    a = 2*np.pi*(1/4-lf)
                    x = np.cos(a)
                    y = np.sin(a)
                    pl.plot(x,y,'o',color=col,markersize=10,
                            markeredgewidth=0) 

just(r,[1,3],'cyan')
just(r,[1,3,5],'blue')
just(r,[1,3,5,7],'magenta')
just(r,[1,3,5,7,9],'red')


pl.gca().set_aspect('equal')
pl.show()

