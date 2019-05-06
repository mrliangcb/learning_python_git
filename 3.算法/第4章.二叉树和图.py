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

#递归
def isValid(root,min,max):
	if root==None :return True
	if (min!=None and root.val<=min) :return False;
	if (max !=None and root.val>=max) :return False
	return isValid(root.left,min,root.val)and isValid(root.right,root.val,max);

isValid(a,2,3)







