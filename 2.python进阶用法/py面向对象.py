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


#动态添加方法3  添加静态方法








