''''
@Author HazmanNaimBinAhsan
Title: Euler Method
'''
#import necessary libraries
import numpy as np
import matplotlib.pyplot as mpl

#First order differential equation
def fp(x,y):
    return (y - x)/(y + x)

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
    y1 = y0 + h*fp(x0,y0)
    error = abs(y1 -y0)
    if i < n:
        print("Number of iteration = "+str(i)+"")
        print("y0 = "+str(y0)+"")
        print("f0 = "+str(fp(x0,y0))+"")        
        print("y1 = "+str(y0 + 1)+"")
        print("The error is "+str(error)+"")
        print("-------------------------------------")
        mpl.scatter(x0,y0)
        x0 = h + x0
        y0 = y1
    else:
      print('Stop Iteration')
      break 
  
mpl.axvline(0,color='Black')
mpl.axhline(0,color='Black')
mpl.xlabel('x')
mpl.ylabel('f(x)')
mpl.title('Graph of f(x) Euler Method')

mpl.show()     
