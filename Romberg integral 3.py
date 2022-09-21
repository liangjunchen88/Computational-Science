#  龙贝格法求积分
import math
print('龙贝格积分法')
stra = input("请输入积分下限: ")
strb = input("请输入积分上限：")
strc = input("请输入积分精度：")
strd = input("请输入被积函数：")
a = float(stra)
b = float(strb)
eps = float(strc)

#eps=1E-5      # 精度
T=[]            # 复化梯形序列
S=[]            # Simpson序列
C=[]            # Cotes序列
R=[]            # Romberg序列
def func(x):    # 被积函数
#    y=(math.sin(x))/x
    y = eval(strd)
    return y
def Romberg(a,b,eps,func):
    h = b - a
    if a!= 0:
        T.append(h * (func(a) + func(b)) / 2)
    else :
        T.append(h * (1 + func(b)) / 2)
    ep=eps+1
    m=0
    while(ep>=eps):
        m=m+1
        t=0
        for i in range(2**(m-1)-1):
            t=t+func(a+(2*(i+1)-1)*h/2**m)*h/2**m
        t=t+T[-1]/2
        T.append(t)
        if m>=1:
            S.append((4*T[-1]-T[-2])/(4-1))
        if m>=2:
            C.append(((4**2)*S[-1]-S[-2])/(4**2-1))
        if m>=3:
            R.append(((4**3)*C[-1]-C[-2])/(4**3-1))
        if m>4:
            ep=abs(10*(R[-1]-R[-2]))
Romberg(a,b,eps,func)

print("积分结果为：{:.12f}".format(R[-1]))
