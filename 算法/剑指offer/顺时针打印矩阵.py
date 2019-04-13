#顺时针打印矩阵
import numpy as np
image = b=np.arange(0,16,1).reshape((4,4))
print('image:')
print(image)

row=len(image)#行数
collor=len(image[0])#列数
circle=int((min([row,collor])-1)/2+1)
print(circle)

for i in range(0,circle,1):
	#左向右打印
	for j in range(i,collor-i,1):
		print(image[i,j])
	#此时j=3
	#上往下打印
	for k in range(i+1,row-i,1):
		print(image[k,collor-1-i])
	#判断是否重复打印，右向左
	
	m=collor-i-2
	# print('i为:',i)
	# print('m为：',m)
	# print('行为：',row-i-1)
	# print('j为:',j)
	while (m>=i)and((row-i-1)!=i):
		
		print(image[row-i-1,m])
		m=m-1
	n=row-i-2
	while (n>i)and(collor-i-1!=i):
		print(image[n,i])
		n=n-1
		
	
	