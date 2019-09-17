
# 给定二叉搜索树
# 从小到大，第K个数是多少
# 可以用中序遍历，   中序遍历搜索树就得出（从左到右，从小到大）的序列

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

# 注意嵌套函数和非嵌套(下面)写法
# 

class Solution:
	# 返回对应节点TreeNode
	def KNode(self, pRoot, k):
		# write code here
		if not pRoot or k<=0:
			return None
		self.res=[]
		self.inorder(pRoot)#这里进入函数,pRoot是Knode的
		if len(self.res)<k:
			return None
		return self.res[k-1]
		
		
	def inorder(self,pRoot):
		if not pRoot:
			return []
		self.inorder(pRoot.left)
		self.res.append(pRoot)
		self.inorder(pRoot.right)
			
		

test=Solution()
an=test.KNode(e,3)
print(an.val)















