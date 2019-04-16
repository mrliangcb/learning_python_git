#生成器应用

#斐波拉

#[ 0,1,a+b, ,    ]
#  a,b
#先用a,b指向前面两个

#普通做法
que=[0,1]
for i in range(10):
	a=i
	b=i+1
	que.append(que[a]+que[b])
print(que)


#普通函数做法
fib2=[0,1]
def fib(count):
	index=1
	a,b=0,1
	while index<=count:
		a,b=b,a+b #这里前后位置换了也是ok的  b指向了下一个a,也是指向了下一个
		fib2.append(b)
		index+=1
fib(10)
print(fib2)


#多个变量同时赋值
# a=1
# b=2
# a,b=b,a
# print(a,b)

#生成器做法

def music(time_all):
	time=0
	while time<=time_all:
		print('在听歌')
		time+=1
		yield None
	raise StopIteration() #运行完就抛出一个异常
	
def movie(time_all):
	time=0
	while time<=time_all:
		print('在看电影')
		time+=1
		yield None
	raise StopIteration()
	
def main():
	op1=music(10) #你走一步，然后到他走一步
	op2=movie(20)
	stop_music=0
	stop_movie=0
	while 1:
		try:
			next(op1)
		except StopIteration:
			print('音乐完了')
			stop_music=1
		try:
			next(op2)
		except StopIteration:
			print('电影看完了')#当音乐完了，电影没完的时候，音乐每次都抛出exception
			stop_movie=1
		if stop_movie and stop_music:
			break
			
main()

#单核cpu模拟多任务，一人走一步
#那如何多核呢
















