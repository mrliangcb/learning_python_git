#https://blog.csdn.net/Marksinoberg/article/details/69482397
#从上到下打印二叉树
#https://blog.csdn.net/u010005281/article/details/79493413
import numpy as np

class BinaryTree:
    def __init__(self,rootObj):#儿子的，一创建运行，=Binary(rootobj)  self只是声明这个是儿子的
        self.key = rootObj#(参数给这里)
        self.leftChild = None
        self.rightChild = None
	#上面是儿子的数字，下面是儿子的工具箱
    def insertLeft(self,newNode):  #也是儿子的 儿子名.insertLeft调用
        if self.leftChild == None: #如果这个大儿子左边没有儿子  a=binary(b) binary叫爸爸，a叫大儿子，b是小儿子
            self.leftChild = BinaryTree(newNode) #就给大儿子的左边起一棵树，名字是参数
        else: #如果大儿子左边有小儿子
            t = BinaryTree(newNode)#则t取得新儿子
            t.leftChild = self.leftChild#大儿子的左儿子给新儿子的左边
            self.leftChild = t#当然，新儿子就成为了大儿子的左儿子
 
    def insertRight(self,newNode):#如果要调用上面的insertLeft函数，这个类内其他函数或者自己，要self.函数名，不能漏了
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)#有点递归的感觉
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
 
 
    def getRightChild(self):
        return self.rightChild
 
    def getLeftChild(self):
        return self.leftChild
 
    def setRootVal(self,obj):
        self.key = obj
 
    def getRootVal(self):
        return self.key

		

#根据前序，中续遍历建立树的方法
def getBSTwithPreTin(self, pre, tin):
		if len(pre)==0 | len(tin)==0: #传进来的数组长度如果为0，就返回none
			return None
		root = treeNode(pre[0])#建立根节点，也就是前序遍历的第0位，变量是pre[0]，整个树变量给root
		print('中序遍历的enu:',list(enumerate(tin)))
		for order,item in enumerate(tin):  #得到[(0, 4), (1, 7), (2, 2), (3, 1), (4, 5), (5, 3), (6, 8), (7, 6)]
			if root .val == item:
				root.left = self.getBSTwithPreTin(pre[1:order+1], tin[:order])
				root.right = self.getBSTwithPreTin(pre[order+1:], tin[order+1:])
				return root
				
				
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
a=list(enumerate(seasons))
print('a:',a)
print(seasons[:2])#最尾那个不打印

a = BinaryTree('a')#建立一个树节点


