#简单迭代法求解非线性方程组
import math
x = [0]*100
y = [0]*100
i = 0
while i <= 98:
    x[i+1] = 0.5*(math.cos(y[i]))
    y[i+1] = 0.5*(math.sin(x[i+1]))
    print(x[i+1],' ',y[i+1])
    i += 1
    
