#类

class exa1():#顶层类，没有继承
	def __init__(self):#初始方法
		print('exa1_1')
	def fc():
		print('exa1_self_function')
		
		
class exa2(exa1):#继承了exa1类
	def __init__(self):#初始方法
		print('exa2_1')
	def fc():
		print('exa2_self_function')#初始化时没有运行这个
	
	
class exa3(exa1):#继承了exa1
	def __init__(self):#初始方法
		print('exa2_3')
	def fc(self):
		print('exa3_self_function')#初始化时没有运行这个
		exa1.fc()#调用继承了的类exa1中的方法(调用父类方法)

	
a=exa1()
b=exa2()
#因为继承了exa1，所以实例化时，运行exa1的初始方法，但如果自己也定义了init，就运行自己的
#为重写，优先考虑本地的初始方法

c=exa3()
c.fc()



class A:
	def __init__(self):
		print("5")
		print("6")
class B(A):
	def __init__(self):
		print("2")
		super(B, self).__init__()
		print("7")
class C(A):
	def __init__(self):
		print("3")
		super(C, self).__init__()#因为调用super()(B  C  D)的时候，A已经用过一次，之后都不调用,pass
		print("8")
class D(A):
	def __init__(self):
		print("4")
		super(D, self).__init__()
		print("9")
class E(B, C, D):
	def __init__(self):
		print("1")
		super(E, self).__init__()
		print("10")
E()
#调用顺序为1到10，横向 
# B  C  D 的super前
#B  C  D的super 内，但只调用一次，重复pass
#B  C  D 的super之后










