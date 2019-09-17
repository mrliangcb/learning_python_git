import numpy as np


class Solution():
	def __init__(self,m):
		self.input=np.array(m)
		
		self.cnt_rest=len(m)*len(m[0])
		
		print('输入:',self.input)
	
	def scan(self,x,y):
		self.cnt=set()#缓存已读点
		self.search(self.input,x,y)
		return self.cnt
		
	def search(self,m,x,y):#扫描元素所在块,单词扫描的路径放在set
		if (x,y) in self.cnt:
			return
		me=m[x][y]
		self.cnt.add((x,y))
		#走上边
		if x>0 and m[x-1][y]==me:
			self.search(m,x-1,y)
		#走下边
		if x<len(m)-1 and m[x+1][y]==me:
			self.search(m,x+1,y)
		#走左边
		if y>0 and m[x][y-1]==me:
			self.search(m,x,y-1)
		#走右边
		if y<len(m[0])-1 and m[x][y+1]==me:
			self.search(m,x,y+1)
	
	def drop(self,m):
		for x in range(len(m)-1,0,-1):#自底向上
			for y in range(len(m[0])):
				if m[x,y]==0:
					while m[x,y]==0 and sum(m[:x,y])!=0:#元素为0 而且 上方元素和不为0，表示还可以往下掉
						m[1:x+1,y]=m[0:x,y]
						m[0,y]=0
						
		
	def dele(self,x,y):#消去元素所在块
		print('消:',self.input[x,y])
		block=self.scan(x,y)
		if len(block)>=3:
			for i,j in block:
				self.input[i,j]=0
				self.cnt_rest-=1
			self.drop(self.input)
		return self.input
	
	def rest(self):
		
		return self.cnt_rest

a=[[1,2,3,2],[1,3,2,3],[1,1,3,3]]
test=Solution(a)
print(test.scan(0,0))
print(test.dele(0,0))
print(test.dele(2,2))
print(test.rest())

