#2.4并行池


from multiprocessing import Pool
import os, time, random 

def run_task(name): 
	print('Task %s (pid = %s) is running...' % (name, os.getpid()))
	time.sleep( random.random() * 3) 
	print('Task %s end.' % name )

#并行任务1
def task0():
	time.sleep(1)
	print('我是任务0')
	 
def task1():
	time.sleep(2.5) 
	print('我是任务1')
	
def task2():
	print('我是任务2')

def task3():
	print('我是任务3')

#引导并行任务的函数
def para_task(a):#最先出现2和3任务，然后出现0，最后1，所以他们是并行的
	if a==0:
		task0()
	elif a==1:
		task1()
	elif a==2:
		task2()
	elif a==3:
		task3()
	
	
if __name__=='__main__': 
	print ('Current process %s.'% os.getpid())
	p = Pool( processes = 4) 
	
	for i in range(4): 
	#并行的执行5个程序，分别传入5个初始值。
	#所以自定义run任务的时候，里面可以放很多子任务，接收输入值然后就，分别运行几个子任务
	#i是并行任务的标号选择
		p.apply_async(para_task, args =( i,)) 
	print('Waiting for all subprocesses done...') 
	p.close() #join之前要先close
	p.join() 
	print('All subprocesses done.')


