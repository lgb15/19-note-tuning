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


h = [1,3,5,7,9]
c = ['yellow','cyan','blue','magenta','red']
r = []

for i,p in enumerate(h):
    for q in h:
        if p >= q:
            f = Fraction(p,q)
            if f not in r:
                r.append(f)
                lf = float(f)   
                lf = np.log(lf)/np.log(2)
                print(f)
                a = 2*np.pi*(1/4-lf)
                x = np.cos(a)
                y = np.sin(a)
                pl.plot(x,y,'o',color=c[i],markersize=10,
                        markeredgewidth=0) 

pl.gca().set_aspect('equal')
pl.show()

