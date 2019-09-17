import numpy as np

# leecode 50
# class Solution(object):
	# def myPow(self, x, n):
		# if n == 0:
			# return 1
		# if n == 1:
			# return x
		# result = self.myPow(x,n>>1)
		# result*=result
		# if n&0x1==1 :#奇数的话，0次方位有1
			# print('次方为奇数',n)
			# result*=x
		# return result

# test=Solution()
# a=test.myPow(2,-5)
# print(a)



def compu(x,n):#计算入口x^n
	#底数有问题
	if x<=0:
		return 0
	# 底数没问题:
	if n>=0:
		return mpow(x,n)
	else: #负指数
		return 1/mpow(x,-n)


def mpow(x,n):   #计算指数
	#底层
	print(x,n)
	if n==1:
		return x
	if n==0:
		return 1
	#下放的次方 n/2
	xx=mpow(x,n>>1)#拿到2^5，就让底下算2^2
	xx=xx*xx
	if n&0b1:#若是奇数，再乘一次底数x
		xx=xx*x
		
	return xx
	
a=compu(2,5)
print('2^5',a,'\n')

a=compu(2,-5)
print('2^-5',a,'\n')
	
a=compu(0,-5)
print(a)













