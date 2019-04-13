#(12)左旋转字符串
#self就是建立一条通道，给私有属性传进来

#无self
# class Solution:
	# def LeftRotateString(s,n): 
		# print(self.name)
		# # write code here
		# if s == '':
			# return s
		# n = n%len(s)
		# return s[n:]+s[0:n]
# a='abcdefg'
# solution=Solution
# print(solution.LeftRotateString(a,2))

class Solution:
	def LeftRotateString(self,s,n): 
		# write code here
		if s == '':
			return s
		n = n%len(s)
		return s[n:]+s[0:n]
# #有self
t=Solution()
a='abcdefg'
print(t.LeftRotateString(a,2))   

#所以参数里面的self表示这个类，传入一个类，他的私有属性全部都能用，相当于声明一个self 自己类
#我还是比较喜欢把参数提前传入到初始化函数，然后类再调用

