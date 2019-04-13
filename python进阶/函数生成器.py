#函数生成器


#为什么生成?
#调用range打印1到1亿的话，就会崩溃，因为一次性返回很大的数据，变量，爆内存  


#例子一
#(1) list_a=[x for i in range(1,10000)] #普通产生list

#(2)
list_b=(x for i in range(1,10000)) #生成器
print(type(list_b))

#(3)
#也可以自己写
#只要def函数中有yield，就跟生成器有关

def gene():
	yield 1 #有限队列不用while
	yield 2

ret=gene()
print(next(ret))#先取1，然后冻结状态
print(next(ret))#再次进入的时候，从冻结状态开始运行，然后再冻结
# print(next(ret))  再运行就报错了

print('\n关于b生成器\n')
def b(start,end):
	index=start
	while index <= end:#无限长度的队列，就用while
		yield index   #相当于生成器的return    相当于很多行yield 一次只执行一个yield，遇到下一个yield的时候就冻结，等下次调用才析出
		index+=1
		print('最后')

ret2=b(1,3)#设置一个迭代器 
for i in ret2:
	print(i)

print("测试是不是遇到yield就立马冻结")
#关于sent
# send fangfa he next方法类似，可以 触发！！ 生成器的下一个yield
print('\n关于c生成器\n')
def c(start):
	while start <10:
		print('yield之前')
		temp =yield start
		print('yield之后')
		print(temp)
		start+=1
ret3=c(4)
print(next(ret3)) #第一次碰到yield，立马冻结然后输出   运行4
print('第一条结束')
print(next(ret3)) #从冻结的yield下一条进入    运行5
print(next(ret3))  #运行6
print("next结束")
print('send输出',ret3.send('ziliao')) #先运行ret3.send，上次遇到yield start就冻结了，这次先temp='ziliao'，然后运行下面的  可以在外部传递值给生成器的yield，
#遇到下一个yield的时候，就立马冻结，就析出结果给到这里的print
#也可以传None

for i in ret3:#因为ret3里面的yield之前冻结了，现在从冻结处进入   运行7
	print(i)


# def gen():
	# print('进入')
	# yield 1
	# return 2
	# print('结尾')
# ret1=gen()
# next(ret1)
# next(ret1) #yield就最好不要用return，报错
