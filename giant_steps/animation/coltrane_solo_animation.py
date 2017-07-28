# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 10:30:08 2017

@author: budd
"""

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from solo_coords import *

img = plt.imread("melody_keyboard.png")
fig, ax = plt.subplots()
ax.imshow(img)

p=plt.plot(0,0,'o',color='yellow',ms=15.)[0]
plt.axis('off')
f=int(solo_cumulative[-1]/.12)

def update(n):         
    t=(n%f)*.12 
    def i_index(t):    
        for i in range(len(solo_cumulative)):
            if solo_cumulative[i] > t:
                return i
        else:
            return 0
    i=i_index(t) 
    print(i)       
    xi=solo_notes[i][0]    
    yi=solo_notes[i][1]
    p.set_xdata(xi)
    p.set_ydata(yi)

print(f)

anim = FuncAnimation(fig, update, frames=range(f),interval=120)
anim.save('coltrane_solo.gif', dpi=100, writer='imagemagick')
    
#plt.show()
