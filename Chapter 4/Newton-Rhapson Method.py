''''
@Author HazmanNaimBinAhsan
Title: Newton-Rhapson Method
'''
#Import necessary libraries
import numpy as np
import matplotlib.pyplot as mpl

#Define the Function
def fp(x):
    return 3.0-2.0**x
#First derivative function
def fpp(x):
    return -2.0

#initialisation/Initial Guess
x = int(input("Enter your initial guess: ")) 
xinitial = x
#Insert tolerance of error
tol = float(input("Enter your tolerance of error: "))

#start iteration
for i in range (0,100):
    xi = x - fp(x)/fpp(x) #Newton Rhapson Method for Optimisation
    delx = abs(xi - x) #Error/Tolerance of Error
    if delx < tol:
        print('Stop Iteration')
        break
    else:
        print("Number of iteration = "+str(i)+"")
        print("xi = "+str(xi)+"")
        print("x = "+str(x)+"")
        print("The error is "+str(delx)+"")
        print("-------------------------------------")
        mpl.scatter(x,fp(x),label='Approximated Root of Function')
        x = xi
print("-------------------------------------")
print("Your inital guess is = "+str(xinitial)+"")
print("The tolerance of error is, tol = "+str(tol)+"")
print("The number of iteration is, i = "+str(i)+"")
print("The approximated root of the function is, x = "+str(xi)+"")
print("The error is, delx = "+str(delx)+"")


#Graph Settings
x = np.arange(-10,5,0.01) #Range of the X-axis
  
#Theoretical Plot      
mpl.plot(x,fp(x),label='Graph of f(x) against x')
mpl.axvline(0,color='Black')
mpl.axhline(0,color='Black')
mpl.xlabel('x')
mpl.ylabel('f(x)')
mpl.title('Graph of f(x) and approximated root of the function')

mpl.show()