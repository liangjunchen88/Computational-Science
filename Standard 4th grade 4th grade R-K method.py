#标准4级4阶R-K法
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
K1 = [0]*k
K2 = [0]*k
K3 = [0]*k
K4 = [0]*k
j = 0
print(' ')
print("y的取值为：")
while j< k:
    K1[j] = h*func(x[j], y[j])
    K2[j] = h*func(x[j]+h/2, y[j]+K1[j]/2)
    K3[j] = h*func(x[j]+h/2, y[j]+K2[j]/2)
    K4[j] = h*func(x[j]+h, y[j]+K3[j])
    y[j+1] = y[j] + (K1[j] + 2*(K2[j] + K3[j]) + K4[j])/6
    print(y[j+1])
    j += 1