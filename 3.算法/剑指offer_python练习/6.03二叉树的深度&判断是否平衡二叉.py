
import time

# 二叉树的深度

# 如果一棵树只有一个节点，它的深度为1
# 用dept计算节点的深度
# 父亲的深度=max(左深，右深)+1

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


a=TreeNode(1)
b=TreeNode(2)
c=TreeNode(3)
d=TreeNode(4)
e=TreeNode(5)
f=TreeNode(6)
g=TreeNode(7)
h=TreeNode(8)

# 如何建立二叉搜索树
e.left=c
e.right=g

c.left=a
c.right=d

a.right=b

g.left=f
g.right=h


que=[e]
def prit(que): #按层打印
	#结束信号
	if len(que)<=0:
		return 
	#

	#递归体
	root=que.pop(0)
	print(root.val)
	if root.left!=None:
		que.append(root.left)
	if root.right!=None:
		que.append(root.right)
	prit(que)
	
prit(que)



# def depth(root):#求节点深度
	
	# if root.left!=None:#如果有左子树，则……  
		# ld=depth(root.left)#先求左深度
		
	# if root.right!=None:
		# rd=depth(root.right)#先求右深度
	
	# return max(ld,rd)+1


#下面换了一种结束方式,上面的缺点是 可能不存在ld，但下面这个一定有ld。
# 
dit={}



def depth(root):#求节点深度
	if root==None:#如果传入空，则返回0
		return 0


	ld=depth(root.left)#先求左深度，叶子节点则会传入一个None，获得0
	rd=depth(root.right)#先求右深度
	
	#求本节点深度
	dep=max(ld,rd)+1
	dit[root.left]=dep#计了就存字典
	return dep
	#也有一种写法return max(递归左，递归右)+1
	#但上面这种方法一般便于记录曾经计算过的节点
	#这里记录和不记录是一样的，因为这里没有重复计算东西
	
print(depth(e))

# 是否平衡二叉树
# 它首先要是排序树，搜索树
# 左右子树的高度差<=1


def isba(pRoot):
	if pRoot is None:#遇到叶子节点的孩子，返回True
		return True
	left = depth(pRoot.left)
	right = depth(pRoot.right)#计算深度
	diff = left - right #
	if diff< -1 or diff >1:#绝对值大于1的，返回false，否则继续搜索
		print(pRoot.val,left,right)
		return False #return代表止住，不继续搜索了
	
	return isba(pRoot.left) and isba(pRoot.right) #看一下孩子是否返回false

# s=time.time()
# for i in range(1000):
	# print(isba(e))
# t=time.time()
# print(t-s)
print(isba(e))







