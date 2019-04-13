#二叉树深度
import setup_print_tree as set

class Solution2:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot == None:
            return 0
        if pRoot.left == None and pRoot.right==None:
            return 1
        return max(self.TreeDepth(pRoot.left),self.TreeDepth(pRoot.right))+1
		
solution = set.Solution()
preorder_seq = [1, 2, 4, 7, 3, 5, 6, 8] #前序遍历
middleorder_seq = [4, 7, 2, 1, 5, 3, 8, 6]#中序遍历
treeRoot = solution.getBSTwithPreTin(preorder_seq, middleorder_seq)


solution2=Solution2()
print(solution2.TreeDepth(treeRoot))#深度为4