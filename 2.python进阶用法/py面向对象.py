#面向对象

class person(object):
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
	
#动态添加方法1





#动态添加方法1
#动态添加方法1






