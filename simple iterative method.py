#简单迭代法
x = [0]*20
x[0] = 1.5
i = 0
while i <= 15:
    x[i+1] = (1 + (x[i])**2)**(1/3)
    print(x[i+1])
    i = i + 1