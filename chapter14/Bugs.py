"""
From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook
by RH Landau, MJ Paez, and CC Bordeianu
Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
Support by National Science Foundation
"""
# Logistic map

#from visual.graph import *
import matplotlib.pyplot as plt
import numpy as np

m_min = 1.0
m_max = 4.0
step = 0.01

"""
graph1 = gdisplay(width=600, height=400, title='Logistic Map',\
        xtitle='m', ytitle='x', xmax=4.0, xmin=1., ymax=1., ymin=0.)
pts = gdots(shape = 'round', size = 1.5, color = color.green)
"""

#lasty = int(1000 * 0.5)                         # Eliminates some points
lasty = 0.5
count = 0  # Plot every 2 iterations
eps =1e-3
m = m_min

#for m in np.range(m_min, m_max, step):

mlist = []  # x座標
ylist = []  # y座標

for j in range(0, 301):
    print(m)
    m += step
    y = 0.5
    """
    for i in range(1,201,1):                          # Avoid transients
        y = m*y*(1-y)
    for i in range(201,402,1):
        y = m*y*(1-y)
    """
    for i in range(1,402,1):
        y = m*y*(1-y)
    for i in range(201, 402, 1):                      # Avoid transients
        #oldy=int(1000*y)
        y = m*y*(1-y)   
        #inty = int(1000 * y)
        #if  inty != lasty and count%2 == 0:
        if(abs(y-lasty) > eps and count%2 ==0):
            #print('true')
            mlist.append(m)
            ylist.append(y)
            #plt.plot(m,y,'green')
        #lasty = inty
        lasty = y
        count += 1

plt.figure(figsize=(6, 4))
plt.title('Logistic Map')
plt.xlabel('m')
plt.ylabel('x')
plt.plot(mlist,ylist,'green')
plt.show()

#なんで正常に動かないのかわからない
