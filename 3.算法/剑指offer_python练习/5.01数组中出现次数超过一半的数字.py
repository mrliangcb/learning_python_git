

# 方法一：统计到dict
# 方法二: 排序，然后中间那个就是了  长5：>=3    长6:>=4，改变输入数组
# 方法三：用计数器，不改变输入数组

a={'a','b','c'} #集
print(a)

#partition 函数：分割算法，分成两部分，左边小于P，右边大于P


def count(nums):
	if not nums or len(nums)<=0:
		return 0
	res=nums[0]  #取出第一位
	times=1
	for i in range(1,len(nums)):#从0开始
		if times==0:#如果现在统计角色次数为空
			res=nums[i] #更新统计角色
			times=1 #次数+1
		elif nums[i]==res: #已经有统计角色,并且为当前遍历元素
			times+=1  #直接加以
		else:
			times-=1  #当前元素非统计角色
		
	sum=0
	# 知道了出现最多次的是res，然后计算一下res是不是大于总长的一半
	for j in nums: #最后得到的是res，统计角色，统计出现的次数
		if j==res: 
			sum+=1
	return res if sum*2>len(nums) else 0


a=[1,2,3,2,2,2,5]
print(count(a))




















