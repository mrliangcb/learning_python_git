
a=''
# while 1:
	# try:
		# a=input('输入:')
		# if not a:
			# print('没有东西')
		# else:
			# print('结果:',a)
	# except:
		# break
		
		
		
		
aa=''.encode()
print(aa)
a='lcb'
b='123'
c=b.encode()
d=c+a.encode()
print(d.decode())

import threading
con=threading.Condition() 
print(con.acquire())#可以获得

# con.wait()
# con.release()#
if con.acquire():#acquire等待开锁
	print('能够获得')
	con.notifyAll()
	print(con.acquire())
	con.release()
	print(con.acquire())
	con.wait()#在等待其他线程发出notify
	
	
# print(con.acquire())#con已经锁上了，等待他释放
