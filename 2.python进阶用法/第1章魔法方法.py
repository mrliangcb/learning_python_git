#魔术方法

#所谓的魔法方法，就是python类中的特殊方法
#例如:(1)__init__  (2)__iter__ (3)__next__ (4)__len__等等 
# 这里 iter引入类的迭代器

#可以用for循环遍历的，叫做可迭代对象  list tuple dict set  str
#生成器也是可迭代的
#一个可迭代对象，是有__iter__方法的,并且会返回一个迭代器对象
# isinstance()是否是可迭代对象
# from collection import Iterable

class iteration():
	def __init__(self,start,stop):#self对象专属方法
		self.value=start-1  #self对象私有属性
		self.stop = stop
		print("初始化")
	
	def __iter__(self):
		print('进入迭代')
		return self #返回自己这个对象，只有遍历的第一次才会进入这里，之后每次都进入next
	
	def __next__(self):
		print("进入next")
		if self.value == self.stop:
			raise StopIteration #遍历到末尾就停止
		self.value += 1
		return self.value ** 2
	def __len__(self):
		print ("进入 __len__")
		return 1

test=iteration(1,4) #这里只运行init方法
len(test)




for i in test:
	print("遍历结果:",i)
#第一次进入迭代，就运行iter，然后再运行next一次

#机器学习的队列迭代读取
#(1) : 输入队列list
#(2) : 设置次数标志位i，每遍历一次就读取[i:i+batch_size]的数据
#(3) : 

# b=[1,2,3]
# print(isinstance(b,Iterable))


class test():
	def __call__(self,num):
		print(num)

a=test()('beautiful')# 调用call
b=test()
b('beautiful')














