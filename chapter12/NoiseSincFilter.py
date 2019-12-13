# NoiseSincFilter.py
#from visual import *
#from visual.graph import *
import random
from numpy import *
import matplotlib.pyplot as plt

max = 4000
array = zeros((max),float)
ps = zeros((max),float)
step = 2*math.pi/1000

x1list = []
x2list = []# x座標
y1list = []  # y座標
y2list = []
x3list = []
y3list = []


"""
graph1 = gdisplay(x=0,y=0,width=600,height=250, title='Pure Signal',
              xtitle='t (s)',ytitle='f(t)',xmin=0,xmax=25,ymin=0,ymax=10)
funct1 = gcurve(color=color.red)
graph2 = gdisplay(x=0,y=250,width=600,height=250, title='Signal + Noise',
              xtitle='t (s)',ytitle='y(t)',xmin=0,xmax=25,ymin=0,ymax=10)
funct2 = gcurve(color=color.red)
graph3 = gdisplay(x=0,y=500,width=600,height=250, title='Filtered Input',
              xtitle='t (s)',ytitle='y(t)',xmin=0,xmax=25,ymin=0,ymax=10)
funct3 = gcurve(color=color.red)
"""



def function(array,max):
    f = zeros((max + 1),float) 
    step = 2*pi/1000
    x = 0.0 
    for i in range(0,max):
        f[i] = 1/(1.0 - 0.9*sin(x))                             # Function
        array[i] = (1/(1-0.9*sin(x)))+0.5*(2.0*random.random()-1)  # Noise
        #funct1.plot(pos=(x,f[i]))
        #funct2.plot(pos=(x,array[i]))
        x1list.append(x)
        y1list.append(f[i])
        x2list.append(x)
        y2list.append(array[i])
        x += step
				
def filter():                           # Low-pass windowed sinc filter
    y = zeros((max),float)
    h = zeros((max),float)
    step = 2*pi/1000
    m = 100                                          # Set filter length
    fc = 0.07   
    for i in range(0,100):                             # Low-pass filter
        if ((i-(m/2)) == 0):
            h[i] = 2*pi*fc 
        if ((i-(m/2))!= 0):
            h[i] = sin(2*pi*fc*(i-m/2))/(i-m/2)
        h[i] = h[i]*(0.54 - 0.46*cos(2*pi*i/m))         # Hamming window
    sum = 0.0                                 # Normalize low-pass filter
    for i in range(0,100):
        sum = sum + h[i]
    for i in range(0,100):
        h[i] = h[i] / sum 
    for j in range(100,max-1):               # Convolute input + filter
        y[j] = 0.0                    
        for i in range(0,100):
            y[j] = y[j] + array[j-i] * h[i]
    for j in range(0,max-1):
        #funct3.plot(pos=(j*step,y[j]))
        x3list.append(j*step)
        y3list.append(y[j])

function(array, max)                                       
filter()                                                     

fig1 = plt.figure()
plt.title('Pure Signal')
plt.xlabel('t(s)')
plt.ylabel('f(t)')
plt.plot(x1list,y1list,marker='o',color = 'red')

fig2 = plt.figure()
plt.title('Signal + Noise')
plt.xlabel('t(s)')
plt.ylabel('y(t)')
plt.plot(x2list,y2list,marker='o',color = 'blue')

fig3 = plt.figure()
plt.title('Filtered input')
plt.xlabel('t(s)')
plt.ylabel('y(t)')
plt.plot(x3list,y3list,marker='o',color = 'yellow')

plt.show()
