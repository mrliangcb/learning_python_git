# 把只包含因子2、3和5的数称作丑数（Ugly Number）。
#例如6、8都是丑数，但14不是，因为它包含因子7。 
#习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数

#leecode 动态规划 找出第N个丑数


# 1.暴力法  用目标数除以 2 3 5 7 9 ……直到<n的奇数
# 2. p=(2^x)*(3^y)*(5^z)
# 设第i个丑数为f(i)  目标数为M  假设f(i)<=M<f(i+1)，则M前面的最大丑数为f(i),则下一个丑数则为f(i) *2 或者*3 或者*5
   
 
class Solution:
	def test(self, index):
		# write code here
		if index == 0:
			return 0
		# 1作为特殊数直接保存
		baselist = [1]
		min2 = min3 = min5 = 0   #这里是第几个
		curnum = 1
		while curnum < index: #假设生成第5个，从1开始
			minnum = min(baselist[min2] * 2, baselist[min3] * 3, baselist[min5] * 5)#minnum装的是最新的丑数
			baselist.append(minnum)
			# 找到第一个乘以2的结果大于当前最大丑数M的数字，也就是T2
			while baselist[min2] * 2 <= minnum:  #某个丑数乘以2刚好大于最新丑数
				min2 += 1
			# 找到第一个乘以3的结果大于当前最大丑数M的数字，也就是T3
			while baselist[min3] * 3 <= minnum: #某个丑数*3 刚好大于最新丑数
				min3 += 1
			# 找到第一个乘以5的结果大于当前最大丑数M的数字，也就是T5
			while baselist[min5] * 5 <= minnum: #某个丑数乘以5 刚好大于丑数
				min5 += 1
			curnum += 1#每轮生成一个，
		return baselist[-1]#返回最新
a=Solution()
for i in range(20):
	b=a.test(i)
	print(b)
	
# m2表示T2的号数，T2是*2之后刚好比最新丑数大的数

# 初始化t1 t2 t3=1
# [1] 最新丑数1  T2*2 T3*3 T5*5最小为2,加入到最新丑数[1 2]
# 















