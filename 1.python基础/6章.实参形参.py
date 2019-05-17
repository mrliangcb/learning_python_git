
def in_put(arr):
	print("传入:",arr)
	arr[0]=1

arr1=[0,1,2]
in_put(arr1)
print("是否有改变:",arr1)
#结论: (1)函数传入单变量的时候，函数内把这个值复制给新开辟的变量，进行操作，就不会影响到实参
#		(2)函数传入数组arr1的时候，其实是传入了arr1的首地址，函数是直接拿地址来用，不开辟新空间，所以函数内修改会影响实参数组arr1[]
#		(3)如果不想影响实参，则可以在函数内新建数组，然后再return



#局部和全局
test=1
def b():
	test=2
	print()
b()#如果函数内有test则用函数内的局部参，如果函数内没有的，就找全局的



print('\n \n')
a=3
import numpy as np

b=np.array([1,2,3,4])
def func():
	global a #声明这个a是全局的，不是形参
	print(a)
	b[3]=0#这里数组不用定义global，如果本函数没找到定义b，则从全局去找。这是数组和单个变量的区别
	a=2  #实参
	
	
print(func())
print(a)
print(b)


