#第3章，二叉树/图

class Tree:
	def __init__(self,rootObj=None):
		self.key = rootObj
		self.leftChild = None 
		self.rightChild = None
class Node:
	def __init__(self,val):
		self.val = val
		self.left,self.right=None,None
		
#分层打印
#双向二叉树就是图  
# 左子树和右子树和全局根节点比较，根节点的左边子树的所有节点都要比他大或者小
#容易查找

# 98
   # 3                  5
 # 1     5            1    4
  # 2                     3  6

#1.中序遍历  左，根 ，右    array升序
# 递归  判断next是否为空，非空则递归 
# 

#中序遍历
a=Node(3)
b=Node(1)
a.left=b
c=Node(4)
d=Node(4)

#中序编列记住所有节点
def test(root):
	inorder2=inorder(root)
	return inorder2==list(sorted(set(inorder)))
	
def inorder(root):
	if root is None:
		return []
	return inorder(root.left)+[root.val]+inorder(root.right)


#中序遍历记住前继结点
def test2(root):
	prev=None
	return helper(root)
def helper(root):
	if root is None:#这个点不是底
		return True
	if not helper(root.left): #
		return False
	if prev and prev.val>=root.val:#如果上一个非空和上一个内容，大于本节点的，就错了
		return False
	prev=root#prev指针指向本节点
	return helper(root.right)#查右边

#递归 98题
def isValid(root,min,max):#下界上界
	if root==None :return True#到了端点就会返回True，如果一开始就给none呢
	if (min!=None and root.val<=min) :return False
	if (max !=None and root.val>=max) :return False
	return isValid(root.left,min,root.val)and isValid(root.right,root.val,max);
#检查左右子树
print(isValid(a,0,4))
#对于

#235.236题
#最近公共祖先
#               6
        # 2            8
      # 0   4        7    9
        # 3   5
#
#
#递归 遍历树一次  
#基于非搜索树
def treeNode(root,p,q):
	if(root==null or root==p or root==q): return root
	left=treeNode(root.left,p,q)
	right=treeNode(root.right,p,q)
	if left==None:
		return right
	else:
		if right == None:
			return left
		else:
			return root
			
#最近公共祖先，二叉搜索树
def lowCommon(root,p,q):
	if p.val<root.val>q.val:
		return self.lowCommon(root.left,p,q)
	if p.val> root.val<q.val:#还没到
		return self.lowCommon(root.right,p,q)
	return root
	
#非递归写法(逻辑上，复杂度都跟上面递归一样的)
def lowCommon2(root,p,q):
	while root:#只要还没到端点
		if p.val<root.val>q.val:
			root=root.left
		elif p.val>root.val<q.val:
			root=root.right
		else:
			return root
			
#先学会巡底  程序看上去是自上而下，但真正思考是自下而上的，所以研究树还是从结尾点开始思考
# def sample(root):
	# if root为底：
		# 做判断
		# return 
	# else:还没到底
		# 就递归找底

# 二叉树遍历  
# 前序pre order   in order中序  后序post order
#深度优先，广度优先 搜索树  用的比较多

#前序遍历
traverse_path=[]
def preorder(root):
	if root:
		traverse_path.append(root.val)  #
		preorder(root.left)
		preorder(root.right)

#中序遍历
def inorder(root):
	if root:
		inorder(root.left)#先访问所有点的左子树,在这么多左子树之中，最下面的先进来
		traverse_path.append(root.val) #然后到中
		inorder(root.right) #最后访问右子树
#当遇到端点的时候，相当于返回None

# 递归循环  
# n!=1*2*3*4*5 
def compu(n):
	if n<=1:return 1#触底，阻断下面的
	return compu(n-1)*n  

#最开始是想到下面这个
# def compu(n):
	# compu(n-1)

#分治 divde conquer   先解决小问题再解决大问题



# 50   x=2 n=10  2^10=1024
# (1)pow(x,n)    o1
#  (2)暴力 on   x乘以自己N次
#  (3)分治办法 先获得一半的相乘，然后结果相乘   节省了一半的递归 偶数情况：y=2^int(n/2)   y*y   奇数：y=2^int(n/2)   y*y*x
#  更加高效是，2/n又分一半   可以看n可以分多少次一半2^x=n x=logx(n) 这么多次操作   比上面更少复杂度

def myPow(x,n):
	if not n:
		return 1
	if n<0:
		return 1/myPow(x,-n)
	if n%2: #奇数
		return x*myPow(x,n-1)
	return myPow(x*x,n/2)
#10(1/2)^x=1  10一直分，直到分到一个元素

#非递归
def myPow2(x,n):
	if n<0:
		x=1/x
		n=-n
	pow=1
	while n:
		if n&1:
			pow *=x
		x+=x  
		n>>=1 #位运算
	return pow

# graph
#广度优先搜索  BFS  先写出第一层的，再写第二层的
# 判重set
visited = set()
def BFS(graph,start,end):
	queue=[]
	queue.append([start])
	visited.add(start)#一个set  这个节点已经被访问过了   判重
	while queue:
		node=queue.pop()
		visited.add(node)
		process(node)
		nodes=generate_related_nodes(node)
		queue.push(nodes)
		
		





#深度优先搜索  DFS  先找其中一个分支，一直找到底
visited = set()
def dfs(node,visited):
	visited.add(node)  #用栈存节点
	for next_node in node.children():
		if not next_node in visited:
			dfs(next_node,visited)   #传递栈


# 102题 二叉树遍历  按层
#（1）bfs   把每层元素加入到队列
#           batch处理 最佳
# (2)  dfs   每次循环记得深度

a=Node(1)
b=Node(2)
a.left=b
c=Node(3)
a.right=c
d=Node(4)
c.left=d
e=Node(5)
c.right=e
#下面是bfs算法
import collections
def levelOrder(root):
	if not root:return []
	result=[]
	queue=collections.deque()
	queue.append(root) #这时候queue只有顶这一个元素
	
	while queue:  #一次循环做一层，第二层获得两个元素
		level_size=len(queue)#长度为2
		current_level=[]
		
		for _ in range(level_size): #遍历这一层长度，走完这个循环就获得这一层全部人的孩子
			node=queue.popleft()#拿出左边，注意本次循环，新的一层元素从右边进，旧的出来
			current_level.append(node.val) #取得左边元素的值
			print(current_level)
			if node.left:queue.append(node.left)  #把此点的孩子放进来
			if node.right:queue.append(node.right) #queue装整一层的元素
		result.append(current_level)
	return result
levelOrder(a)

#给我自己写
#先拿到根点，放入队伍，(然后存变量，查孩子，把他的孩子放入队伍)，，查孩子)


# 104 111   最大最小深度
# bfs  判断根节点，叶子节点     On
   
# dfs 走完一条竖直路，更新max，min，然后走第二条路   On
# 给我做的话，一直打洞，高于max的话就更新，小于min就更新 

def maxDepth(root):
	if not root:return 0
	return 1+max(maxDepth(root.left),maxDepth(right)) #分治
	
#最小
def minDepth(root):
	if !root :return 0
	if !root.left return 1+ 
	