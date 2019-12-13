from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from numpy import *

xmax=201
ymax=100
zmax=100
x1list = []
y1list = []
z1list = []
x2list = []
y2list = []
z2list = []
ts = 2                          # time switch
beta = 0.01*10
Ex = zeros((xmax,ts),float)# init E 
Hy = zeros((xmax,ts),float)# init H
ti=0
time = 0

def inifields():
    i = arange(xmax)
    Ex[:xmax,0] = 0.1*sin(2*pi*i/100.0)
    Hy[:xmax,0] = 0.1*sin(2*pi*i/100.0)


def animate(time):
    if time !=0:
        plt.cla()
    
    x1list.clear()
    y1list.clear()
    x2list.clear()
    y2list.clear()
    z1list.clear()
    z2list.clear()
    Ex[1:xmax-1,1] = Ex[1:xmax-1,0] + beta*(Hy[0:xmax-2,0]-Hy[2:xmax,0])
    Hy[1:xmax-1,1] = Hy[1:xmax-1,0] + beta*(Ex[0:xmax-2,0]-Ex[2:xmax,0])
    Ex[0,1]        = Ex[0,0]        + beta*(Hy[xmax-2,0]  -Hy[1,0]) # BC
    Ex[xmax-1,1]   = Ex[xmax-1,0]   + beta*(Hy[xmax-2,0]  -Hy[1,0])  
    Hy[0,1]        = Hy[0,0]        + beta*(Ex[xmax-2,0]  -Ex[1,0]) # BC
    Hy[xmax-1,1]   = Hy[xmax-1,0]   + beta*(Ex[xmax-2,0] - Ex[1,0]) 

    for i in range(1,xmax):
        x1list.append(2*i - xmax)
        y1list.append(Ex[i,ti+1])
        z1list.append(0)
        x2list.append(2*i - xmax)
        y2list.append(0)
        z2list.append(Hy[i,ti+1])

    ax.plot(x1list,y1list,z1list,"-",c="r")
    ax.plot(x2list,y2list,z2list,"-",c="b")
    Ex[:xmax,0] = Ex[:xmax,1]                            # New->old
    Hy[:xmax,0] = Hy[:xmax,1]
    #print(time)
    time +=1

fig = plt.figure()
inifields()
ax = fig.add_subplot(111, projection='3d')
ani = animation.FuncAnimation(fig,animate,interval=100)
plt.show()

 
