""" From "A SURVEY OF COMPUTATIONAL PHYSICS", Python eBook Version
   by RH Landau, MJ Paez, and CC Bordeianu
   Copyright Princeton University Press, Princeton, 2012; Book  Copyright R Landau, 
   Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2012.
   Support by National Science Foundation , Oregon State Univ, Microsoft Corp"""  
		
# QMC.py:      Quantum MonteCarlo (Feynman path integration)

#from visual import *
#from visual.graph import *
import random
import matplotlib.pyplot as plt
from numpy import *
import matplotlib.animation as animation
import math

N = 100
M = 101
xscale = 10.0
path = zeros([M], float)
prob = zeros([M], float)   # Initialize

x1list =[]
y1list =[]
x2list = []
y2list = []
ims1 = []
ims2 = []

"""
#trajec = display(width = 300,height=500, title='Spacetime Trajectories')
#trplot = curve(y = range(0, 100), color=color.magenta, display = trajec)
 
def trjaxs():                                                      # Axis
   trax = curve(pos = [(-97,-100),(100,-100)], color = color.cyan, display = trajec)
   label(pos = (0,-110),  text = '0', box = 0, display = trajec)
   label(pos = (60,-110), text = 'x', box = 0, display = trajec) 
 
#wvgraph = display(x=340,y=150,width=500,height=300, title='Ground State')
#wvplot = curve(x = range(0, 100), display = wvgraph)                
#wvfax = curve(color = color.cyan)
 
def wvfaxs():                                      # Axis for probability
   wvfax = curve(pos =[(-600,-155),(800,-155)], display=wvgraph,color=color.cyan)
   curve(pos = [(0,-150), (0,400)], display=wvgraph, color=color.cyan) 
   label(pos = (-80,450), text='Probability', box = 0, display = wvgraph)
   label(pos = (600,-220), text='x', box=0, display=wvgraph)
   label(pos = (0,-220), text='0', box=0, display=wvgraph)   

trjaxs()
wvfaxs()                                  # Plot axes
"""

def energy(path):                                             # HO energy
    sums = 0.                                
    for i in range(0,N-2):sums += (path[i+1]-path[i])*(path[i+1]-path[i])
    sums += path[i+1]*path[i+1]; 
    return sums 

def plotpath(path):                                    # Plot trajectory
   for j in range (0, N):                     
       #trplot.x[j] = 20*path[j]
       #trplot.y[j] = 2*j - 100
       #line.set_data(20*path[j], 2*j -100)
       #line, = ax1.plot(20*path[j], 2*j -100,"r",lw = 2)
       x1list.append(20*path[j])
       y1list.append(2*j - 100)
   im1 =plt.plot(x1list,y1list)
   ims1.append(im1)
   ani1 = animation.ArtistAnimation(fig1,ims1,interval=1 ,repeat_delay = 1000)
   x1list.clear()
   y1list.clear()
       
def plotwvf(prob):                                            # Plot prob
    for i in range (0, 100):
       #wvplot.color = color.yellow
       #wvplot.x[i] = 8*i - 400# For centered fig
       #x2list.append(8*i - 400)
       a = 1
oldE = energy(path)
#fig1 = plt.figure()
#
#ax1 =fig1.add_subplot(111, autoscale_on = False, xlim=(-5,105),ylim=(-5,110.0))
#ax1.grid()
#line, = ax1.plot(20*path[j], 2*j -100,"r",lw = 2)
fig1 = plt.figure()
while True:                                         # Pick random element
    #rate(10)                                             # Slow paintings
    element = int(N*random.random())              # Metropolis algorithm
    change = 2.0*(random.random() - 0.5)    
    path[element] += change                                 # Change path
    newE = energy(path)                                   # Find new E
    if  newE > oldE and math.exp(-newE+oldE)<= random.random():
          path[element] -= change                                # Reject
          plotpath(path)# Plot trajectory
          
          #print(x1list)
          

          #ani = animation.FuncAnimation(fig1,plotpath(path),1)
    elem = int(path[element]*16 + 50)            # if path = 0, elem = 50
    
    # elem = m *path[element] + b is the linear transformation
    # if path=-3, elem=2 if path=3., elem=98 => b=50, m=16 linear TF.
    # this way x = 0 correspond to prob[50]
    
    if elem < 0:
       elem = 0                     
    if elem > 100:
       elem = 100                            # If exceed max
    prob[elem] += 1                                # increase probability
    #plotwvf(prob)
    #im2 = plt.plot(x2list,color = 'y')
    #ims2.append(im2)
    #ani = animation.FuncAnimation(fig2,plotwvf(prob),1)# Plot prob
    oldE = newE
    
    
    #fig2 = plt.figure()
    #ani2 =  animation.ArtistAnimation(fig2,ims2,interval=10 ,repeat_delay = 1000)
    plt.show()


