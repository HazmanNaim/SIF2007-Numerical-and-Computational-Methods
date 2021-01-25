''''
@Author HazmanNaimBinAhsan
Title: Solving systems of linear equations

2x + 4y + 6z = 4
x - 3y - 9z = -11
8x + 5y - 7z =1
'''

#Import necessary libraries
import numpy as np
import scipy.linalg as la

A = np.array([[14,14,-9,3,-5],[14,52,-15,2,-32],[-9,-15,36,-5,16],[3,2,-5,47,49],[-5,-32,16,49,79]])
B = np.array([-15,-100,106,329,463])

print(la.solve(A,B))

Ainverse = la.inv(A)
print(la.solve(Ainverse,B))

P, L, U = la.lu(A)
print(P)
print(L)
print(U)