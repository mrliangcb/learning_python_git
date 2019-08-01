#python中基础数据结构


# python的基础数据结构  list dict set tuple set queue
# 参考: 
# https://blog.csdn.net/qq_28304687/article/details/79088491 
#https://blog.csdn.net/liangguohuan/article/details/7088265

class Node():
	def __init__(self,x):
		self.val=x # 成员都写在函数里
		self.next=None

# (1)list
# list是线性表，按照位置索引o1,插入删除，按值搜索都是On  排序nlogn    
b=[1,2,3]
print(b.pop()) #pop(0)从栈底取出  
print(b)

a=Node(1)
list_a=[]
list_a.append(a)#queue也能存放节点
print(list_a)
list_a.pop(0)
print(list_a) 


# (2)dict
# dict是哈希表，根据Key查找value，时间复杂度o1

# 搜索
a={'a':'b'} #检查b在Key中有出现吗，不是value
print('b' in a) #False



# (3) set
#set 的查找和add也是o1的，哈希结构,搜索是与list最大的不同
# 具体看(数据结构基础)中(set应用)

# (4) deque
# deque 双向队列，搜索为ON 
import collections
queue=collections.deque()
queue.append(a)

print(len(a))
print('deque放入了什么:',queue)



#基础算法复杂度
# sorted(list)
# 2^x=len
# x=log2(n)

# (5)树节点
class Node:
	def __init__(self,val):
		self.val = val
		self.left,self.right=None,None



# (6)链表
#链表的一个元素为node节点，内容有value和指针 。树有左右孩子，链表只有一个孩子  
class Node():
	def __init__(self,x):
		self.val=x # 成员都写在函数里
		self.next=None 





























