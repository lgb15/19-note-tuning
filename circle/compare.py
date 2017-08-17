import matplotlib.pyplot as pl
import numpy as np
from fractions import Fraction

pl.subplot(1,1,1,axisbg='black')

case = 1

if case == 0:
    N = 12
    n = list(range(N))
    a = 2*np.pi * (1/4-np.array(n)/N)
    X = 1.1*np.cos(a)
    Y = 1.1*np.sin(a)
    fig, = pl.plot(X,Y,'o',color='white',markersize=10)

if case == 1:
    N = 12
    a = []
    t = 0
    p = 12*np.log(1.5)/np.log(2) - 7;
    print(p)
    for n in range(1,13):
        t += np.log(1.5)/np.log(2)
        if t > 1:
            t -= 1
        if n<5 or n==12:
            t -= p/6
        elif n<8:
            t = t
        elif n<11:
            t -= p/12
        else:
            t += p/12
        a.append(t)
    a.sort()
    print(a)
    a = 2*np.pi * (1/4-np.array(a))
    X = 1.1*np.cos(a)
    Y = 1.1*np.sin(a)
    fig, = pl.plot(X,Y,'o',color='white',markersize=15)


h = [1,3,5,7,9]
c = ['yellow','cyan','magenta','blue','red']
s = [15,15,15,10,10]
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
                pl.plot(x,y,'o',color=c[i],markersize=s[i]) 


ax = pl.gca()
ax.set_aspect('equal')
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

for n in range(1000):
    k = n%N
    t = np.pi/2 - np.arctan2(Y[k],X[k])
    cs,sn = np.cos(t),np.sin(t)
    X,Y = cs*X - sn*Y, sn*X + cs*Y
    fig.set_xdata(X)
    fig.set_ydata(Y)
    print(k)
    pl.pause(0.5)

