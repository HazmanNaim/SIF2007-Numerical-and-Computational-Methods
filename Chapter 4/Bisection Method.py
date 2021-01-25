''''
@Author HazmanNaimBinAhsan
Title: Bisection Method
'''
#Import necessary libraries
import numpy as np
import matplotlib.pyplot as mpl

#Drfine the Function
def fp(x):
    return 3.0-2.0**x

#Interval which the root must be in the range
print("The range of the function")
a = float(input("a: "))
b = float(input("b: ")) 
ai = a
bi = b

#Insert tolerance of error
tol = float(input("Enter your tolerance of error: "))

#Define Error
error = abs(b-a)

#Start Iteration
for i in range(0,100):
  c = a + 0.5*(b-a)
  if fp(c)*fp(a)<0:
    a = a
    b = c
    error = abs(b-a)
  else:
       a = c
  if error > tol:
      print("Number of iteration = "+str(i)+"")
      print("a = "+str(a)+"")
      print("b = "+str(b)+"")
      print("c = "+str(c)+"")
      print("The error is "+str(error)+"")
      print("-------------------------------------")
      mpl.scatter(a,fp(a))
  else:
      print('Stop Iteration')
      break  
  
print("Your range of interval is ["+str(ai)+","+str(bi)+"]")
print("The tolerance of error is, tol = "+str(tol)+"")
print("The number of iteration is, i = "+str(i)+"")
print("The approximated root of the function is, x = "+str(c)+"")
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