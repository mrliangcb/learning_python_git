#reduce用法

from functools import reduce

a=[1,2,3,4,5]
print(a[-2:])

def haha(a,b):
	return (a+b)
	
b=reduce(haha,a) #a是一个可迭代的对象，是一个集和，有1到5，每次取两个出来计算，最终结果是一个数
print(b)
