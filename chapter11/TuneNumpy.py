from datetime import datetime
import numpy as np

def f(x):
    return x**2 -3*x + 4
x = np.arange(1e5)

for j in range(0,3):

    t1 = datetime.now()
    y = [f(i) for i  in x]
    t2 = datetime.now()
    print('For for loop,         t2-t1=',t2 - t1)
    t1 = datetime.now()
    y = f(x)
    t2 = datetime.now()
    print('For vector function, t2-t1=' ,t2 - t1)
    
