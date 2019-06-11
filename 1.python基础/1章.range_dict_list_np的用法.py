
#一.range,dict,list,numpy 的用法


import numpy as np

#1.range
a=range(0,3,1)





#2.dict
student = {'小萌': '1001', '小智': '1002', '小强': '1003', '小明': '1004'}
# (1)根据value返求key
new_dict = {v : k for k, v in dict.items()}#将原字典翻转
new_dict ['1001']
print(idx_label.values())
print(idx_label.keys())

# (2)分离key,value
key=[]
value=[]
for i in dict.keys():#遍历坐标   不写.keys也行的
	key.append(i)
	value.append(dict[i])

#利用key做统计
#先遍历 一个可迭代的东西 称为item
# dic1[item]=dic1.get(item,0)+1 # 看看是否有item这个key，有的话拿出来，+1，送给原item这个key。如果没有，则0+1送给item新key
# list(dict.keys()) 把turble变成list
# dict.setdefault('runoob', None)  #看看有没有runoob，有就拿出来value，没有的话给该key赋值，并且显示出来



# 字典的遍历
# (1) for key in dict:  for key in a.keys():    遍历key
# (2) for value in a.values(): 遍历值
# (3)for kv in a.items():   key和值一起遍历


#3.list
#(1)如果list要看shape，就先转成np：np.array(*)然后再看shape)  type

#(2)建立短list:  b=[1,2,3]

#(3)建立长list:  d=np.arange(1,4,1).tolist()
#				d=list(range(0,10,1))
#(4)str转为list:  a=list('abc')

#(5)把str按照逗号为分隔符，分开后装到list  [i.split(',')[0] for i in lines]

#(6)增添元素
#.append()   .extend()
#.insert(1,'x')在1的位置增加上x
#两个list相加，尽量用append，没有额外用内存

#(7)排序
#lista.sort(reverse = True) #reverse = True 降序， reverse = False 升序（默认）。
# a[::-1] #相当于把list的顺序翻转
#(8)删除
a=np.array([1,2,3]).tolist()
a.remove(1)#删除一个元素1
print('删除元素:\n',a)
#while 0 in selected:
#	selected.remove(0) #删除多个元素1要用while
# print('pop返回:\n',a.pop(0))#默认是最后一个
# print('删除第0位置:\n',a)
# del a[:]   del a[0]

#(9)判断是否为空
abc=[]
print(len(abc))#=0就为空




#4.numpy

# (1)建立np

np.arange(1,4,1,dtype=np.int32)

np.linspace(0, 10, 1000)#0到10之间平均分成1000分

np.array([[1,2,3],
			[4,5,6],
			[7,8,9]],dtype=np.int)

#生成0矩阵
np.zeros(shape=(3,4))
# np.ones


#产生随机数(不重复，且整数)
b=np.arange(100,dtype=np.int)
a=np.random.choice(b,10)
#c2=c[a]#抽取list c的10个样本

e=np.arange(12,dtype=np.int32).reshape((3,4))
print('e是:\n',e)#reshape前，(12,)  后是(3,4)

e=e.transpose(1,0)#调换维度,也是转置  np.T也行的
print(e)
#b=np.expand_dims(a,axis=0)#增加维度
#c=np.squeeze(b)#删除维度为1的

# np.random.seed() #他不是单独使用的，与随机数生成的语句配合   1.如果数值相同的种子，生成的随机数是一样的  2,.对之后的程序生成随机数一直有作用
# np.random.randn(1, 5)
# 赋值问题 x=y,x[0,1]=3,于是y中的[0,1]也会被修改为3，因为x是取得y的首地址，于是x[0,1]是取得这个地址上的值
# x=y.copy() 这样x修改就不会影响到y

# (2)类型转换
#转化   np转list 一维才可以转
a=np.array([1,2,3])
b=a.tolist()
print(b)

# listh转array
print(np.array(b))

# (3)维度，变换
# #矩阵拼接
# #水平
# print np.hstack((a, b))
# print np.concatenate((a, b), axis=1)
# #垂直
# print np.vstack((a, b))
# print np.concatenate((a, b), axis=0)
a=np.array([[1,2,3],[1,2,3],[1,2,3]])
print(a.ravel())#不改变原a，返回一个一维的np

#复制扩展
#一维： 
a=np.array([0]) 
a=a.repeat(5)   #从[0] 扩展成[0 0 0 0 0]
# 二维:
a.repeat([3,2],axis=1) 


#np读取
#np.load()
#np.loadtxt(path,delimiter=',',dtype=str)逗号作为分隔，要不然逗号也含在[]里，如果文件本身的类型是str
# print('第一行:\n',a[0])
# print('第一行，第一个字符:\n',a[0][0])
# print('第一行类型:\n',type(a[0]))#str

# print('第一行str的长度',len(a[0]))
# result=[]
# for i in range(len(a[0])):
	# result.append(a[0][i])


#保存
#np.savetxt('answer.txt',矩阵,fmt='%d')#保存的数据是整形的
#03d表示整数为3位，不够的话前面添0
#03d表示整数为3位，不够的话前面添0

# print()

#乱行序
np.random.shuffle(sample)


#类型转换np.astype(np.float32)
#float(*)
#.float()
#list: 

#x=np.zeros((,),dtype=np.float32)
#如果给这个矩阵赋float64的数据，最终x.dtype还是float32


#np和for 
#a=[[1,2,3],[4,5,6],[7,8,9]]
#f=[i for i in a]  #遍历处理的东西，放回list中，for和list.append融合的高效写法

#矩阵转置
#

#乱序方法

import random

random.shuffle(list)#直接打乱，洗牌
random.sample(indexList, 5)#打乱，然后抽样5个，不重复


#打包遍历for 
#主要用于绑定图片和对应的label
#queue=[]
#for data,label in zip(list1,list2)
	#queue.append((data,label))
#然后shuffle，data和label依然对的上

#第二种打包
# >>>seq = ['one', 'two', 'three']
# >>> for i, element in enumerate(seq):
# ...     print i, element
# 0 one
# 1 two
# 2 three

# 计算相关  可以输入list或者np矩阵
#np乘法
np.dot()  横乘以竖
np.multiply()  对应相乘
np.mean()  #axis=0第0维度，如果是二维的话，就是行之间的平均   =1
或者array.mean()

#矩阵转置
array.T
常用np.dot(a,b.T)，序列求乘积的和

# np.sqrt() 根号  
# np.square = array**2 求平方
# 

#两个列表打包一起乱序
import random
c = list(zip(a, b))
random.shuffle(c)
a[:], b[:] = zip(*c)

#统计np
np.bincount(x)  #各种数字出现多少次  序列样本，转化为次数
np.argsort(x)  #次数转化为排序
np.max() #求最大值
np.argmax()  #求最大值对应的索引












