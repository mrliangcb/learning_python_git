# 

a=[1,2,3]
print(a.pop(0))

#设计栈
class Solution:
	def __init__(self):
		self.stack=[]
		self.minstack=[]  #辅助存最小值

	def push(self, node):
		
		self.stack.append(node) #不管什么值，先入全局栈
		if self.minstack==[] or node<self.min():#最小栈为空，或者当前节点<最小栈顶
			self.minstack.append(node)#入最小栈
		else:
			self.minstack.append(self.min())#否则最小值入最小栈，这时候是基于第一步已经加入了值，最小栈非空的,否则空栈-1会超出范围
		
	def pop(self):
		
		if self.stack==[] or self.minstack==[]:  #如果全局栈或者最小栈非空(最小栈数量跟全局栈一样，最小栈代表现在全局栈中的最小)
			return None
		self.stack.pop()  #取出栈顶
		self.minstack.pop() #同时取出最小栈顶
		
	def top(self):
		# write code here
		return self.stack[-1]#查看全局栈的栈顶
		
	def min(self):#返回最小值
		
		return self.minstack[-1]  #最右边的























