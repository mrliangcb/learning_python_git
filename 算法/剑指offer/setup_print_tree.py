#建立和打印二叉树setup_print_tree
class Solution:
	
	# 给定二叉树的前序遍历和中序遍历，获得该二叉树
	def getBSTwithPreTin(self, pre, tin):
		if len(pre)==0 | len(tin)==0: #传进来的数组长度如果为0，就返回none
			return None
		root = treeNode(pre[0])#建立根节点，也就是前序遍历的第0位，变量是pre[0]，整个树变量给root
		for order,item in enumerate(tin):  #得到[(0, 4), (1, 7), (2, 2), (3, 1), (4, 5), (5, 3), (6, 8), (7, 6)]
			if root .val == item:
				root.left = self.getBSTwithPreTin(pre[1:order+1], tin[:order])
				root.right = self.getBSTwithPreTin(pre[order+1:], tin[order+1:])
				return root
	
	#从上往下打印出二叉树的每个节点，同层节点从左至右打印，打印在一层
	def PrintFromTopToBottom(self, root):
		array = []
		result = []
		if root == None:
			return result
		array.append(root)#根放进数组
		while array:#数组不为0继续  result装变量，array装树
			newNode = array.pop(0)#把第0位取出来
			if newNode!='*':
				result.append(newNode.val)#把他的变量给result
				if newNode.left != None:#左边有
					array.append(newNode.left)#加入到array待处理
				else:array.append('*')
				if newNode.right != None:#右边有
					array.append(newNode.right)
				else:array.append('*')
			else:result.append('*')
		while result[-1]=='*':
			del result[-1]
		return result
	
	def Print(self, pRoot):#打印在多层
		# write code here
		if pRoot == None:
			return []
		stack = [pRoot]
		ret = []
		while(stack):
			tmpstack = []
			tmp = []
			for node in stack:
				tmp.append(node.val)
				if node.left:
					tmpstack.append(node.left)
				if node.right:
					tmpstack.append(node.right)
			ret.append(tmp[:])
			stack = tmpstack[:]
		return ret

	def Print_zhi(self, pRoot):#之字形打印
			# write code here
			if pRoot == None:
				return []
			stack = [pRoot]
			step = 1
			ret = []
			while(stack):
				tmpstack = []
				tmp = []
				for node in stack:
					tmp+=[node.val]
					if node.left:
						tmpstack.append(node.left)
					if node.right:
						tmpstack.append(node.right)
				if step%2==0:
					tmp.reverse()
				ret.append(tmp)
				step += 1
				stack = tmpstack[:]
			return ret

		
class treeNode:
	def __init__(self, x):
		self.left = None
		self.right = None
		self.val = x


solution = Solution()
preorder_seq = [1, 2, 4, 7, 3, 5, 6, 8] #前序遍历
middleorder_seq = [4, 7, 2, 1, 5, 3, 8, 6]#中序遍历
treeRoot1 = solution.getBSTwithPreTin(preorder_seq, middleorder_seq)
print(solution.Print(treeRoot1))
# #打印
# newArray = solution.PrintFromTopToBottom(treeRoot1)

# print(newArray)

