import math

print('龙贝格积分法')
stra = input("请输入积分下限: ")
strb = input("请输入积分上限：")
strc = input("请输入积分精度：")
a = float(stra)
b = float(strb)
c = float()
#a=0             # 积分下限
#=1             # 积分上限
#eps=10**-5      # 精度
T=[]            # 复化梯形序列
S=[]            # Simpson序列
C=[]            # Cotes序列
R=[]            # Romberg序列
def func(x):    # 被积函数
    y=math.exp(-x)
    return y
def Romberg(a,b,c,func):
    h = b - a
    T.append(h * (func(a) + func(b)) / 2)
    d = c +1
    m=0
    while(d >= c):
        m=m+1
        t=0
        for i in range(2**(m-1)-1):
            t=t+func(a+(2*(i+1)-1)*h/2**m)*h/2**m
        t=t+T[-1]/2
        T.append(t)
        if m>=1:
            S.append((4**m*T[-1]-T[-2])/(4**m-1))
        if m>=2:
            C.append((4**m*S[-1]-S[-2])/(4**m-1))
        if m>=3:
            R.append((4**m*C[-1]-C[-2])/(4**m-1))
        if m>4:
            d = abs(10*(R[-1]-R[-2]))
Romberg(a,b,c,func)
#print(T)
#print(S)
#print(C)
#print(R)
# 计算机参考值0.6321205588
print("积分结果为：{:.5f}".format(R[-1]))
