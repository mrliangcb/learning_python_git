#建树和遍历树
#https://blog.csdn.net/u010636181/article/details/78289429
#下面这个画二叉树
#https://www.cnblogs.com/rocketfan/archive/2009/09/10/1564232.html
#https://www.cnblogs.com/AimeeKing/p/5021675.html


class BinaryTree:
    def __init__(self,rootObj):#儿子的，一创建运行，=Binary(rootobj)  self只是声明这个是儿子的
        self.key = rootObj#(参数给这里)
        self.left = None
        self.right = None
	#上面是儿子的数字，下面是儿子的工具箱
    def insertLeft(self,newNode):  #也是儿子的 儿子名.insertLeft调用
        if self.left == None: #如果这个大儿子左边没有儿子  a=binary(b) binary叫爸爸，a叫大儿子，b是小儿子
            self.left = BinaryTree(newNode) #就给大儿子的左边起一棵树，名字是参数
        else: #如果大儿子左边有小儿子
            t = BinaryTree(newNode)#则t取得新儿子
            t.left = self.left#大儿子的左儿子给新儿子的左边
            self.left = t#当然，新儿子就成为了大儿子的左儿子
 
    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.right
            self.right = t
abs
def mirri(root):
	if (root is None):
	#if(root==None):
		return 0
	# if root is not None:
	# if root:
	if root!=None:
		print('非空')
		root.left,root.right=root.right,root.left
		if root.left:
			mirri(root.left) #python递归算法
		if root.right:
			mirri(root.right)
	return root
	

a=BinaryTree('1')
a.insertLeft('2')
a.insertRight('3')
a.right.insertLeft('4')
a.right.insertRight('5')

b=mirri(a) #返回一棵树

#b=mirri(a)
#print(type(mirri(a)))
print('					',a.key)
print('			',a.left.key,'				',a.right.key)
print('		',a.left.left.key,'		',a.left.right.key)

#print(b.leftChild.key)
# print(b.right.leftChile.key)
# print(b.right.right.key)












