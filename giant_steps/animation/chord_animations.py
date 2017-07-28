import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from chord_coords import *

img = plt.imread("melody_keyboard.png")
fig, ax = plt.subplots()
ax.imshow(img)

p=plt.plot(0,0,'o',color='red',ms=15.)[0]
plt.axis('off')
f=int(chord_cumulative[-1]/.12)

def update(n):         
    t=(n%f)*.12 
    def i_index(t):    
        for i in range(len(chord_cumulative)):
            if chord_cumulative[i] > t:
                return i
        else:
            return 0
    i=i_index(t) 
    print(i)       
    x=[]
    y=[]    
    for j in range(len(chord_list[i])):    
        xi=chord_list[i][j][0]    
        yi=chord_list[i][j][1]
        x.append(xi)
        y.append(yi)
    p.set_xdata(x)
    p.set_ydata(y)

print(f)

anim = FuncAnimation(fig, update, frames=range(f),interval=120)
anim.save('gs_chords.gif', dpi=100, writer='imagemagick')
    
#plt.show()
