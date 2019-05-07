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
	if root is None:
		return True
	if not helper(root.left):
		return False
	if prev and prev.val>=root.val:
		return False
	prev=root
	return helper(root.right)

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
#

