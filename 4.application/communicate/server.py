

import socket
import threading

# 同步机制  锁
# ip地址 127.0.0.1


# condition
con=threading.Condition()  

host=input('服务器ip:')
port=8888
data=''
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('建立套接字')

def clientin(conn,name):
	global data
	while True:
		try:#尝试等待接收，如果有哪个用户断掉，这里就抛出错误
			temp=conn.recv(1024).decode()#有其中一个客户端说话了  conn包含了至多5个客人 收到的是encode   解码之后就是str类型
			#这个是会等待的，如果其中一个客户强制退出 conn会一直错误
			
			print('收到:',temp)
			
			if not temp:#接收到 空字符 说明大家要结束了
				conn.close()#关掉连接，大家都不说话
				return #返回空
			NotifyAll(temp)#有一个人说话，那就修改这个变量，要等这个变量修改完了，其他人(线程)才能改
		except:
			NotifyAll((name+'离开了')) #有一个人走了，那就结束掉他的两个线程
			
			# print('结束',data)
			return #return 可以起到关闭线程的作用
		
def clientout(conn,name):
	global data
	while True:
		if con.acquire():#可以获得锁 如果不能，就等待   con是多线程锁
			con.wait() #等待锁的激活
			
			if data:#有东西
				try:#尝试等待收东西，如果conn不存在，就是那个用于已经退出了
					conn.send(data.encode())
					con.release()
				except:
					print(name,'退出out')
					con.release()#释放这个锁
					return 
			
			

		
		
def NotifyAll(ss):
	global data
	if con.acquire():#获得锁
		data=ss#修改数据data
		con.notifyAll()#唤醒所有等待这个锁的线程
		con.release()#这个release会影响clientout 


s.bind((host,port))

s.listen(5)#监听  最大5个人连接

print('在监听:')

while True:
	print('等待进来:')
	conn,addr=s.accept()#自己IP，还有对方地址   这个主线程等待新人进来
	
	print('与这个链接:'+addr[0]+':'+str(addr[1]))#
	name=conn.recv(1024).decode() #获取用户名 需要解码 服务端主线程等待握手
	NotifyAll(name+'进来了')
	print('数据是:',data)
	print('当前线程数:',threading.activeCount()+1)
	print('当前线程:',str((threading.activeCount()+1)/2)+'个用户在连接')#一个人是创建两个线程
	conn.send(data.encode())
	threading.Thread(target=clientin,args=(conn,name)).start()
	threading.Thread(target=clientout,args=(conn,name)).start()
	







