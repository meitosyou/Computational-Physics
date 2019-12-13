from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as anm
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
#ax = fig.gca(projection='3d')
ax = fig.add_subplot(111, projection='3d')

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
        ax.axis("off")
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





ani = anm.FuncAnimation(fig, update, interval = 15, frames = 10000)


plt.show()
