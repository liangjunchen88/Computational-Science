#鸡兔同笼问题
str1 = input("请输入头的总数： ")
str2 = input("请输入脚的总数： ")
n = int(str1)
m = int(str2) 
from sympy import Symbol,solve,pprint
x = Symbol('x')
y = Symbol('y')
n = Symbol('n')
m = Symbol('m')
expr1 = x + y - n
expr2 =2*x+4*y- m
solution = solve((expr1,expr2),(x,y),dict=True)
chicken = solution[0][x].subs({n:35,m:94})
rabbits = solution[0][y].subs({n:35,m:94})
print(f'There are {chicken} chicken.')
print(f'There are {rabbits} rabbits.')
