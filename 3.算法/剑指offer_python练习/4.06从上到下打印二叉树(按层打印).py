

# 按层从上到下吗，还是深度遍历(前中后序)那样
# 按层

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






























