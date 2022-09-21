import numpy as np
from sympy import *
import matplotlib.pyplot as plt

#输入第二种边界条件、XY的取值
print('第二种边界条件')
str0 = input("请分别输入两个端点的一阶导数值，用空格隔开：")  
list0 = str0.split(" ") 
list0_length = len(list0)
i = 0
m = []
while i <= list0_length-1:
    m.append(int(list0.pop())) 
    i += 1
m.reverse()
X = [] 
str1 = input("请输入x的取值，用空格隔开：")  
list1 = str1.split(" ") 
list1_length = len(list1)
i = 0
while i <= list1_length-1:
    X.append(int(list1.pop()))
    i += 1
X.reverse()
Y = []
str2 = input("请输入y的取值，用空格隔开：")  
list2 = str2.split(" ") 
list2_length = len(list2)
i = 0
while i <= list2_length-1:
    Y.append(int(list2.pop())) 
    i += 1
Y.reverse()

#求H
X_length = len(X)
H = [0]*(X_length - 1)
i = 0
while i <= X_length  - 2:
    H[i] = X[i + 1] - X[i]
    i += 1

#求三弯矩方程的两个系数P、Q
H_length = len(H)
P = [0]*(H_length - 1)
Q = [0]*(H_length - 1)
i = 0
while i <= H_length  - 2:
    P[i] = H[i]/(H[i] + H[i+1])
    Q[i] = 1- P[i]
    i += 1

#列出三弯矩方程组的系数矩阵
P_lenth = len(P)
A = [[0 for i in range(P_lenth+1)] for i in range(P_lenth+1)]
A[0][0] = 2
A[0][1] = 1
A[P_lenth][P_lenth] = 2
A[P_lenth][P_lenth-1] = 1
i = 1
while i <= P_lenth - 1:
    A[i][i] = 2
    A[i][i-1] = P[i]
    A[i][i+1] = Q[i]
    i += 1

#求出差商表
d = [0]*(P_lenth)
def fun(X, Y):
    rows=len(X)        #行数
    cols=len(Y)+1      #列数
    temp=[[0 for col in range(cols)] for row in range(rows)]  
    for i in range(rows):
        temp[i][0]=X[i]
        temp[i][1]=Y[i]
    for i in range(1,rows):
        for j in range(2,i+2):
            temp[i][j]=(temp[i][j-1]-temp[i-1][j-1])/(temp[i][0]-temp[i-j+1][0])
    i = 0
    while i <= rows-3:
        d[i] = 6*temp[i+2][3]
        i += 1
    print("x的取值：" , X)
    print("y的取值：" , Y)
    print("差商表为： ", temp)
fun(X, Y)

#求出三弯矩方程组的b
B = [0]*(P_lenth+1)
B[0] = 6*((Y[1]-Y[0])/H[0] - m[0])/H[0]
B[P_lenth] = 6*(m[1] - (Y[len(Y)-1]-Y[len(Y)-2])/H[X_length - 2])/H[X_length - 2]
i = 0
while i < len(B)-1:
    B[i] = d [i]
    i += 1

#求解三弯矩方程组
#追
rownum = len(A)
colnum = len(A[0])
u = [0]*rownum
y = [0]*rownum
l = [0]*rownum
x = [0]*rownum
u[0] = A[0][0]
y[0] = B[0]
i = 1
while i < rownum:
    l[i] = A[i][i-1]/u[i-1]
    u[i] = A[i][i] - l[i]*A[i-1][i]
    y[i] = B[i] - l[i]*y[i-1]
    i += 1
#赶
x[rownum-1] = y[rownum-1]/u[rownum-1]
i = rownum-2
while i >= 0:
    x[i] = (y[i] - A[i][i+1]*x[i+1])/u[i]
    i += -1

#得出M
M = [0]*len(X)
i = 0
while i <= len(X) -1:
    M[i] = x[i-1]
    i += 1


print("6*三阶差商为 d： ", d)
print("h的取值：" , H)
print("p的取值：" , P)
print("q的取值：" , Q)
print("三弯矩方程组的系数: ", A)
print("三弯矩方程组的b: ", B)
print("三弯矩方程组的解：", x)
print("所有的M；", M)

#求出三次样条插值
i = 1
while i < len(M) :
    print("S(x) = ",(M[i]-M[i-1])/(6*H[i-1]),"x**3 + ",
          (M[i-1]*X[i]-M[i]*X[i-1])/(2*H[i-1]),"x**2 + ",
          ( M[i]*(X[i-1]**2)-M[i-1]*(X[i]**2))
          /(2*H[i-1]) + (Y[i] - Y[i-1])/H[i-1]
          + H[i-1]*(M[i-1]-M[i])/6,"x + ",(M[i-1]*(X[i]**3)
          -M[i]*(X[i-1]**3))/(6*H[i-1]) + ( Y[i-1]*X[i]
          -Y[i]*X[i-1] )/H[i-1] +  H[i-1]*(M[i]*X[i-1]
          - M[i-1]*X[i])/6 , "     ",X[i-1],"<=",X[i] ) 
    i += 1
