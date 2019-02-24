import numpy as np
import pandas as pd
path=r"C:\Users\mrliangcb\Desktop\note\extra_feature\open\labels.txt"
file = open(path)

a = file.readlines()#按行读取，作为字符型
print(a)
print('类型:\n',type(a))#list类型,每行读作一个str，为一个元素
print('第一行:\n',a[0])
print('第一行，第一个字符:\n',a[0][0])
print('第一行类型:\n',type(a[0]))#str

print('第一行str的长度',len(a[0]))
result=[]
for i in range(len(a[0])):
	result.append(a[0][i])
#c=np.array(result,dtype=int).reshape(-1,1)

#保存时用np
#np.savetxt(r'C:\Users\mrliangcb\Desktop\note\extra_feature\open\answer.txt',c,fmt='%d')#03d表示整数为3位，不够的话前面添0

#如果要保存为csv表格，用dataframe#字典创建
s=pd.DataFrame({'P1':[1,2,3],'P2':[1,2,3]})
print(s)









