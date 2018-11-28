#等高线
import numpy as np
import matplotlib.pyplot as plt

def f(x,y):#计算高度
	return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n=256
x=np.linspace(-3,3,n)
y=np.linspace(-3,3,n)
X,Y=np.meshgrid(x,y)

plt.contourf(X,Y,f(X,Y),8,alpha=0.75,cmap=plt.cm.hot)#填充颜色,8是,alpha透明度,cmap对应颜色
#hot,cool,Blues,accent#8是等高线分成10部分，0分成2部分

#上面是等高图，下面等高线
C=plt.contour(X,Y,f(X,Y),8,colors='black',linewidth=0.5)

#增加label
plt.clabel(C,inline=True,fontsize=10)#画在线里面

plt.xticks(())
plt.yticks(())
plt.show()