import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from bass_coords import *

img = plt.imread("melody_keyboard.png")
fig, ax = plt.subplots()
ax.imshow(img)

p=plt.plot(0,0,'star',color='blue',ms=15.)[0]
plt.axis('off')
f=int(bass_cumulative[-1]/.12)

def update(n):         
    t=(n%f)*.12 
    def i_index(t):    
        for i in range(len(bass_cumulative)):
            if bass_cumulative[i] > t:
                return i
        else:
            return 0
    i=i_index(t) 
    print(i)       
    xi=bass_notes[i][0]    
    yi=bass_notes[i][1]
    p.set_xdata(xi)
    p.set_ydata(yi)

print(f)

anim = FuncAnimation(fig, update, frames=range(f),interval=120)
anim.save('gs_bass.gif', dpi=100, writer='imagemagick')
    
#plt.show()
