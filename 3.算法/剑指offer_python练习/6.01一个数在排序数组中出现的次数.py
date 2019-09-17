


#1 2 2 2 2 3 4
# 找到这个数的开始和结束的位置, i, j,
# 然后j-i+1就是出现次数

# 二分法 例如找2
# 1：首先用二分法找到2，然后按顺序往左和往右扫描，所以复杂度有可能O（n）

# 优化的二分法
# https://blog.csdn.net/chaipp0607/article/details/76977687

# 中间数字>2: (开始2和结束2) s2和t2 应该在左边  
#         <2:  s2和t2  应该会在右边
# 如果    =2: 判断是否S2或者T2   
#             如果左边有2，则本2不是S2，S2肯定在左边
#			  如果左边不是2，则本2就是S2，T2在右边
#			  如果右边是2，则T2一定在本2右边
# 			如果右边不是2，则本2一定是T2
# 

class Solution:
	def GetNumberOfK(self, data, k):
		# write code here
		number = 0
		if data !=None and len(data)>0:#输入非空
			length=len(data)
			first = self.GetFirst(data,length,k,0,length-1)
			last = self.GetLast(data,length,k,0,length-1)
			if first > -1 and last > -1:
				number=last-first+1
		return number


	def GetFirst(self,data,lenth,k,start,end):#找到开始点
		if start>end:
			return -1
		middle = (start+end)//2
		if data[middle]==k:
			if middle>0 and data[middle-1]==k:
				end = middle -1
			else:
				return middle
		elif data[middle]>k:
			end=middle-1
		else:
			start=middle+1
		return self.GetFirst(data,lenth,k,start,end)
		

	def GetLast(self, data, lenth, k, start, end):#找结束点
		if start>end:
			return -1
		middle=(start+end)//2
		if data[middle]==k:
			if middle<end and data[middle+1]==k:
				start = middle+1
			else:
				return middle
		elif data[middle]>k:
			end=middle-1
		else:
			start=middle+1
		return self.GetLast(data, lenth, k, start, end)



