''''
@Author HazmanNaimBinAhsan
Title: Simpson Rule for Integration
'''
#import necessary libraries
import numpy as np
import scipy.integrate as integrate

#Function to integrate
def f(x):
    return 1/(1+x**3)

#Limit of the integration [x0,xn]
x0 = 0
xn = 1
print("-------------------------------------")

#Simpson's Rule to Approximate the Value
M = (xn - x0)/6*(f(x0)+4*f((x0 + xn)/2)+f(xn))

#Exact Value of Integral
Exact, err = integrate.quad(f,x0,xn)

#Error
Error = abs(Exact - M)

print('Exact value:',Exact)
print('The approximated value: ',M)
print('Exact Error: ', Error)
