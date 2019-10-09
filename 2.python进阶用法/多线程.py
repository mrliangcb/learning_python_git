



def demo1():
	for i in range(5):
		print(i)

def demo2():
	for i in range(6,10):
		print(i)


def main():
	demo1()
	demo2()


main()

import time
import threading as td



def say():
	for i in range(5):
		print('hw')
		time.sleep(1)
	

# for i in range(2):#相当于建立了两条线程
	# t=td.Thread(target=say)#建立一个线程
	# t.start()
	# while :
		# print()  可以创建一个while 监测并发中发生的事情












