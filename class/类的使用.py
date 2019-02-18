#https://blog.csdn.net/Marksinoberg/article/details/69482397
import numpy as np
class BinaryTree:
	def __init__(self,rootObj=None):#儿子的，一创建运行，=Binary(rootobj)  self只是声明这个是对象自己的，就像c++的非static   无self=static
		self.key = rootObj#(参数给这里)  __私有变量，只能内部访问，外部只能通过公有方法访问,例如__a():为私有，a()为公有
		self.leftChild = None #相当于声明一个私有属性，懂得用none,可以在普通def函数里面写self.私有变量，不一定这里
		self.rightChild = None 
		
	#上面是儿子的数字，下面是儿子的工具箱
	def insertLeft(self,newNode):  #也是儿子的 儿子名.insertLeft调用
		if self.leftChild == None: #如果这个大儿子左边没有儿子  a=binary(b) binary叫爸爸，a叫大儿子，b是小儿子
			self.leftChild = BinaryTree(newNode) #就给大儿子的左边起一棵树，名字是参数
		else: #如果大儿子左边有小儿子
			t = BinaryTree(newNode)#则t取得新儿子
			t.leftChild = self.leftChild#大儿子的左儿子给新儿子的左边
			self.leftChild = t#当然，新儿子就成为了大儿子的左儿子
		self.takename()#调用内类函数用self, self指的是对象的takename()函数
		
	def insertRight(self,newNode): #有self指的是非静态方法，是属于对象的，无self是属于类的
		if self.rightChild == None:
			self.rightChild = BinaryTree(newNode)#有点递归的感觉
		else:
			t = BinaryTree(newNode)
			t.rightChild = self.rightChild
			self.rightChild = t


	def getRightChild(self):
		return self.rightChild

	def getLeftChild(self):
		return self.leftChild

	def setRootVal(self,obj):
		self.key = obj

	def getRootVal(self):
		return self.key
	def takename(self):
		print("转入类内函数")

#def __init__(self,rootObj=None) 其实r对应于self，'boy1'对应于rootObj
r=BinaryTree('boy1')
y=BinaryTree('boy3')
print(r.getRootVal())#其实直接r.key也是可以的
r.insertLeft('boy2')
print(r.getLeftChild().getRootVal())#递归取实例方法
print(type(r))
print(len(dir(r))) #有35个属性
r.key2=12#给r实例增加了一个属性
print(len(dir(r)))#现在有36个属性了，私有
print(len(dir(r.leftChild)))#大儿子的左儿子，也只有35个属性


beau=[]
beau.append(r)
beau.append(y)
print(beau) #把节点放到一维矩阵里

#r=y #树可以赋值
#print(r.key)
r,y=y,r#互换
print(r.key)


#调用父类
#https://www.cnblogs.com/kongk/p/8644745.html
