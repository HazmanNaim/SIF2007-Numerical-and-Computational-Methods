''''
@Author HazmanNaimBinAhsan
Title: Mid-Point Method for Integration
'''
#import necessary libraries
import numpy as np
import scipy.integrate as integrate

#Function
def f(x):
    return x*(1 - x**2)

#Initialisation
print("Limit of integration [x0,xn]")
x0 = int(input("Insert x0: "))
xn = int(input("Insert xn: "))
print("-------------------------------------")

#Midpoint rule
M = (xn - x0)*f((x0 + xn)/2)

#Exact Integral from scipy
Exact, err = integrate.quad(f,x0,xn)

#Error
Error = abs(Exact - M)

print('Exact value:',Exact)
print('The approximated value: ',M)
print('Exact Error: ', Error)


    




