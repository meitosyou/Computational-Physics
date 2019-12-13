""" From "A SURVEY OF COMPUTATIONAL PHYSICS", Python eBook Version
   by RH Landau, MJ Paez, and CC Bordeianu
   Copyright Princeton University Press, Princeton, 2011; Book  Copyright R Landau, 
   Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2011.
   Support by National Science Foundation , Oregon State Univ, Microsoft Corp"""  

# LyapLog.py:                Lyapunov coef for logistic map

#from visual import *
#from visual.graph import *
from matplotlib import pyplot as plt
import numpy as np
import math
m_min = 2.1
m_max = 4.0
step = 0.05
m = m_min
"""graph1 = gdisplay( title = 'Lyapunov coef (blue) for LogisticMap (red)', 
                   xtitle = 'm', ytitle = 'x , Lyap',
                   xmax=5.0, xmin=0, ymax = 1.0, ymin =  - 0.6)
funct1 = gdots(color = color.red)
funct2 = gcurve(color = color.yellow)
"""
m1list = []  # x座標
m2list = []
y1list = []  # y座標
y2list = []

#for m in arange(m_min, m_max, step):                             # m loop
for j in range( 42,81 ):
    m += step
    #print(m)
    y = 0.5
    suma = 0.0
    for i in range(1, 401, 1):
        y = m*y*(1 - y)        # Skip transients
    for i in range(402, 601, 1):
        y = m*y*(1 - y)
        #funct1.plot(pos = (m, y) )
        m1list.append(m)
        y1list.append(y)
        suma = suma  +  np.log(abs(m*(1. - 2.*y) ))               # Lyapunov
        
    m2list.append(m)
    y2list.append(y)
    #funct2.plot(pos = (m, suma/401) )                         # Normalize

fig1 =plt.figure()
plt.title('Lyapunov coef (blue) for LogisticMap (red)')
plt.xlabel('m')
plt.ylabel('x')
plt.plot(m1list, y1list, 'red')

fig2 =plt.figure()
plt.title('Lyapunov coef (blue) for LogisticMap (red)')
plt.xlabel('m')
plt.ylabel('Lyap')
plt.plot(m2list, y2list, 'green')

plt.show()
