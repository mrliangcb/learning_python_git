


# 输入(树根，整数)，打印出二叉树中结点值的和为输入整数的所有路径。
# 路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。

# 
class Node:
	def __init__(self,rootObj):
		self.val = rootObj #建立一个根val
		self.left = None
		self.right = None

a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
e=Node(5)

a.left=b
a.right=c
b.left=d
b.right=e

def PrintTB(root):
	if not root:
		return []
	res=[]
	res_val=[]
	res.append(root)   #根节点入队
	while len(res)>0:  #只要队里有元素，就继续遍历
		node=res.pop(0) #拿出待处理元素0
		res_val.append(node.val)  #将本节点的值输出
		if node.left: #遇到一个元素就把左右孩子加入队列后边
			res.append(node.left)
		if node.right:
			res.append(node.right)
	return res_val
	
print('打印层树:',PrintTB(a))
	



result=[]

	# 返回二维列表，内部每个列表表示找到的路径
def FindPath(root, expectNumber):#根  还有  期望和
	# write code here
	if not root:
		return []
	
	FindPathCore(root,[],0,expectNumber)
	return result
		
def FindPathCore(root,path,currentNum,expectNumber):
	currentNum += root.val     #当前数+节点变量
	path.append(root) #当前节点加入path
	
	
	# 判断是否达到叶子节点
	flag = (root.left==None and root.right==None)# 非叶子的，为false
	
	#如果到达叶子节点且当前值等于期望值(任务的终点)
	if currentNum==expectNumber and flag: # 如果当前数=期望数，flag为true(到了叶子)
		onepath=[]
		for node in path:#到了这个叶子传下来的路径
			onepath.append(node.val) #将路径给onepath，因为就算返回上层，path pop完了，onepath还保存着成果
		result.append(onepath) 
		
	if currentNum<expectNumber: #如果当前数<期望数
		if root.left:#左边非空，找左边
			FindPathCore(root.left,path,currentNum,expectNumber)
		if root.right:#否则找右边
			FindPathCore(root.right,path,currentNum,expectNumber)
	
	#如果不是叶子，也不是小于期望值，表示这条路行不通，直接把这个节点去除，然后回到上一层
	
	path.pop() 
				
		
		
print(FindPath(a,7)) #1,2,4就是路径，得到7

# 搜索到某一个路径的和 为目标，则输出整个目标

























