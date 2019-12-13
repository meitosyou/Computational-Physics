#from visual import *
#from visual.graph import *

from numpy import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

v0 = 22.0
angle = 34.0
g = 9.8
kf = 0.8
N = 5
v0x = v0*cos(angle*pi/180.0)
v0y = v0*sin(angle*pi/180.0)
T = 2.*v0y/g
H = v0y*v0y/2./g
R = 2.*v0x*v0y/g



"""
graph1 = gdisplay( title='Projectile with & without Drag',
          xtitle='x', ytitle='y', xmax=R, xmin=-R/20.,ymax=8,ymin=-6.0)
funct = gcurve(color=color.red)
funct1 = gcurve(color=color.yellow)
"""
print('No Drag T =',T,', H =',H,', R =',R)

#
x1list = []
x2list = []# x座標
y1list = []  # y座標
y2list = []


def plotNumeric(k):
     vx = v0*cos(angle*pi/180.0)
     vy = v0*sin(angle*pi/180.0)
     x = 0.0
     y = 0.0
     dt = vy/g/N/2
     print("\n       With Friction  ")
     print("       x            y")
     for i in range(N):
         
          #rate(30)
         time.sleep(3e-3)
         vx = vx - k*vx*dt
         vy = vy - g*dt - k*vy*dt
         x = x + vx*dt
         y = y + vy*dt
         #funct.plot(pos=(x,y))
         x1list.append(x)
         y1list.append(y)
         print(" %13.10f  %13.10f "%(x,y))
   

		
def plotAnalytic():
    v0x = v0*cos(angle*pi/180.0)
    v0y = v0*sin(angle*pi/180.0)
    dt =  v0y/g/N/2
    print("\n       No Friction  ")
    print("        x            y")
    for i in range(N):
        #rate(30)
        time.sleep(3e-2)
        t = i*dt
        x = v0x*t
        y = v0y*t -g*t*t/2.
        #funct1.plot(pos=(x,y))
        x2list.append(x)
        y2list.append(y)
        print(" %13.10f  %13.10f"%(x ,y))

fig1 = plt.figure()
plt.title('Projectile with & without Drag')
plt.xlabel('x')
plt.ylabel('y')

plotNumeric(kf)
plotAnalytic()

plt.plot(x1list,y1list,marker='o',color = 'yellow')
plt.plot(x2list,y2list,marker='o',color = 'blue')
plt.show()
