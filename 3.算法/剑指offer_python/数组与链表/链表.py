


class Node():
	def __init__(self,x):
		self.val=x # 成员都写在函数里
		self.next=None

a=Node('zhang')
b=Node('liang')
a.next=b

def prin_lianbiao(head):
	print(head.val)
	if head.next:
		prin_lianbiao(head.next)
		
print('打印整个链表:')
prin_lianbiao(a)
















