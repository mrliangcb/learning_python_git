#2.进程
#windows中只能用multiprocessing模块
#getpid获得当前进程ID
#getppid获得父进程ID

#https://www.cnblogs.com/tom2ling/p/9025391.html 参考进程的方法

#多核就是并行，同时做两件事
#并发就是都请求运行，轮流进行，时间间隔短
#本文只是多任务并发，如果要并行就要进程池



#multiprocess用法
#建立进程，启动进程，join实现进程同步
import os 
from multiprocessing import Process
import multiprocessing as mp
import threading as td
import time
p_l = []
#子进程，写成一个函数
# def run_proc( name): 
	# print (r'Child process {} | {} Running'.format(name, os.getpid()))

#Process([group [, target [, name [, args [, kwargs]]]]])
	
# if __name__ == '__main__': 
	# print ('Parent process %s.' % os.getpid() )
	# for i in range( 5): #设置起点，退出了for循环之后，才分别进入子程序(若不用for循环写，就立即调用进程def函数)
		# p = Process( target = run_proc, args =(str(i),)) #args是传入参数,创建进程，实例化,必须有逗号
		# print('Process will start.')
		# p.start() #开始进程
		# p_l.append(p)
	# print('显示进程:',p_l)
	# p.join() #Join()是主程序等我这个进程执行完毕了，程序才往下走
	# print('Process end.')
#然后才进入子程序


#threting是多线程，仍然是单核

#multiprocessing 多进程
#多核处理
#正常情况下用单线程运行

def job1(q,a,b):
	print('{} | {}'.format(a,b))
	res=0
	for i in range(100000000):
		res+=i
	print('第二个搞定')
	q.put(res)
	
	
def job2(q,a,b):
	res1=0
	print('{} | {}'.format(a,b))#第一步进入这个
	res=a+b
	for i in range(100000000):
		res1+=i
	print('第一个搞定')
	q.put(res)
	
if __name__=='__main__':#多线程，核都要判断main
	#t1=td.Thread(target=job,args=('a','b'))
	st=time.time()
	
	
	
	q=mp.Queue()#建立一个队列
	p1=mp.Process(target=job1,args=(q,1,2))#就算这个核运行时间很长，下面那个运行时间短，但P2要等P1运行完了才动手，并不是并行的
	p2=mp.Process(target=job2,args=(q,2,3))#如果job(b)的话，要args=(q,)
	st1=time.time()
	print('normal time:',st1-st)
	
	#t1.start()
	p1.start()
	#t1.join()
	p1.join()
	p2.start()
	p2.join()#阻塞
	res1=q.get()#通过两次取
	res2=q.get()
	print(res1)
	print(res2)
	print('完成')






























