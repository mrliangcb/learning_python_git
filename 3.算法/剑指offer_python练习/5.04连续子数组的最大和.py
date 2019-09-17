
# leecode 53
#连续子数组的最大和
# 枚举分析法:组合问题
# 分治：不是尝试
# 动态规划法(如何避免重复计算)，尝试做法，取或者不取

class Solution(object):
	def maxSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		l = len(nums)
		if l == 0:
			return 0
		# 以索引 i 结尾的最大子数组的和
		end_i_max = nums[0]
		# 最后返回的数
		res = nums[0]
		for i in range(1, l):#从1 开始遍历，0项一开始就作为上一最大项val
			# 例：[-3,1]
			end_i_max = max(nums[i], end_i_max + nums[i]) #last累计+now  vs now   ，如果now较大，则说明过去是负数，则从现在开始累计
			res = max(res, end_i_max)#当前累计最大 VS 过去累计最大
		return res

a=Solution()
print('结果:',a.maxSubArray([1,2,3,-4,5,6]))
print(1+2+3+5+6)




















