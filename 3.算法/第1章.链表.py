#第1章.链表

# 1.
#链表的一个元素为node节点，内容有value和指针
class Node():
	def __init__(self,x):
		self.val=x # 成员都写在函数里
		self.next=None

# 2.
a=Node('zhang')
b=Node('liang')
a.next=b

def prin_lianbiao(head):
	print(head.val)
	if head.next:
		prin_lianbiao(head.next)
		
print('打印链表:')
prin_lianbiao(a)

# print(dir(a)) #查看有什么成员，方法















