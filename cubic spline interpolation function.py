import math
import numpy as np
import matplotlib.pyplot  as plt
from sympy import *
from pylab import mpl
 
def func(y):
    y = np.float64(y)
    return 1/(1 + y * y)
 
def draw_pic(words, x, y):
    fig=plt.figure()
    plt.plot(x, y, label='interpolation')
    plt.plot(x, func(x), label='raw')
    plt.legend()
    plt.title(words, FontProperties='SimHei')
    #plt.show()
    plt.savefig(words+'.png')
    plt.close(fig)
    pass
 
def spline3_Parameters(x_vec):
        # parameter为二维数组，用来存放参数，size_of_Interval是用来存放区间的个数
        x_new = np.array(x_vec)
        parameter = []
        size_of_Interval = len(x_new) - 1;
        i = 1
        # 首先输入方程两边相邻节点处函数值相等的方程为2n-2个方程
        while i < len(x_new) - 1:
            data = np.zeros(size_of_Interval * 4)
            data[(i - 1) * 4] = x_new[i] * x_new[i] * x_new[i]
            data[(i - 1) * 4 + 1] = x_new[i] * x_new[i]
            data[(i - 1) * 4 + 2] = x_new[i]
            data[(i - 1) * 4 + 3] = 1
            data1 = np.zeros(size_of_Interval * 4)
            data1[i * 4] = x_new[i] * x_new[i] * x_new[i]
            data1[i * 4 + 1] = x_new[i] * x_new[i]
            data1[i * 4 + 2] = x_new[i]
            data1[i * 4 + 3] = 1
 
            parameter.append(data)
            parameter.append(data1)
            i += 1
        # 输入端点处的函数值。为两个方程, 加上前面的2n - 2个方程，一共2n个方程
        data = np.zeros(size_of_Interval * 4)
        data[0] = x_new[0] * x_new[0] * x_new[0]
        data[1] = x_new[0] * x_new[0]
        data[2] = x_new[0]
        data[3] = 1
        parameter.append(data)
 
        data = np.zeros(size_of_Interval * 4)
        data[(size_of_Interval - 1) * 4] = x_new[-1] * x_new[-1] * x_new[-1]
        data[(size_of_Interval - 1) * 4 + 1] = x_new[-1] * x_new[-1]
        data[(size_of_Interval - 1) * 4 + 2] = x_new[-1]
        data[(size_of_Interval - 1) * 4 + 3] = 1
        parameter.append(data)
        # 端点函数一阶导数值相等为n-1个方程。加上前面的方程为3n-1个方程。
        i = 1
        while i < size_of_Interval:
            data = np.zeros(size_of_Interval * 4)
            data[(i - 1) * 4] = 3 * x_new[i] * x_new[i]
            data[(i - 1) * 4 + 1] = 2 * x_new[i]
            data[(i - 1) * 4 + 2] = 1
            data[i * 4] = -3 * x_new[i] * x_new[i]
            data[i * 4 + 1] = -2 * x_new[i]
            data[i * 4 + 2] = -1
            parameter.append(data)
            i += 1
        # 端点函数二阶导数值相等为n-1个方程。加上前面的方程为4n-2个方程。
        i = 1
        while i < len(x_new) - 1:
            data = np.zeros(size_of_Interval * 4)
            data[(i - 1) * 4] = 6 * x_new[i]
            data[(i - 1) * 4 + 1] = 2
            data[i * 4] = -6 * x_new[i]
            data[i * 4 + 1] = -2
            parameter.append(data)
            i += 1
        #端点处的函数值的二阶导数为原函数的二阶导数，为两个方程。总共为4n个方程。
        data = np.zeros(size_of_Interval * 4)
        data[0] = 6 * x_new[0]
        data[1] = 2
        parameter.append(data)
        data = np.zeros(size_of_Interval * 4)
        data[-4] = 6 * x_new[-1]
        data[-3] = 2
        parameter.append(data)
        #df = pd.DataFrame(parameter)
        #df.to_csv('para.csv')
        return parameter
 
 
    # 功能：计算样条函数的系数。
    # 参数：parametes为方程的系数，y为要插值函数的因变量。
    # 返回值：三次插值函数的系数。
 
def solution_of_equation(parametes, x):
        size_of_Interval = len(x) - 1;
        result = np.zeros(size_of_Interval * 4)
        i = 1
        while i < size_of_Interval:
            result[(i - 1) * 2] = func(x[i])
            result[(i - 1) * 2 + 1] = func(x[i])
            i += 1
        result[(size_of_Interval - 1) * 2] = func(x[0])
        result[(size_of_Interval - 1) * 2 + 1] = func(x[-1])
        result[-2] = 5/13
        result[-1] = -5 / 13
        a = np.array(spline3_Parameters(x))
        b = np.array(result)
        #print(b)
        return np.linalg.solve(a, b)
 
 
    # 功能：根据所给参数，计算三次函数的函数值：
    # 参数:parameters为二次函数的系数，x为自变量
    # 返回值：为函数的因变量
def calculate(paremeters, x):
        result = []
        for data_x in x:
            result.append(
                paremeters[0] * data_x * data_x * data_x + paremeters[1] * data_x * data_x + paremeters[2] * data_x +
                paremeters[3])
        return result
 
x_init4 = np.arange(-5, 5.1, 1 )
result = solution_of_equation(spline3_Parameters(x_init4), x_init4)
#print(spline3_Parameters(x_init4))
#print(result)
x_axis4 = []
y_axis4 = []
for i in range(10):
    temp = np.arange(-5 + i, -4 + i, 0.01)
    x_axis4 = np.append(x_axis4, temp)
    y_axis4 = np.append(y_axis4, calculate(
        [result[4 * i], result[1 + 4 * i], result[2 + 4 * i], result[3 + 4 * i]], temp))
draw_pic('三次样条插值与原函数的对比图', x_axis4, y_axis4)
