""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""

# CircPolarztn.py: solves Maxwell eqs. using FDTD 

#from visual import *                           
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from numpy import *

#scene = display(x=0, y=0, width=600, height=400,range=200, title='Circular polarization, E field in white, H field in yellow')
global phy, pyx
max = 201                                               
c = 0.01*10                      # Courant stable if c < 0.1

x1list = []
y1list = []
z1list = []
x2list = []
y2list = []
z2list = []

Ex = zeros((max+2,2),float)                         
Hy = zeros((max+2,2),float)     
Ey = zeros((max+2,2),float)                         
Hx = zeros((max+2,2),float)

"""
#arrowcol= color.white                                   
Earrows = []
Harrows = []
for i in range(0,max,10):       
    Earrows.append(arrow(pos=(0,i-100,0), axis=(0,0,0), color=arrowcol))
    Harrows.append(arrow(pos=(0,i-100,0), axis=(0,0,0), color=color.yellow))

def plotfields(Ex,Ey,Hx,Hy):
    for n, arr in enumerate(Earrows):
        arr.axis = (35*Ey[10*n,1],0,35*Ex[10*n,1])
    for n, arr in enumerate(Harrows):
        arr.axis = (35*Hy[10*n,1],0,35*Hx[10*n,1])
"""

def inifields():                                         # Initial E & H
    phx = 0.5*pi
    phy = 0.0
    k = arange(0,max)
    Ex[:-2,0] = cos(-2*pi*k/200 + phx)
    Ey[:-2,0] = cos(-2*pi*k/200 + phy)
    Hx[:-2,0] = cos(-2*pi*k/200 + phy + pi)
    Hy[:-2,0] = cos(-2*pi*k/200 + phx)

time = 0
def newfields(time):
    #while True:                                          # Time stepping
    #  rate(1000)
    if time !=0:
        plt.cla()
    
    x1list.clear()
    y1list.clear()
    x2list.clear()
    y2list.clear()
    z1list.clear()
    z2list.clear()
    
    Ex[1:max-1,1] =  Ex[1:max-1,0]+c*(Hy[:max-2,0]-Hy[2:max,0])  
    Ey[1:max-1,1] =  Ey[1:max-1,0] + c*(Hx[2:max,0]-Hx[:max-2,0])
    Hx[1:max-1,1] =  Hx[1:max-1,0] + c*(Ey[2:max,0]-Ey[:max-2,0]) 
    Hy[1:max-1,1] =  Hy[1:max-1,0] + c*(Ex[:max-2,0]-Ex[2:max,0])
    Ex[0,1]   = Ex[0,0]   + c*(Hy[200-1,0]-Hy[1,0])   # Periodic BC
    Ex[200,1] = Ex[200,0] + c*(Hy[200-1,0]-Hy[1,0])    
    Ey[0,1]   = Ey[0,0]   + c*(Hx[1,0]- Hx[200-1,0])   
    Ey[200,1] = Ey[200,0] + c*(Hx[1,0]- Hx[200-1,0])
    Hx[0,1]   = Hx[0,0]   + c*(Ey[1,0]- Ey[200-1,0])
    Hx[200,1] = Hx[200,0] + c*(Ey[1,0]- Ey[200-1,0])
    Hy[0,1]   = Hy[0,0]   + c*(Ex[200-1,0]-Ex[1,0])
    Hy[200,1] = Hy[200,0] + c*(Ex[200-1,0]-Ex[1,0])
    #plotfields(Ex,Ey,Hx,Hy)
    for i in range(1,max):
        x1list.append(2*i - max)
        y1list.append(Ex[i,1])
        z1list.append(0)
        x2list.append(2*i - max)
        y2list.append(0)
        z2list.append(Hy[i,1])

    ax.plot(x1list,y1list,z1list,"-",c="r")
    ax.plot(x2list,y2list,z2list,"-",c="b")
    
    Ex[:max,0] = Ex[:max,1]                        # Update fields
    Ey[:max,0] = Ey[:max,1]
    Hx[:max,0] = Hx[:max,1]
    Hy[:max,0] = Hy[:max,1]

    time +=1

fig = plt.figure()
inifields()                                           # Initial field
#newfields()                                        # Subsequent field
ax = fig.add_subplot(111, projection='3d')
ani = animation.FuncAnimation(fig,newfields,interval=100)
plt.show()
