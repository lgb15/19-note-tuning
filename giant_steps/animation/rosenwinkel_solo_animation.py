# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 10:57:51 2017

@author: budd
"""

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from rsolo_coords import *

img = plt.imread("melody_keyboard.png")
fig, ax = plt.subplots()
ax.imshow(img)

p=plt.plot(0,0,'o',color='red',ms=10.)[0]
plt.axis('off')
f=int(rsolo_cumulative[-1]/.12)

def update(n):         
    t=(n%f)*.12 
    def i_index(t):    
        for i in range(len(rsolo_cumulative)):
            if rsolo_cumulative[i] > t:
                return i
        else:
            return 0
    i=i_index(t) 
    print(i)       
    xi=rsolo_notes[i][0]    
    yi=rsolo_notes[i][1]
    p.set_xdata(xi)
    p.set_ydata(yi)

print(f)

anim = FuncAnimation(fig, update, frames=range(f),interval=120)
#anim.save('rsolo.gif', dpi=100, writer='imagemagick')
    
plt.show()
