#中点法求解常微分方程

stra = input("请输入函数f(x,y)：")
strb = input("请输入步长h: ")
strc = input("请输入x的下界： ")
strd = input("请输入x的上界： ")
stre = input("请输入y的初值： ")
a = float(strc)
b = float(strd)
h = float(strb)
def func(x, y):    
    t = eval(stra)
    return t
k = int((b - a)/h)
x = [0]*(k + 1)
i = 0
while i<= k:
    x[i] = a + i*h
    i += 1
y = [0]*(k + 1)
y[0] = float(stre)
y[1] = 0.0909
j = 1
while j< k:
    y[j+1] = y[j-1] + 0.2*(1-y[j]) 
    print(y[j+1])
    j += 1


