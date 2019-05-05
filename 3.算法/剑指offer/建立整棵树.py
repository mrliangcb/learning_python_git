#根据两种遍历方法来建立树

class treeNode:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x
		
class Solution:
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
preorder_seq = [1, 2, 4, 7, 3, 5, 6, 8] #前序遍历
middleorder_seq = [4, 7, 2, 1, 5, 3, 8, 6]#中序遍历
solution = Solution()
treeRoot1 = solution.getBSTwithPreTin(preorder_seq, middleorder_seq)