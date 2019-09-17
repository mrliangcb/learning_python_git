


# 不仅左孩子=右孩子，也要 左子树=右子树

#因为入口只传入根，但递归函数要传入左和右，所以分别开设两个函数
# 如果镜像的是相等的，那就是对称了

def isSym1(root):
	if root!=None: #  if root: 比较高效
		isSym(root,root)
	else:
		return True #空树也是对称

def isSym(pRoot1,pRoot2):#用排除法筛选
	if not pRoot1 and not pRoot2:  #两个指针为空
			return True
		if not pRoot1 or not pRoot2: #只有其中一个空的话，否
			return False
		if pRoot1.val != pRoot2.val:#如果 左！=右，否
			return False #return 就代表截住了，就不再往下遍历了
		return isSym(pRoot1.left,pRoot2.right) and isSym(pRoot1.right,pRoot2.left)
		#左孩子的左，右孩子的右 比较     左孩子的右=右孩子的左




















