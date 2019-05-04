# leecode

import heapq as hp

# 239 移动窗口 的最大值
# [1,3,-1,-3,5,3,6]  k=3  找最大值  中位数
# [1,3,-1] 返回3   [3,-1,-3] 返回3
# 优先队列法  大顶堆
# 建立一个K堆
   # 3
# -1    1
#向右移窗口   1出去，新的-3进来(log2(k))，排序建立新堆，o(1)   
     # 3
 # -1      -3

ans = []
hp.heappush(ans,1)#把1放进来，而且1放在最顶，最小的放最顶
hp.heappush(ans,3)
hp.heappush(ans,2)
hp.heappush(ans,5)
print(hp.heappop(ans))#把顶拿出来
print(ans)#剩下的自己重新排序，把最小的放顶

# 简化方法  queue队列 前面进，后面出   双端队列 deque   数组实现
#1,3,-1进入队列，因为3比1大，所以1出队，-1进来，没有比3大，所以进来[3  -1]#因为没满，右边还有空位，-3进来   [3  -1  -3]#因为满了，所以左边先出去   [-1 -3 5]
# 进一步维护  5比前面两个都大 所以左边两个出队，5的右边先不管[5]  
#所以每个步骤有两小步：  进来  维护 [5,3,6]   [6]
#这种更快 on   最后答案是，输出每次窗口的最大值的下标
class answer():
	def maxSlidingWindow1(self,nums,k):
		if not nums:return []  #更加健壮性
		window,res=[],[]  #窗口和输出盒子
		for i,x in enumerate(nums):#x是新进入的数
			if i >=k and window[0] <=i-k:#右边就是判断窗口多长的，如果刚好等于三，窗口第一位应该存下标是i-3及以下
				window.pop(0)#如果新元素比左边大，第0位出去  或者
			while window and nums[window[-1]] <=x:#window非空，队列最右边对应的num比新的数小，左边全部出去
				window.pop()
			window.append(i)#加入nums下标
			if i>=k-1:
				res.append(nums[window[0]])#左边应该是目前最大的,此时最大数字给res
		return res
a=answer()
print(a.maxSlidingWindow1([1,3,-1,-3,5,3,6],3))










