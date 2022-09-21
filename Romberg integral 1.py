import numpy as np
 
# 编写Romberg求积法，并计算
def romberg(inf, sup, lenth): #定义函数的输入，积分上下界，分块的数量
    vec_init = np.zeros(lenth + 1)
    vec_init[0] = 0.5 * (func(sup) + func(inf)) / (sup - inf)
    #初始化T0向量，计算并赋值
    for i in range(1, lenth):
        vec_init[i] = 0.5 * vec_init[i - 1] + np.array(
            [func(inf + (sup - inf) * (2 * j + 1)/(2 ** i))
             for j in range(2 ** (i - 1) - 1)], dtype=np.float64).sum() * (sup - inf) / 2 ** i
    count = lenth
    deepth = 1
    #设置停止条件，前后两次迭代结果之差小于10^-10
    while np.abs(vec_init[count] - vec_init[count - 1]) > 10 ** -10:
        print('现在在第', deepth, '层')
        vec_init[0: count - 1] = np.array([(4 ** deepth * vec_init[k + 1] - vec_init[k]) / (4 ** deepth - 1)
                                          for k in range(count - 1)], dtype=np.float64)
        deepth += 1
        count -= 1
    return vec_init[count]
 
def func(x):
    return (np.log(1 + x)) / (1 + x ** 2)
 
print('计算结果为', romberg(0, 1, 20))
 
