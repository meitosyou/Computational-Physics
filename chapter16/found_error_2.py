from numpy import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

Nx =101
T = np.zeros((Nx,2),float)
k = range(0,Nx)
fig = plt.figure()
xlist = []
ylist = []

def init():
    for j in range(0,50):       
        for i in range(0,50):
            xx = i+j
            yy = i-j
            xlist.append(xx)
            ylist.append(yy)

init()

ax =fig.add_subplot(111, autoscale_on = False, xlim=(-5,500),ylim=(-5,200.0))
ax.grid()
plt.ylabel("Temperature")
plt.title("Cooling of a bar")
line, = ax.plot(xlist, ylist, "o", lw =2)
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
p =1
k = 0
def animate(k):
    xlist.clear()
    ylist.clear()
   
    for ix in range(1, Nx-1):
        for j in range(1, Nx-1):
            k +=1
            xlist.append(ix +k)
            ylist.append(j)
 
    line.set_data(xlist,ylist)
    return None
    
ani = animation.FuncAnimation(fig,animate,interval=100)
plt.show()
#limitation をつけないと見えない。！！
#animateに変数をつけるとエラーが発生する。
