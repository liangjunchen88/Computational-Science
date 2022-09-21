import numpy as np
from sympy import *
import matplotlib.pyplot as plt

A = [[1, 2, 0, 0, 0], [2, 3, 1, 0, 0], [0, -3, 4, 2, 0], [0, 0, 4, 7, 1], [0, 0, 0, -5, 6]]
b = [5, 9, 2, 19, -4]
#追 
rownum = len(A)
colnum = len(A[0])
u = [0]*rownum
y = [0]*rownum
l = [0]*rownum
x = [0]*rownum
u[0] = A[0][0]
y[0] = b[0]
i = 1
while i < rownum:
    l[i] = A[i][i-1]/u[i-1]
    u[i] = A[i][i] - l[i]*A[i-1][i]
    y[i] = b[i] - l[i]*y[i-1]
    i += 1
    
#赶
x[rownum-1] = y[rownum-1]/u[rownum-1]
i = rownum-2
while i >= 0:
    x[i] = (y[i] - A[i][i+1]*x[i+1])/u[i]
    i += -1

print(u)
print(l)
print(y)
print("方程组的解为： ", x)