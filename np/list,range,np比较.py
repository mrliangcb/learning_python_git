import numpy as np


##一、py
a=range(0,3,1)
print(a)#range类型1到3
print(type(a))
读取
file = open(path)
a = file.readlines()#按行读取，作为字符型
a=[[一行],[二行],['1','2']]#,为分隔符

#求最大
#max(list[]),min(list[])




##二、字典
student = {'小萌': '1001', '小智': '1002', '小强': '1003', '小明': '1004'}
#根据value返求key
new_dict = {v : k for k, v in dict.items()}#将原字典翻转
new_dict ['1001']

#分离key和value
key=[]
value=[]
for i in dict.keys():#遍历坐标
	key.append(i)
	value.append(dict[i])



##三、list

#如果list要看shape，就先转成np：np.array(*)然后再看shape
b=[1,2,3]
print(b)
print(type(b))

d=np.arange(1,4,1).tolist()
print('\n一次创建多位list:\n',d)

a=list('abc')
print('产生list 的str:\n',a)

#把str按照逗号为分隔符，分开后装到list
[i.split(',')[0] for i in lines]

#增加
#.append()   .extend()
#.insert(1,'x')在1的位置增加上x
#两个list相加，尽量用append，没有额外用内存


#排序
#lista.sort(reverse = True) #reverse = True 降序， reverse = False 升序（默认）。

#numpy.sort(a, axis=1, kind='quicksort', order=None)

#

#删除
a=np.array([1,2,3]).tolist()
a.remove(1) #删除value=1的
print('删除元素:\n',a)
#while 0 in selected:
#	selected.remove(0)

# print('pop返回:\n',a.pop(0))#默认是最后一个
# print('删除第0位置:\n',a)

del a[:]#长度减少了
print('删除a[0]:\n',a)



#四、numpy

np.linspace(0, 10, 1000)
#0到10之间分成1000份

c=np.array([[1,2,3],
	           [4,5,6],
	           [7,8,9]],dtype=np.int)
print('\nc是:\n',c)

d=np.arange(12,20,2,dtype=np.int32)
print('\nd是:\n',d)

d=np.arange(12)
print('只产生12个数\n',d)

a=np.zeros(shape=(3,4))
print('0矩阵：\n',a)

#np.ones

#产生随机数




e=np.arange(12,dtype=np.int32).reshape((3,4))
print('e是:\n',e)#reshape前，(12,)  后是(3,4)

e=e.transpose(1,0)#调换维度
print(e)
#b=np.expand_dims(a,axis=0)#增加维度
#c=np.squeeze(b)#删除维度为1的










#转化   np转list 一维才可以转
a=np.array([1,2,3])
b=a.tolist()
print(b)



# listh转array
print(np.array(b))







# #矩阵拼接
# #水平
# print np.hstack((a, b))
# print np.concatenate((a, b), axis=1)
# #垂直
# print np.vstack((a, b))
# print np.concatenate((a, b), axis=0)
a=np.array([[1,2,3],[1,2,3],[1,2,3]])
print(a.ravel())#不改变原a，返回一个一维的np


#np读取
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

# print()

#乱行序
np.random.shuffle(sample)


#类型转换.astype(np.float32)
