import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from melody_coords import *

img = plt.imread("melody_keyboard.png")
fig, ax = plt.subplots()
ax.imshow(img)

p=plt.plot(0,0,'o',color='cyan',ms=15.)[0]
plt.axis('off')
f=int(melody_cumulative[-1]/.12)

def update(n):         
    t=(n%f)*.12 
    def i_index(t):    
        for i in range(len(melody_cumulative)):
            if melody_cumulative[i] > t:
                return i
        else:
            return 0
    i=i_index(t) 
    print(i)       
    xi=melody_notes[i][0]    
    yi=melody_notes[i][1]
    p.set_xdata(xi)
    p.set_ydata(yi)

print(f)

anim = FuncAnimation(fig, update, frames=range(f),interval=120)
anim.save('gs_melody.gif', dpi=100, writer='imagemagick')
    
#plt.show()
