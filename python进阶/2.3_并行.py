#3.并行

import multiprocessing as mp
import time
import numpy as np

def job(v,num,l,flag):
	l.acquire()#获得锁
	
	for _ in range(10):
		print(flag)
		if flag=='进入1':
			time.sleep(0.1)
		else:
			time.sleep(0.2)
		v.value+=num#两个process抢共享内存 v是地址  v.value是这个地址存的值
		print(v.value)
	l.release()#释放前，进程2 在等着写入第一次，这时候进程1在做10次循环，完成之后，释放锁，此时进程2就可以写入了，然后进程2循环
	#如果没加锁，进程1,2就会瞬时抢共享变量写入
	
def multicore():
	l=mp.Lock()#设置一个锁
	v=mp.Value('i',0)#设置一个共享内存
	#这种方式手动设置进程
	p1=mp.Process(target=job,args=(v,1,l,'进入1'))
	p2=mp.Process(target=job,args=(v,3,l,'进入2'))#这两个是并行的，交替出现结果,而且1的时间短，2的时间长，这里就很明显并行了
	p1.start()
	p2.start()
	p1.join()
	p2.join()
	print('并行任务结束')

if __name__=='__main__':
	multicore()
	print('主任务结束')

#还有pool.map  pool.apply

