# DFTreal.py:  Discrete Fourier Transform using real numbers

import cmath     # complex math
from numpy import *
import matplotlib.pyplot as plt
#from visual.graph import *



"""
signgr = gdisplay(x=0,y=0,width=600,height=250, \
        title='Signal y(t)= 3 cos(wt)+2 cos(3wt)+ cos(5wt) ',\
	xtitle='x', ytitle='signal',xmax=2.*math.pi,xmin=0,ymax=7,ymin=-7)
sigfig = gcurve(color=color.yellow,display=signgr)
imagr = gdisplay(x=0,y=250,width=600,height=250,\
	    title='Fourier transform imaginary part',xtitle='x',\
        ytitle='Transf.Imag',xmax=10.0,xmin=-1,ymax=20,ymin=-25)
impart = gvbars(delta=0.05,color=color.red,display=imagr)      
"""



N = 200                                   
Np = N 
signal = zeros((N+1),float)     
twopi = 2.*pi
sq2pi = 1./sqrt(twopi) 
h = twopi/N
dftimag = zeros((Np),float)# Im. transform



x1list = []
x2list = []# x座標
y1list = []  # y座標
y2list = []


def f(signal):                                          
    step = twopi/N
    t= 0. 
    for  i in range(0,N+1):
       signal[i] = 3*sin(t*t*t)  
       #sigfig.plot(pos=(t,signal[i]))
       x1list.append(x)
       y1list.append(signal[i])
       t += step
      
def fourier(dftimag):                                            # DFT
    for n in range(0,Np):                                 
      imag = 0.                                         
      for  k in range(0, N):                               
        imag += signal[k]*sin((twopi*k*n)/N) 
      dftimag[n] = -imag*sq2pi                           # Im transform
      if dftimag[n] !=0:                 
          #impart.plot(pos=(n,dftimag[n]))
          x2list.append(n)
          y2list.append(dftz[n].imag)

f(signal) 
fourier(dftimag)

fig1 = plt.figure()
plt.title('Signal')
plt.xlabel('x')
plt.ylabel('signal')
plt.plot(x1list,y1list,marker='o',color = 'yellow')

fig2 = plt.figure()
plt.title('FT imaginary part')
plt.xlabel('x')
plt.ylabel('TF.lmag')
plt.plot(x2list,y2list,marker='o',color = 'blue')

plt.show()
