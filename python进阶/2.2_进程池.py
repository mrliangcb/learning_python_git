#进程池
#进程池就是并行

import multiprocessing as mp
import time
def job(x):
	return x*x
	
def job1(x):
	return x*x
	
def multicore():
	pool=mp.Pool(processes=1)#试了用1核和4核运行，分别是0.5和0.45
	#其实多线程的意思是，先用核内部处理，等处理完了，在按顺序print，而不是谁先做完谁print
	res=pool.map(job,range(1000000))#放入方程和对应的输入值
	#print(res)
	
if __name__=='__main__':
	st=time.time() 
	multicore()
	st1=time.time()
	print('运行时间:',st1-st)
	
	
	
	
	
	
	
	
	