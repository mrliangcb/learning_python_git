#面向对象
import types

class person(object):
	country='china'
	def __init__(self,name):
		print('进入')
		print(name)#形参name
		self.name=name 
		
		
		
a=person('1号')

#动态添加属性1
a.age=18

#动态添加属性2
# setattr(a,"age",18)  对象，属性名，属性值

print(dir(a))

if hasattr(a,'age') :
	print('有这个属性1')
if hasattr(a,'agee') :
	print('有这个属性2')
	
	
#动态添加方法1  普通方法添加给实例(类没有)
#types.MethodType
def run(self,ab): #self不指向类，指向对象实例
	print('run',self.name)
	print('输出',ab)

p1=person('p1')
p1.run=types.MethodType(run,p1) #给p1对象绑定一个run方法,后面p1表示给run的self传入这个p1对象指针
print('加了一个run方法',dir(p1))
p1.run(12)

#动态添加方法2  方法添加给类
@classmethod #加了一个装饰器 
def walk(cls): #cls指向类
	print('类方法')
	print('调用一个类自己的属性:',cls.country)
	
person.walk=walk #person类的walk属性给了一个walk方法
person.walk()


#动态添加方法3  添加静态方法  与self无关 不指向任何东西
# @staticmethod
def jingtai():
	print('进入静态方法')
person.jingtai=jingtai
person.jingtai()

#动态删除属性和方法
#方法一
# del 对象.属性名
# delattr(对象，'属性名')

# __slots__魔术方法
#类里面定义
class testt():
	__slots__=('age','name')
	def __init__(self,name):
		self.name=name
ob1=testt('魔术方法')
ob1.age=18
# ob1.country='china' #因为设置了slots ，指定只有age name名字的属性才能绑定进来


###########   元类  ###########
# 一切东西都是对象
# 元类:创建类  type就是一个元类，因为可以产生任何类
# 类:创建对象
# 最高级元类

print('\n\n元类\n\n')
#其实类也是一种对象，只不过是比普通对象高级的高级对象

#动态创建类 python的优点
def creat_class(name):
	if name=='foo':
		class Foo(object):
			pass
		return Foo #返回一个类
	else:
		class Car():
			pass
		return Car
	
a=creat_class('Car')
print(a) #名字为Car的类   列举的方法建立
print(type(a))

#动态创建一个类，叫dynamic_class，继承object，有name和age属性    
dyn_class=type('dynamic_class',(object,),{'name':'lcb','age':24})
print(dyn_class.name)
ob2=dyn_class()
# 等价于
# class dynamic_class(object):
	# def __init__(self):
		# self.name=''
		# self.age=''
print('模板名称是什么',dyn_class) #类的名字叫什么，不是变量的名字
print(dyn_class.age.__class__)
print('上层类是什么',dyn_class.__class__)#
#所以 type  dyn  ob2  左边最高级

#对于普通的  
c=2
print(c.__class__) #是	int创建c的
print(c.__class__.__class__) #是type创建int的

# __metaclass__  ，原本创建 类 由type生成的对象，即元类是type，但是用了这个之后，就由这个生成

# class foo():
	# __metaclass__=1
	
# class foo2():
	# a=1
	
# print('加了metaclass:',foo.__class__)
# print('没加metaclass:',foo2.__class__)


#自定义元类  一般做框架使用元类
#方法一：函数形式  少用

def upper_attr(class_name,parent,class_attrs):  #Foo类变量，继承谁，类属性
	new_attrs = [ (k,v) for k,v in class_attrs.items() if not k.startswith("__") and not k.endswith("__")] #[[1,2],[3,4]]
	print('改大写',new_attrs)
	upper_attrs = dict((k.upper(),v) for k,v in new_attrs)
	
	print('进入元类')
	print(class_name)
	print(parent)
	print(class_attrs)
	return type(class_name,parent,upper_attrs)
	
class Foo(object,metaclass=upper_attr):#自定义一个类
	__metaclass__= upper_attr #这个函数返回的值，Foo指向他
	country = 'china' #类属性

ob3=Foo()
print(dir(Foo))

#方法一：类形式定义元类  常用
print('类形式定义元类')
class abc(type):
	def __new__(cls,class_name,parents,class_attrs): #cls指向类的
		new_attrs=[(k,v) for k,v in class_attrs.items() if not k.startswith("__") and not k.endswith("__") ]
		upper_attrs = dict((k.upper(),v) for k,v in new_attrs)
		print('怎样:',upper_attrs)
		return super(abc,cls).__new__(cls,class_name,parents,upper_attrs)
		
class person2(object,metaclass=abc):
	__metaclass__ = abc
	country = 'china'
print(person2.COUNTRY)













