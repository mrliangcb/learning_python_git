import numpy as np
#237
# 输入: head = [4,5,1,9], node = 5
# 输出: [4,1,9]

#1.给出要删除的节点
class ListNode:
	def __init__(self):
		self.v = None
		self.next = None
		
a=ListNode()
b=ListNode()
c=ListNode()
d=ListNode()

a.v=4
a.next=b

b.v=5
b.next=c

c.v=1
c.next=d

d.v=9




def dele(head,d_n):#要删除的d_n节点
	if not (head and d_n): return False
	
	i=d_n
	j=d_n.next
	
	if j!=None:   #如果d-n有下一个节点
		i.v=j.v   #把下一节点复制到此节点，然后删除下一节点
		i.next=j.next
		#只要没有东西指向j这个节点，到时候自动销毁回收
	
	elif i==head: #没有下节点，就直接删除这个节点。注意这种删除方法，如果有前节点，则前节点会连接一个空节点。所以这里只看没有前节点的情况
		
		head=None#一定要令头节点为空。节点为空和节点的next为空的区别
	else : #没有下节点，而且有前节点，也就是最尾节点
		#先找到父亲，然后断掉关系
		k=head
		while k.next!=i:
			k=k.next
		#现在K指着i的父亲
		k.next=None #主链完成
		
		
		i=None
		#使i=none就可以了，不用再让v，next分别=none，因为此时这个节点没有任何依赖，自己就消除了
		#当这个对象不再需要时，也就是说，这个对象的引用计数变为0时，它被垃圾回收。
		#也就是当走出这个函数的时候，局部变量都会销毁，全局变量只有主链的head，还有各个节点的next.
		# https://www.cnblogs.com/bigberg/p/7591463.html    内存分配问题
		
		#只要没有next指向一个节点，这个节点被0个指针指向，就会被销毁回收
		
		# i.v=None# 废弃点
		# i.next=None
	return head
# 2.给出要删除节点的值，
# 不是普通的从链表中删除节点，例如 1 3 4 5  删除4，就将3连接到5,34连接取消掉。但我们现在找到4 的时候，是得不到3的引用的，或者说不能同时获得3,5的引用
# 

head2=dele(a,c)


i=a
while i!=None:
	print(i.v)
	i=i.next

