

# 斐波拉契系数
# 动态规划
# 自底向上


class Solution:
	def cal(self,n):
		if n<3:
			return n
		pre2,pre1=1,2
		for i in range(2,n):
			pre1,pre2=pre1+pre2,pre1
		return pre1

# 1 1 2 3 5 8 13 21
# 比如要求第7个数 
#      		     13
#		   5	     8
#		2     3    3    5
#    1   1  1  2  1 2  2 3
# 这里自上而下的话有大量重复的计算
#所以先从这个看出递推公式，然后再自下而上填表格


















