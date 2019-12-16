import numpy as np
import matplotlib.pyplot as plt

def cabs(x, y):
    #return abs of x + iy
    return (x ** 2 + y ** 2)**(1/2)
#######param
#filename
filename = "mandelbrot_5.png"
#set window
#minx, maxx = -2, .75
#miny, maxy = -1.5, 1.5
pl = .03
minx = -.77
maxx = minx + pl
miny = -.1 
maxy = miny + pl 
#minx, maxx = -1.9, -1.899
#miny, maxy = -.00005, .00005
num = 480
lx = np.linspace(minx, maxx, num)
ly = np.linspace(miny, maxy, num)

#set maxitr
maxitr = 100
########
#def
def f(x, y, cx, cy):
    #C -> C
    return (x**2 - y**2 + cx, 2 * x * y + cy)
def return_n(x, y, cx, cy, maxitr,  n = 0):
    #return n if abs(f(x))>=R
    if n > maxitr:
        return -1
    elif cabs(x, y) > 2:
        return n
    else:
        nx, ny = f(x, y, cx, cy)
        return return_n(nx, ny, cx, cy, maxitr, n + 1)
A = [[]]*num
i = 1
for y in ly:
    tmp = []
    for x in lx:
        tmp.append(return_n(x,y,x,y,maxitr,n=0))
    A[-i] = tmp
    i += 1
#print(A)
plt.figure()
plt.imshow(A)
plt.axis('off')
plt.colorbar()
#plt.show()
plt.savefig(filename)
