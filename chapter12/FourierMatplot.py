import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from pylab import *

M = 4                                 
T = 2.0                                                   # Period 

numwaves =  2
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.15, bottom=0.25)         # L & B margins
t = np.arange(0.0, pi, 0.01)               
t1 = np.arange(0.0,T/2,0.01)               
t2 = t[100:300]                               
f1 = t1                                 
f2 = t2-T                                  
s = 0 
plot(t1,f1)                                 
plot(t2,f2,color='b')     #直線二つ      

def Four(M,T,t):         # M = number waves, T = period, t = time
    sumy = 0                                            
    om = 2.0*pi/T                                    # Omega = 2pi/T
    fac = 1                                     
    for m in range(1,M):         # M variable selected with slider
        sumy += fac* sin(m*om*t)                      
        fac = -fac                                 #why?? 矩形波が確かこの形だった
    sumy = (2.0/pi)*sumy                           # Common factor何がπ/2?
    return sumy

s = Four(M,T,t)                                    # Initial plot   
l, = plt.plot(t,s, lw=1, color='red')    #lの後の点がｌを点の集団として格納するという機能を持つ
plt.axis([0, pi, -4.0, 4.0])             # minx, maxx, miny, maxy

xlabel('Time')                                        
ylabel('Signal')                                      
title('Fourier Synthesis of Sawtooth function')
grid(True)               

# Slider
axcolor = 'y'                           
axnumwaves = plt.axes([0.15, 0.1, 0.75, 0.03])   #, axisbg=axcolor) 
snumwaves = Slider(axnumwaves, '# Waves', 1, 20, valinit=T)
# Previous: value of the slider (float) assigned to snumwaves

def hzfunc():     
    hzdict = Four(int(numwaves),T,t)
    ydata = hzdict
    l.set_ydata(ydata)  # add data to l, 
    plt.draw()

hzfunc()

def update(val):                                # Update slider
    global  numwaves                         
    numwaves =int( snumwaves.val)                 
    l.set_ydata(Four(numwaves,T,t))             # Change nwaves
    fig.canvas.draw_idle()

snumwaves.on_changed(update)

plt.show()
