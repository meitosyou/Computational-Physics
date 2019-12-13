from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import matplotlib.pyplot as plt
#import numpy as np
from numpy import *


"""
f=np.pi/6
d=np.pi/2
t=[]

def update(i):
        if i !=0:
             plt.cla()

        X1=0
        Y1=0
        Z1=0
        U1=-np.cos(i/10)*np.sin(f)*np.cos(f)
        V1=np.cos(i/10)*np.sin(f)*np.sin(f)
        W1=0

        X2=0
        Y2=0
        Z2=0
        U2=np.cos(i/10)*np.sin(f)*np.cos(f)
        V2=np.cos(i/10)*np.cos(f)*np.cos(f)
        W2=0

        X3=0
        Y3=0
        Z3=0
        U3=U1+U2
        V3=V1+V2
        W3=0

        X4=[X1,U1]
        Y4=[Y1,V1]
        Z4=[Z1,W1]
        X5=[X2,U2]
        Y5=[Y2,V2]
        Z5=[Z2,W2]
        X6=[X3,U3]
        Y6=[Y3,V3]
        Z6=[Z3,W3]

        ax.set_xlim(-1.5,1.5)
        ax.set_ylim(-1.5,1.5)
        ax.set_zlim(0,3)
        #ax.axis("off")
        ax.plot(X4,Y4,Z4,"-",c="r",lw=2)
        ax.plot(X5,Y5,Z5,"-",c="b",lw=2)
        ax.plot(X6,Y6,Z6,"-",c="m",lw=2)

        t.append(i)
        t1=np.array(t)

        x1=-np.cos((i-t1)/10)*np.sin(f)*np.cos(f)
        y1=np.cos((i-t1)/10)*np.sin(f)*np.sin(f)
        z1=t1/100


        x2=np.cos((i-t1)/10)*np.sin(f)*np.cos(f)
        y2=np.cos((i-t1)/10)*np.cos(f)*np.cos(f)
        z2=t1/100

        x3=x1+x2
        y3=y1+y2
        z3=z1

        ax.plot(x1, y1, z1,"-", c="r")
        ax.plot(x2, y2, z2,"-", c="b")
        ax.plot(x3, y3, z3,"-", c="m")
"""
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
beta = 0.01
Ex = zeros((xmax,ts),float)# init E 
Hy = zeros((xmax,ts),float)# init H
ti=0
time = 0

def inifields():
    k = arange(xmax)
    Ex[:xmax,0] = 0.1*sin(2*pi*k/100.0)
    Hy[:xmax,0] = 0.1*sin(2*pi*k/100.0)


def animate(time):
    #if i !=0:
    #    plt.cla()
    #rate(600)
    x1list.clear()
    y1list.clear()
    x2list.clear()
    y2list.clear()
    
    Ex[1:xmax-1,1] = Ex[1:xmax-1,0] + beta*(Hy[0:xmax-2,0]-Hy[2:xmax,0])
    Hy[1:xmax-1,1] = Hy[1:xmax-1,0] + beta*(Ex[0:xmax-2,0]-Ex[2:xmax,0])
    Ex[0,1]        = Ex[0,0]        + beta*(Hy[xmax-2,0]  -Hy[1,0]) # BC
    Ex[xmax-1,1]   = Ex[xmax-1,0]   + beta*(Hy[xmax-2,0]  -Hy[1,0])  
    Hy[0,1]        = Hy[0,0]        + beta*(Ex[xmax-2,0]  -Ex[1,0]) # BC
    Hy[xmax-1,1]   = Hy[xmax-1,0]   + beta*(Ex[xmax-2,0] - Ex[1,0]) 
    #plotfields(ti)
   
   
    
    for i in range(1,xmax):
        x1list.append(2*i - xmax)
        y1list.append(Ex[i,ti])
        z1list.append(0)
        x2list.append(2*i - xmax)
        y2list.append(0)
        z2list.append(Hy[i,ti])

    ax.plot(x1list,y1list,z1list,c="r")
    ax.plot(x2list,y2list,z2list,c="b")
    """
    x1=-np.cos((i-t1)/10)*np.sin(f)*np.cos(f)
    y1=np.cos((i-t1)/10)*np.sin(f)*np.sin(f)
    z1=t1/100
    x2=np.cos((i-t1)/10)*np.sin(f)*np.cos(f)
    y2=np.cos((i-t1)/10)*np.cos(f)*np.cos(f)
    """
    
    #E.set_data(x1list,y1list,zlist)
    #H.set_data(x2list,y2list,zlist)
    Ex[:xmax,0] = Ex[:xmax,1]                            # New->old
    Hy[:xmax,0] = Hy[:xmax,1]
    time +=1
    

fig = plt.figure()
inifields()
##ax = fig.gca(projection='3d')
ax = fig.add_subplot(111, projection='3d')
#E, = ax.plot(x1list,y1list,zlist,"-")
#H, = ax.plot(x2list,y2list,zlist,"-")
ani = animation.FuncAnimation(fig,animate,interval=100)
plt.show()
