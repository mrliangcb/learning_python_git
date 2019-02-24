import pandas as pd
import numpy as np
import os

# a=np.array([[1,2,3]])
answer=2
ground_true=0

#df1=pd.DataFrame(a,columns=['imgID','ground_true','answer'])
#print(df1)
def mark_data(name,answer,ground_true,a,b,c):
	path=r'C:\Users\mrliangcb\Desktop\pyqt_test\result\{}.csv'.format('1')
	df1 = pd.read_csv(path,nrows=None)
	print(df1)
	row_now=df1.shape[0]
	print(df1.dtypes)#int64型
	da=np.array([[name,answer,ground_true,a,b,c]])
	df2=pd.DataFrame(da,columns=['name','answer','ground_true','que1','que2','que3'])
	df3=df1.append(df2)
	print(df3)
	df3.to_csv(path,sep=',',index=0)


	
def generate_data(refer):
	line_num=[]
	if refer==1:
		print('1进来:',refer)
		for i in range(20,68,4):
			if i>40:
				line_num.append([i,1,1,0])
			else :
				line_num.append([1,1,i,1])
		sample=np.array(line_num)
		np.random.shuffle(sample)
		
	if refer==2:
		print('2进来这里',refer)
		for i in range(-30,30,6):
			if i>0:
				line_num.append([i,2,2,0])
			else :
				line_num.append([2,2,i,1])
		sample=np.array(line_num)
		np.random.shuffle(sample)
		
	return sample
	
def get_data():
	a=generate_data(1)
	b=generate_data(2)
	results=np.vstack((a, b))
	result=pd.DataFrame(results,columns=['1','2','3','label'])
	result.to_csv(r'C:\Users\mrliangcb\Desktop\pyqt_test\result\image.csv',sep=',',index=0)
	return results