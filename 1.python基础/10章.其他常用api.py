#



# 1.map的用法
# map(function, iterable, ...) 函数，一个或多个序列
# 法一：显函数
def square(x) :
	return x ** 2
a=[1,2,3,4,5]
print(list(map(square,a )))
# map格式的数据要用list()转换
# map 就是遍历后面的数组，然后逐个输入到square函数
# 
#法二：隐函数
list_1=[1, 2, 3, 4, 5]
result=map(lambda x: x ** 2,list_1 )
print(list(result))

#多个序列输入
a=[2, 4, 6, 8, 10]
b=[1, 3, 5, 7, 9]
result=map(lambda x, y: x + y,a,b )
print(list(result))

# 2.排序 .sort 和sorted()
# list_.sort()
a=[2,5,1]
# a.sort()
# print(a)

# a=sorted(a)
# print(a)


#3.apply用法
def test(m):
	if m>2:
		return True
	else:
		return False
# a=[1,2,3,4]
# a.apply(test)  #list 没有apply的属性
#nn.module类，pandas中df和series都有apply的属性，传入可迭代的序列，送给test函数

#3.assert
# assert print('assert用法')

#4.isinstance   常用于判断 该对象 是否 某种类型
class example():
	pass
a=example()
print(isinstance([3,'good',2],int))
print(isinstance([3],int))
print(isinstance(3,int))
print(isinstance(a,example))

# 5.reduce

from functools import reduce
a=[1,2,3,4,5]
print(a[-2:])
def haha(a,b):
	return (a+b)
b=reduce(haha,a) #a是一个可迭代的对象，是一个集和，有1到5，每次取两个出来计算，最终结果是一个数
print(b)


# 6.断点调试
# import pdb
# pdb.set_trace()#设置断点语句

# 7.





