# 求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。


# 法一 ： 用sum函数
# 法二： 一个函数做递归，一个函数做终止 0转为false

a=[]
print(a==None)#不是none
print(len(a)<=0) #是0
if a:
	print('if a 通过')

def Sum_Solution(n):
	# write code here     
	return sum(n)

def sum0(n):
	return 0

def sum(n):
	func={False:sum0,True:sum} #字典存函数地址
	return n+func[not not n](n-1) #比如输入9 9+func[1](8)+   当n=0时候 func[0]=0






























