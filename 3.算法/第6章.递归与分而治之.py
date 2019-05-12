#递归与分而治之



#分治 divde conquer   先解决小问题再解决大问题

#递归三要素
# 向下打洞(是左右子树同时打，还是有先后顺序)
# 设置检测到底了没
# 优先底操作还是顶操作

#结构一般是，停止判断+递归操作

# 50   x=2 n=10  2^10=1024
# (1)pow(x,n)    o1
#  (2)暴力 on   x乘以自己N次
#  (3)分治办法 先获得一半的相乘，然后结果相乘   节省了一半的递归 偶数情况：y=2^int(n/2)   y*y   奇数：y=2^int(n/2)   y*y*x
#  更加高效是，2/n又分一半   可以看n可以分多少次一半2^x=n x=logx(n) 这么多次操作   比上面更少复杂度

def myPow(x,n):
	if not n:
		return 1
	if n<0:
		return 1/myPow(x,-n)
	if n%2: #奇数
		return x*myPow(x,n-1)
	return myPow(x*x,n/2)
#10(1/2)^x=1  10一直分，直到分到一个元素

#非递归
def myPow2(x,n):
	if n<0:
		x=1/x
		n=-n
	pow=1
	while n:
		if n&1:
			pow *=x
		x+=x  
		n>>=1 #位运算
	return pow
	
print(1&1)
	
	
	