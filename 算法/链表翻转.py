#

class Node():
	def __init__(self,x):
		self.val=x # 成员都写在函数里
		self.next=None
	
#链表翻转
def reverseList(self,head):
	cur,prev=head,None#进来站在原第一个位置
	while cur:
		cur.next,prev,cur=prev,cur,cur.next #理解为窗口移动
	return prev

#交换相邻元素
def swapPairs(self,head):#self是排好的结果给他
	pre,pre.next=self,head #一开始站在1的位置，等号右边是原位置，等号左边是后来位置
	while pre.next and pre.next.next:
		a=pre.next
		b=a.next
		pre.next,b.next,a.next=b,a,b.next
		pre=a
	return self.next

	
set结构
看一下链中有没有环
（1）末尾有null，则没环  所以ON  硬算
(2)每走一下就用set存起来，走过的地址都记录下来，都有味道，搜索下一个点的时候，去set查找有没有重复 判重  on
(3)快慢指针，慢每次加1，快每次加2，只要有环，快指针都会再次追上慢指针  on
(4)

def hasCycle(self,head):
	fast=slow=head#初始化指针
	while slow and fast and fast.next:#走在前面的有可能是快或者慢指针
		fast=fast.next.next
		if slow is fast: #==
			return True
	return False
	
	下面是三个步骤的四意图
	a,b   b a        a  ,  b
	pre       pre   pre
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

