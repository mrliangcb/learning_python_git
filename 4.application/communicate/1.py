import socket

# 客户端需要多线程
import threading 

outString=''
inString=''
name=''


# ip地址
name=input('输入名字:')  #raw_input是py2的
ip=input('输入ip地址:')
print(name)

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #有tcp udp模式   默认   创建套接字
sock.connect((ip,8888))#ip和端口   
sock.send(name.encode())

# 多线程 要负责同时接收发送  并发
# 


def dealout(sock):
	global name,outString,inString  #想要修改一定要声明global
	while True:
		outString=input('发送什么:') #等待输入
		outString=name+':'+outString
		
		sock.send(outString.encode())#封装含有 源用户名  和内容  还有目的IP和端口 

def dealin(sock):#拿到sock，负责接收
	global inString
	while True:
		try:#异常处理，就是读不到东西，就重复继续循环检测，直到有东西
			
			inString=sock.recv(1024).decode()#等待接收信息
			if not inString:
				#空串
				print('收到空的')
				break
			if outString !=inString:#为什么  会收到自己说的话?
				print(inString) # 
		except:
			break 
			
			
thin=threading.Thread(target=dealin,args=(sock,))
thin.start()
thout=threading.Thread(target=dealout,args=(sock,))
thout.start()













