import numpy as np
import matplotlib.pyplot as plt

filename = "a.png"
def cabs(x, y):
    #return abs of x + iy
    return (x ** 2 + y ** 2)**(1/2)
#######param
#C(given)
#cx, cy = -1.4, -0.4
cx, cy = +.01, -1
R = (1 + (1 + 4 * cabs(cx, cy)**(1/2)))/2
#set window
minx, maxx = -2, 2
miny, maxy = -2, 2
num = 480
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
A = [[]]*num
i = 1
for y in ly:
    tmp = []
    for x in lx:
        tmp.append(retf(x,y,cx,cy,R,10,n=0))
    A[-i] = tmp.copy()
    i += 1
#print(A)
plt.figure()
plt.imshow(A)
plt.axis('off')
plt.colorbar()
plt.show()
#plt.savefig(filename)
