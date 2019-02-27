#iterator


class iteration():
	def __init__(self,start,stop):#self对象专属方法
		self.value=start-1  #self对象私有属性
		self.stop = stop
		print("初始化")
	
	def __iter__(self):
		print('进入迭代')
		return self #返回自己这个对象
	
	def __next__(self):
		print("进入next")
		if self.value == self.stop:
			raise StopIteration #遍历到末尾就停止
		self.value += 1
		return self.value ** 2

test=iteration(1,4) #这里只运行init方法
for i in test:
	print("遍历结果:",i)
#第一次进入迭代，就运行iter，然后再运行next一次

#机器学习的队列迭代读取
#(1) : 输入队列list
#(2) : 设置次数标志位i，每遍历一次就读取[i:i+batch_size]的数据
#(3) : 












