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


3.














