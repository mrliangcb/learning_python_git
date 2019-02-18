#python类实现矩阵乘法
import numpy as np
class mul2:
	def __init__(self,a):#自己是a
		self.a = a
	def dott2(self,b):
		c=np.dot(self.a,b)#横乘以竖
		return c
	def multi2(self,b):
		c=np.multiply(self.a,b)
		return c
a=mul2(np.array([1,2,3]))

print(a.a)
print(a.multi2(np.array([[1,2,3],[4,5,6],[7,8,9]])))
		
#用a的时候，记住要self.a，表示自己的a

