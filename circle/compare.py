import matplotlib.pyplot as pl
import numpy as np
from fractions import Fraction

pl.subplot(1,1,1,axisbg='black')

N = 12
n = list(range(N))
a = 2*np.pi * (1/4-np.array(n)/N)
x = 1.1*np.cos(a)
y = 1.1*np.sin(a)
pl.plot(x,y,'o',color='white',markersize=10)


a = []
t = 0
p = 12*np.log(3)/np.log(2) - 7;
for n in range(1,13):
    t += np.log(3)/np.log(2)
    if n<5 or n==12:
        t -= p/6
    elif n<8:
        t = t
    elif n<11:
        t -= p/12
    else:
        t += p/12
    a.append(t)
   
a = 2*np.pi * (1/4-np.array(a))
x = 1.2*np.cos(a)
y = 1.2*np.sin(a)
pl.plot(x,y,'o',color='white',markersize=10)


h = [1,3,5,7,9]
c = ['yellow','cyan','magenta','blue','red']
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
                pl.plot(x,y,'o',color=c[i],markersize=10) 


ax = pl.gca()
ax.set_aspect('equal')
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
pl.show()

