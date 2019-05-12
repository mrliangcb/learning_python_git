# 5章.字符型str的相关操作

import numpy as np  
import pandas as pd  
import random  
import glob  
import os  



# 1.以str名称寻找变量
a=12
name='a'
c=eval(name)
print(c)  #此时c指向a地址

# 2.format用法
print('hello {:0>3}'.format(1))  
:.2f 保留小数点后两位  
:.2%百分比格式，且小数点后两位  
{:0>3}左边补0，直到整个数长度为3   <为右边补  
path=r'abc{0:05d}'.format(123)  

# 3. join用法  
print(' '.join('%5s' % classes[labels[j]] for j in range(4)))  
str.join()  

# 4.glob 输入路径，找到路子下（包括子子子目录）的文件  
path=r'.\extra_feature\nparray'  
tmp=glob.glob(r'{}\*.inkml'.format(path))  #返回的是一个['文件1全名','']
注意*是通配符，能替代任何长度和任何内容  
\*\*\*.inkml 表示搜索多级子目录  
for i in tmp:  #遍历每个文件全名i='全名1' 

# 5.listdir用法  
tmp2=os.listdir(path)#获得当前文件夹下所有文件名，注意不是全名 

# 6.replace用法  
str=r'abcdef'  
str=str.replace('abc','hahaha')#将str的'abc'换成后面的  


# 7.walk用法
file_dir=r'C:\Users\mrliangcb\Desktop\pyqt_test\result'
for root, dirs, files in os.walk(file_dir):
	#print(root) #当前目录路径  
	#print(dirs) #当前路径下所有子目录  
	print(files) #当前路径下所有非目录子文件  
name=int(files[0][0])

b=os.listdir(file_dir)

# 8.os用法
# os.getcwd()#当前脚本路径
# os.path.dirname(path)#取得path路径的父路径
# os.path.basename(path)#取得路径的最后一项

# 9.format和eval的结合
#如果要读s1  s2 s3 等等变量，如何遍历
# for i in range(1,4):
	# name='{}{}'.format('s',i)#拼成's1'  's2'
	# s=eval(name)#找到这个变量并返回
	# print(s)

# 10.find用法
a='conv2d'
print(a.find('v2d')) #若找到，则返回第一个字符所在位置，若没找到返回-1





