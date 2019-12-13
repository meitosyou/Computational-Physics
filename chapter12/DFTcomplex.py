# DFTcomplex.py:  Discrete Fourier Transform with built in complex
#from visual import *
#from visual.graph import *
import cmath     # complex math
from numpy import *
import matplotlib.pyplot as plt

"""                                
signgr = gdisplay(x=0, y=0, width=600, height=250, title ='Signal',\
             xtitle='x', ytitle = 'signal', xmax = 2.*math.pi, xmin = 0,\
	    ymax = 30, ymin = 0)
sigfig = gcurve(color=color.yellow, display=signgr)
imagr = gdisplay(x=0,y=250,width=600,height=250,title ='Imag Fourier TF',
       xtitle = 'x',ytitle='TF.Imag',xmax=10.,xmin=-1,ymax=100,ymin=-0.2)
impart = gvbars(delta = 0.05, color = color.red, display = imagr) 
"""


N = 200
Np = N                           
signal = zeros( (N+1), float )     
twopi  = 2.0*pi
sq2pi = 1.0/sqrt(twopi)
h = twopi/N
dftz   = zeros( (Np), complex )                  # Complex elements

x1list = []
x2list = []# x座標
y1list = []  # y座標
y2list = []

def f(signal):                                                  # Signal
    step = twopi/N
    x = 0.0 
    for i in range(0, N+1):
       signal[i] = 30*cos(80*x)
       #sigfig.plot(pos = (x, signal[i]))# Plot
       x1list.append(x)
       y1list.append(signal[i])
       x += step
      
def fourier(dftz):                                              # DFT
    for n in range(0, Np):              
      zsum = complex(0.0, 0.0)                
      for  k in range(0, N):                              
          zexpo = complex(0, twopi*k*n/N)           # Complex exponent #別の関数を動かすことによって得られたsignal[]を使う
          zsum += signal[k]*exp(-zexpo)           
      dftz[n] = zsum * sq2pi                                      
      if dftz[n].imag != 0:                   
          #impart.plot(pos = (n, dftz[n].imag) )# Plot
          x2list.append(n)
          y2list.append(dftz[n].imag)
          m = 0



f(signal)
fourier(dftz)# Call signal, transform

fig1 = plt.figure()
plt.title('Signal')
plt.xlabel('x')
plt.ylabel('signal')
plt.plot(x1list,y1list,marker='o',color = 'yellow')

fig2 = plt.figure()
plt.title('lmag Fourier TF')
plt.xlabel('x')
plt.ylabel('TF.lmag')
plt.plot(x2list,y2list,marker='o',color = 'blue')

plt.show()
