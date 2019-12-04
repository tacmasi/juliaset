import numpy as np
import matplotlib.pyplot as plt

def cabs(x, y):
    #return abs of x + iy
    return (x ** 2 + y ** 2)**(1/2)
#######param
#C(given)
cx, cy = 0, 1
R = (1 + (1 + 4 * cabs(cx, cy)**(1/2)))/2
#set window
minx, maxx = -2, 2
miny, maxy = -2, 2
num = 1000
lx = np.linspace(minx, maxx, num)
ly = np.linspace(miny, maxy, num)

#set maxiter
maxiter = 20
########
#def
def f(x, y, cx, cy):
    #C -> C
    return (x**2 - y**2 + cx, 2 * x * y + cy)
def retf(x, y, cx, cy, R, maxitr,  n = 0):
    #return n if abs(f(x))>=R
    if n > maxitr:
        return -1
    elif cabs(x, y) > R:
        return n
    else:
        nx, ny = f(x, y, cx, cy)
        return retf(nx, ny, cx, cy, R, maxitr, n + 1)
A = []
for y in ly:
    tmp = []
    for x in lx:
        tmp.append(retf(x,y,cx,cy,R,10,n=0))
    A.append(tmp)
#print(A)
plt.figure()
plt.imshow(A)
plt.axis('off')
plt.colorbar()
#plt.show()
plt.savefig("julia_i.png")
