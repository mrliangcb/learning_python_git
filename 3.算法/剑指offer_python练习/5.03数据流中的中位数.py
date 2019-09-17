
	

from heapq import *    # 利用python的heapq库,来实现堆

#自己写堆




class Solution:
	def __init__(self):
		self.small = []
		self.large = []
	def Insert(self, num):
		# write code here
		small,large = self.small,self.large
		heappush(small,-heappushpop(large,-num))
		if len(large) < len(small): 
		# 这样就保持了大顶堆和小顶堆元素个数的相对稳定性，在取中位数的时候也方便。
			heappush(large,-heappop(small))
	def GetMedian(self,n=1):    
		# write code here
		small,large = self.small,self.large
		if len(large) > len(small):
			return float(-large[0])
		return (small[0] - large[0]) / 2.0

a=Solution()
nums=[1,1,2,3,4,5,6]
for i in nums:
	a.Insert(i)
print(a.GetMedian())



class myheap():
	def __init__(self,type):
		self.que=[]
		if type=='max':
			self.type='max'
		else:
			self.type='min'
	def push(self,num):
		self.que.append(num)#结尾插入
		#调整位置
		self.up(len(self.que))#将最后一个元素上浮,逻辑符号
		
	def pop(self):
		if len(self.que)<=0:#没东西可以删除
			print('error: empty')
			return 
		output=self.que[0]
		self.que[0]=self.que.pop()
		print('中途显示',self.que)
		self.down(1)
		
		return output
		
	def up(self,child):#传入要上升的逻辑号
		if child<=1:
			
			return 
		if self.type=='max':
			if self.que[(child-1)]>self.que[int(child/2)-1]:#如果比父大
				self.que[int(child/2)-1],self.que[child-1]=self.que[child-1],self.que[int(child/2)-1]#交换
				self.up(int(child/2))
		if self.type=='min':
			if self.que[child-1]<self.que[int(child/2)-1]:#如果比父大
				self.que[int(child/2)-1],self.que[child-1]=self.que[child-1],self.que[int(child/2)-1]#交换
				self.up(int(child/2))
	def down(self,father):
		#先检查左右孩子
		l_f=r_f=False
		if (2*father)<=len(self.que):
			left=self.que[2*father-1]
			l_f=True
		if (2*father+1)<=len(self.que):
			right=self.que[2*father+1-1]
			r_f=True
		if (not l_f) and (not r_f):#左右都无
			return 
		
		if self.type=='max':
			if l_f and r_f:
				if left>self.que[father-1] and left>right:#左孩子最小
					self.que[father-1],self.que[2*father-1]=self.que[2*father-1],self.que[father-1]
					self.down(2*father)
				if right>self.que[father-1] and right>left:
					self.que[father-1],self.que[2*father+1-1]=self.que[2*father+1-1],self.que[father-1]
					self.down(2*father+1)
			elif l_f:#只有左
				if left>self.que[father-1]:
					self.que[father-1],self.que[2*father-1]=self.que[2*father-1],self.que[father-1]
					self.down(2*father)
			elif r_f:#只有右
				if right>self.que[father-1]:
					self.que[father-1],self.que[2*father+1-1]=self.que[2*father+1-1],self.que[father-1]
					self.down(2*father+1)
			
		if self.type=='min':
			if l_f and r_f:
				if left<self.que[father-1] and left<right:#左边最小
					self.que[father-1],self.que[2*father-1]=self.que[2*father-1],self.que[father-1]
					self.down(2*father)
					
				if right<self.que[father-1] and right<left:#右边最小
					self.que[father-1],self.que[2*father+1-1]=self.que[2*father+1-1],self.que[father-1]
					self.down(2*father+1)
					
			elif l_f:#只有左
				if left<self.que[father-1]:
					self.que[father-1],self.que[2*father-1]=self.que[2*father-1],self.que[father-1]
					self.down(2*father)
					
			elif r_f:#只有右
				if right<self.que[father-1]:
					self.que[father-1],self.que[2*father+1-1]=self.que[2*father+1-1],self.que[father-1]
					self.down(2*father+1)

#已完成自定义堆

a=myheap('min')
a.push(1)
a.push(2)
a.push(5)
a.push(3)
a.push(10)
a.push(9)
a.push(15)
a.push(17)
print(a.que)
print(a.pop())
print(a.que)
print(a.pop())
print(a.que)