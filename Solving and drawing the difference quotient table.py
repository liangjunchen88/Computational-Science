
import matplotlib.pyplot as plt 
def fun(x,f):
    rows=len(x)        #行数
    cols=len(x)+1      #列数
    temp=[[0 for col in range(cols)] for row in range(rows)]
    
    for i in range(rows):
        temp[i][0]=x[i]
        temp[i][1]=f[i]
 
    for i in range(1,rows):
        for j in range(2,i+2):
            print(i,j )
            temp[i][j]=(temp[i][j-1]-temp[i-1][j-1])/(temp[i][0]-temp[i-j+1][0])
            
    print("差商表为")
    print(temp)
    
    
 
#==============================================================================
# x=[1,3,2]
# f=[1,2,-1]
#==============================================================================
x=[0,1,2,4]
f=[3,6,11,51]
plt.plot(x,f)
fun(x,f)
