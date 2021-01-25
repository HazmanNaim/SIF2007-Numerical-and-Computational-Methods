''''
@Author HazmanNaimBinAhsan
Title: Secant Method
'''
#Import necessary libraries
import numpy as np
import matplotlib.pyplot as mpl

#Define the Function
def fp(x):
    return 3.0-2.0**x

#Interval which the root must be in the range
print("The range of the function [x1,x2]")
x0 = float(input("x0: "))
x1 = float(input("x1: ")) 
ai = x0
bi = x1

#Insert tolerance of error
tol = float(input("Enter your tolerance of error: "))


#Define Error
f0 = fp(x0)
f1 = fp(x1)

for i in range(1,1000):
    f0
    f1
    x2 = x0 - f0*((x1-x0)/(f1-f0))
    error = abs(x2-x1)
    if error > tol:
        print("Number of iteration = "+str(i)+"")
        print("x0 = "+str(x0)+"")
        print("f0 = "+str(f0)+"")        
        print("x1 = "+str(x1)+"")
        print("f1 = "+str(f1)+"")
        print("x2 = "+str(x2)+"")
        print("The error is "+str(error)+"")
        print("-------------------------------------")
        mpl.scatter(x2,fp(x2))
        x0 = x1
        x1 = x2
    else:
      print('Stop Iteration')
      break      

print("Your range of interval is ["+str(ai)+","+str(bi)+"]")
print("The tolerance of error is, tol = "+str(tol)+"")
print("The number of iteration is, i = "+str(i)+"")
print("The approximated root of the function is, x = "+str(x2)+"")
print("The error is, error = "+str(error)+"")

#Graph Settings
x = np.arange(ai,bi,0.01) #Range of the X-axis
  
#Theoretical Plot      
mpl.plot(x,fp(x),label='Graph of f(x) against x')
mpl.axvline(0,color='Black')
mpl.axhline(0,color='Black')
mpl.xlabel('x')
mpl.ylabel('f(x)')
mpl.title('Graph of f(x) and approximated root of the function')

mpl.show()        
    
        
    


