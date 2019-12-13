import pylab as p
from numpy import *

p.title('Grade Inflation')
p.xlabel('Years in College')
p.ylabel('GPA')

xa = array([-1, 5])
ya = array([0, 0])
p.plot(xa,ya)

x0 = array([0,1,2,3,4])
y0 = array([-1.4 , +1.1 , 2.2 , 3.3 , 4.0])
p.plot(x0, y0, 'bo')
p.plot(x0, y0, 'g')

x1 = arange(0 ,5 ,1)
y1 = array([4.0 , 2.7 , -1.8 , -0.9 , 2.6])
p.plot(x1, y1, 'r')

errBot = array([1.0 , 0.3 , 1.2 , 0.4 , 0.1])
errTop = array([2.0 , 0.6 , 2.3 , 1.8 , 0.4])
p.errorbar(x1, y1 , [errBot, errTop], fmt = 'o')


p.grid(True)
p.show()

