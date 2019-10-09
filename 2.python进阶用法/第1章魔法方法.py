#魔术方法

#所谓的魔法方法，就是python类中的特殊方法
#例如:(1)__init__  (2)__iter__ (3)__next__ (4)__len__ (5) __new__等等 
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

print('***************************  __new__ 的使用   ********************************')

class small():
	def __init__(self):
		print('创建small类')

class MusicPlayer(object):
	# def __new__(cls,*args, **kwargs):#没有这个args kwargs也是可以的   cls装着是MusicPlayer类这个对象   class类型的
	def __new__(cls):   #这三个参数有什么用   类调用new的时候，会给new优先传一个参，表示这个内的引用
		# 1.创建对象时，new方法会被自动调用
		print("创建对象，分配空间")#通过new创建了一个空对象 也就是None  
		
		print('cls值:类',cls)
		#instance = super().__new__(cls) # 对象空间在内存的地址，传入   用继承的类来做实例化
		instance = small().__new__(cls)#如果建立small的，等下交给init的就是small了
		#如果用其他类 object.__new__()
		
		return instance
		
	def __init__(self):#self指向一个空间
		
		print("初始化播放器")#没有instance的时候，没有传入self，这里就不会运行。没有运行init  因为没有对象的引用self
		
# 创建播放器对象
player = MusicPlayer() #
print(player)  #这个等于self  
print(MusicPlayer)#这个跟上面的cls是一样的   cls指的是类  self指的是实例化的对象

# args指的是元组()  *args 就是把这个元组打散   *不是指针 python没有指针
a=(1,2,3)
print(*a)
# 在函数的参数里引用
def test(*a):  #意思就是有一个a元组()，打散了就是我现在输入的1,2,3   如果输入[1,2,3]那只有一个单位，不是三个
	print(a)
test(1,2,3)

def test2(a,*b):
	print('a:',a)
	print('b:',b)
test2(1,2,3,4) #1给a，其他的给b

# **kwargs  是一个字典，用**来打散     'a':2,'b':1  等价于a=2,b=1
def test3(**a):
	print(a)
	# for k, v in a.items():
test3(m=2,n=3)

def test4(a=0,b=0,c=0):
	print(a,b,c)
	
dic={'a':2,'b':10,'c':11}# 打散之后变成a=2,b=10,c=11
test4(**dic)

# 通常*args,和**kwargs



