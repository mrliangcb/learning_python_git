#python类实现矩阵乘法
import numpy as np
class mul:
	def __init__(self,a):
		self.a = a
		
	def shift_format(self,a,b):
		if len(a.shape)==1:
			a=a[np.newaxis,:]
		if len(b.shape)==1:b=b[np.newaxis,:]
		if len(a[0]) != len(b):a,b=b,a
		b_row,b_col=len(b),len(b[0])
		a_row,a_col=len(a),len(a[0])
		return a,b,a_row,a_col,b_row,b_col
	def dot(self,b):
		a,b,a_row,a_col,b_row,b_col=self.shift_format(self.a,b)
		result=np.zeros([a_row,b_col],int)
		for i in range(a_row):
			for j in range(b_col):
				for m in range(a_col):
					result[i,j]+=a[i,m]*b[m,j]
		return result
	
a=np.array([1,2,3])
b=np.array([[1,2,3],[4,5,6],[7,8,9]])#定义两个矩阵，可二维，可一维
a=mul(a)
print(a.dot(b))


