''''
@Author HazmanNaimBinAhsan
Title: Runge-Kutta order 2
'''
#import necessary libraries
import numpy as np
import matplotlib.pyplot as mpl

#First order differential equation
def fp(x,y):
    return (y - x)/(y + x)

#Runge-Kutta Order 2
def RK2(x0,y0,xn,n):
    for i in range(0,n):
        k1 = h * (fp(x0, y0))
        k2 = h * (fp((x0+h/2), (y0+k1/2)))
        k3 = h * (fp((x0+h/2), (y0+k2/2)))
        k4 = h * (fp((x0+h), (y0+k3)))
        k = (k1+2*k2+2*k3+k4)/6
        yn = y0 + k 
        
#Initialisation
print("Initialisation")
x0 = int(input("Insert x0: "))
y0 = int(input("Insert y0 at x0: "))
print("-------------------------------------")

#Final Point
print("Final Point")
xn = int(input("Insert xn: "))
print("-------------------------------------")

#Stepsize
print("Stepsize")
n = int(input("How many points: "))
h = (xn - x0)/n
print("Your stepsize is"+str(h)+".")
print("-------------------------------------")

x = np.arange(x0,xn,0.01) #Range of the X-axis

for i in range(0,n):
    k1 = h * (fp(x0, y0))
    k2 = h * (fp((x0+h), (y0+h*k1)))
    yn = y0 + h/2*(k1 + k2)
    if i < n:
        print("Number of iteration = "+str(i)+"")
        print("x0 = "+str(x0)+"")
        print("y0 = "+str(y0)+"")
        print("yn = "+str(yn)+"")        
        print("-------------------------------------")
        mpl.scatter(x0,y0)
        y0 = yn
        x0 = x0+h
    else:
      print('Stop Iteration')
      break

mpl.axvline(0,color='Black')
mpl.axhline(0,color='Black')
mpl.xlabel('x')
mpl.ylabel('f(x)')
mpl.title('Graph of f(x) Runge-Kutta Order 2')

mpl.show()
