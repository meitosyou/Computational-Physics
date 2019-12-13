""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""

# PredatorPrey.py:     Lotka-Volterra models

#from visual import *
#from visual.graph import *
import matplotlib.pyplot as plt
from numpy import *
Tmin = 0.0
Tmax = 500.0                                                   
y = zeros( (2), float)
Ntimes = 1000
y[0] = 2.0
y[1] = 1.3                                                    
h = (Tmax - Tmin)/Ntimes 
t = Tmin

tlist = []  # x座標
list = []
list = []  # y座標
y0list = []
y1list = []  # x座標
list = []

def f( t, y, F):              #  Modify this function for your problem
        F[0] = 0.2*y[0]*(1 - (y[0]/(20.0) )) - 0.1*y[0]*y[1]  
        F[1]  = - 0.1*y[1] + 0.1*y[0]*y[1];                   
		 
def rk4(t, y, h, Neqs):              # rk4 method,  DO NOT modify
    F = zeros((Neqs), float)
    ydumb = zeros((Neqs), float)
    k1    = zeros((Neqs), float)
    k2    = zeros((Neqs), float)
    k3    = zeros((Neqs), float)
    k4    = zeros((Neqs), float)
    f(t, y, F)
    for i in range(0, Neqs):
        k1[i] = h*F[i]
        ydumb[i] = y[i] + k1[i]/2.
    f(t + h/2., ydumb, F)
    for i in range(0, Neqs):
        k2[i] = h*F[i]
        ydumb[i] = y[i] + k2[i]/2.
    f(t + h/2., ydumb, F)
    for i in range(0, Neqs):
        k3[i] =  h*F[i]
        ydumb[i] = y[i] + k3[i]
    f(t + h, ydumb, F)
    for i in range(0, Neqs):
        k4[i] = h*F[i]
        y[i] = y[i] + (k1[i] + 2.*(k2[i] + k3[i]) + k4[i])/6.
"""				        
graph1 = gdisplay(x= 0,y= 0, width = 500, height = 400, \
      title = 'Prey p(green) and predator P(yellow) vs time',xtitle = 't', \
     ytitle = 'P, p',xmin=0,xmax=500,ymin=0,ymax=3.5)
funct1 = gcurve(color = color.yellow)
funct2 = gcurve(color = color.green)
graph2 = gdisplay(x= 0,y= 400, width = 500, height = 400,
                  title = 'Predator P vs prey p',
              xtitle = 'P', ytitle = 'p',xmin=0,xmax=2.5,ymin=0,ymax=3.5)
funct3 = gcurve(color = color.red)

for t in arange(Tmin, Tmax + 1, h):
    funct1.plot(pos = (t, y[0]) )
    funct2.plot(pos = (t, y[1]) )
    funct3.plot(pos = (y[0], y[1]) )
    rate(60)
    rk4(t, y, h, 2)
"""


for t in arange(Tmin, Tmax + 1, h):
    tlist.append(t)
    y0list.append(y[0])
    y1list.append(y[1])
    rk4(t, y, h, 2)


"""
ani1 = animation.ArtistAnimation(fig1,ims1,interval=100 ,repeat_delay = 60)
ani2 = animation.ArtistAnimation(fig1,ims2,interval=100 ,repeat_delay = 60)
ani2 = animation.ArtistAnimation(fig1,ims2,interval=100 ,repeat_delay = 60)
"""
fig1 = plt.figure(figsize=(5,4))
plt.title('Prey p(green) and predator P(yellow) vs time')
plt.xlabel('t')
plt.ylabel('P,p')
plt.plot(tlist, y0list,'yellow')
plt.plot(tlist, y1list,'green')

fig1 = plt.figure(figsize=(5,4))
plt.title('Predator P vs prey p')
plt.xlabel('P')
plt.ylabel('p')
plt.plot(y1list, y0list,'red')

plt.show()
    
