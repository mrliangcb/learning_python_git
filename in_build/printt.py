# print

import sys,time
# for i in range(20):
	# print(i,end='',flush=True) #光标下一个
	# time.sleep(0.4)


for i in range(10):
	time.sleep(0.8)
	print('\r',str(10-i).ljust(10),end='')  #\r回到最新的位置，然后把之前的内容删除，再输出新的
	









