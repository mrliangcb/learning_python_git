#装饰器

#闭包:
#在一个函数中，定义另外一个函数2，而且2函数使用了1函数的变量
def a(name):   #a变量指向b函数
	print('进入第一层')
	def b(): #这个函数称为闭包
		print('名字:',name)
	return b #返回闭包
	

#result=a('123') #得到的不是b  ，函数里面还没运行，我们拿到的是指向(内)函数的指针
#result()#result获得b函数地址,result()  相当于b()

#非闭包的做法def op(a,b,operation)


# print(round(3/4,2))

def cal(option):
	if option==1:
		def add(x,y):  #x,y是自己的，不从cal拿来
			return x+y
		return add #不是运行了add才返回，函数其实还没有运行，但到这里表示add的地址，add()才表示运行函数
	elif option==2:
		def minus(x,y):
			return x-y
		return minus
	elif option==3:
		def mul(x,y):
			return x*y
		return mul
	else:
		print('出错')

ret=cal(1)#获得了add的地址   前面两个参数x,y其实没什么用
print(ret(2,2))  #相当于add(2,2)

mul=cal(3)
print(mul(2,3))



#nonlocal 关键字
# 全局变量，如果要修改就要global声明，如果def局部只拿来用，就不用global  
# 装饰器使用

user=True

def login_require(func):
	def wrapper():
		if user==False:
			func()
		else:
			print('使用者为true')

#写装饰器
@login_require
def edit_user(username):
	print('进入第一个函数')

# @login_requiere

login_require(edit_user)#等价wrapper函数
login_require(edit_user)('iliao')









