#后退欧拉法

stra = input("请输入函数f(x,y)：")
strb = input("请输入步长h: ")
strc = input("请输入x的下界： ")
strd = input("请输入x的上界： ")
stre = input("请输入y的初值： ")
a = float(strc)
b = float(strd)
h = float(strb)
def func(x, y):    
#    y=(math.sin(x))/x
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

j = 0
while j< k:
    y[j+1] = (y[j] + 0.1)/1.1
    print(y[j+1])
    j += 1

