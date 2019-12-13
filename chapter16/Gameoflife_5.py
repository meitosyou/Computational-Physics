""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""
	
# Gameoflife.py: Cellular automata in 2 dimensions

'''* Rules: a cell can be either dead (0) or alive (1)
   * If a cell is alive:
   * on next step will remain alive if
   * 2 or 3 of its closer 8 neighbors are alive.
   * If > 3 of 8 neighbors are alive, cell dies of overcrowdedness
   * If less than  2 neighbors are alive the cell dies of loneliness
   * A dead cell will be alive if  3 of its 8 neighbors are alive'''

#from visual import *
#from visual.graph import *
import random
import matplotlib.pyplot as plt
from numpy import *
import matplotlib.animation as animation

"""
scene = display(width= 500,height= 500, title= 'Game of Life')# 1st array

curve(pos= [(-49,-49),(-49,49),(49,49),(49,-49),(-49,-49)],color=color.white)
boxes = points(shape='square', size=8, color=color.cyan)
"""
cell  = zeros((50,50))
cellu = zeros((50,50))
xlist =[]
ylist =[]
def drawcells(ce):
    
    #boxes.pos = []                                 # erase previous cells
    for j in range(0,50):       
        for i in range(0,50):
            if ce[i,j] == 1:
                xx = 2*i-50
                yy = 2*j-50
                xlist.append(xx)
                ylist.append(yy)
    return xlist, ylist
                #boxes.append(pos=(xx,yy))
            
def initial():
   for j in range (20,28):                       # initial state of cells
        for  i in range(20, 28):  
            r= int(random.random()*2)
            cell[j,i] = r                       # dead or alive at random
   return cell           

def gameoflife(cell):                  # rules and  analysis of neighbors
    for i in range(1,49):              # observe 8 neighbors of cell[i,j]
        for j in range(1,49):
            sum1 = cell[i-1,j-1] + cell[i,j-1] + cell[i+1,j-1] # sum neighb
            sum2 = cell[i-1,j] + cell[i+1,j] + cell[i-1,j+1] + cell[i,j+1] \
                   + cell[i+1,j+1] 
            alive = sum1+sum2
            if cell[i,j] == 1:
                if  alive == 2 or alive == 3:             # remains alive
                    cellu[i,j] = 1                                # lives
                if  alive > 3 or alive < 2:     # overcrowded or solitude
                    cellu[i,j] = 0                                 # dies
            if  cell[i,j] == 0:
                if  alive == 3:
                    cellu[i,j] = 1                              # revives
                else:
                    cellu[i,j] = 0                         # remains dead
    alive = 0                
    return cellu

k=range(0,101)
fig=plt.figure()                            
ax = fig.add_subplot(111, autoscale_on=False)
ax.grid()                                                       # Plot  grid
plt.title('Game of Life')
            

#plt.figure(figsize=(5,5))
#plt.plot(xlist,ylist)

temp = initial()               
#drawcells(temp)
for j in range(0,50):
    for i in range(0,50):
        if cell[i,j] == 1:
            xx = 2*i-50
            yy = 2*j-50
            xlist.append(xx)
            ylist.append(yy)
point, = plt.plot(xlist,ylist, 'o',lw=2)     


"""
while True:
    rate(6)
    cell = temp
    temp = gameoflife(cell)
    drawcells(cell) 
"""

def animate(p):
    xlist.clear()
    ylist.clear()#clearの位置はここ
    cell = p
    temp = gameoflife(cell)
    for j in range(0,50):       
        for i in range(0,50):
            if cell[i,j] == 1:
                xx = 2*i-50
                yy = 2*j-50
                xlist.append(xx)
                ylist.append(yy)
    point, = plt.plot(xlist,ylist, 'o',lw=2) 
                
                

    #xlist , ylist = drawcells(cell)
    #print(xlist)
    #print(ylist)
    #point.set_data(xlist,ylist)
    
    #return point,

ani = animation.FuncAnimation(fig,animate(temp),fargs = (fig, point))
plt.show()

#TypeError: 'tuple' object is not callable
