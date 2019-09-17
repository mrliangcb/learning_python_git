
# 接雨水

#      [0,1,0,2,1,0,1,3,2,1,2,1]
# 了每个元素代表一个山的海拔高度
# 输出6，因为能接6滴水
#
#
#2                      1
#1             1        1 1   1
#0层      1 "" 1 1 "" 1 1 1 1 1 1

#第0层容纳 2
#  1       4
#  2       

# 所以容纳6滴水

# 法一：   思路：一层一层计算  复杂度太高

# 法二：最大值的两边分别计算
# (1)遍历整个数组找到 最大值
# (2)左到右遍历到最高点，求积水
# (3)从右至左，求积水
# 复杂度为 o(n)

nums=[0,1,0,2,1,0,1,3,2,1,2,1]
def findmax(nums):
	index=0
	num=nums[0]
	for i in range(1,len(nums)):
		if nums[i]>num:
			num=nums[i]
			index=i
	return index,num
		
a,b=findmax(nums)
print(a,b)

def comput(nums):
	
	index,val=findmax(nums)#获得最高点的 位置和值
	#初始化左右边界
	sum=0
	L=0
	R=0
	#查左边
	for i in range(index):#一直遍历到左边
		if nums[i]>=L:#新的左边界
			L=nums[i]
		else:#产生积水
			sum=sum+(L-nums[i])
	
	#查右边,从右往左
	for j in range(len(nums)-1,index,-1):
		print('j:',j)
		if nums[j]>=R:
			R=nums[j]
		else:
			sum=sum+(R-nums[j])
	return sum
	
test=comput(nums)
print('答案为:',test)













