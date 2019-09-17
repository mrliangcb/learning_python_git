

# leecode 567
# leecode 46  超出时间限制

import time

def Per(s):
	# write code here
	if not s: #空
		return []
	if len(s)==1: #只有一个
		return list(s)
	pStr=[]
	charlist=list(s) #数组化
	charlist.sort() #快排序
	
	for i in range(len(charlist)): #遍历排序后的字符串
		if i>0 and charlist[i]==charlist[i-1]:
			continue 
		temp=Per(''.join(charlist[:i])+''.join(charlist[i+1:]))  #i=0  
		print(temp)
		for j in temp:
			pStr.append(charlist[i]+j) #前后字母连一起,这是答案
	return pStr
	
a=[1,2,3]
b=[]
b.extend(a[:0])
b.extend(a[1:])
print('例子',b)

time_start = time.time()
print(Per('abc'))
time_end = time.time()
time_a= time_end - time_start
print('time cost', time_a, 's')

result=[]
def start(s):
	if not s: #空
		return []
	if len(s)==1: #只有一个
		return list(s)
	pStr=[]
	L=list(s) #数组化
	L.sort() #快排序
	per(s,'')#全数组，还有空箱子
	
def per(L,tmp):
	# if not L: #空
		# return []
	if len(L)==1: #只有一个，直接打包
		tmp=tmp+L[0]
		result.append(tmp)
		
		return 
		
	for i in range(len(L)):
		tmp=tmp+L[i] #开了个头，然后后面的部分交给递归，直到剩下的数组空了，就开始组装
		#有个问题，如何剔除选出了的头，然后把剩下的部分下放
		print('tmp是什么',tmp)
		deliver=[]
		deliver.extend(L[:i])
		deliver.extend(L[i+1:])
		per(deliver,tmp)#
		tmp=tmp[:-1] #这一条路弄好了，就返回上一层，并且把箱子的最后一位弄丢

time_start = time.time()

start('abc')

time_end = time.time()
time_b= time_end - time_start
print('time cost', time_b, 's')

print('时间差:',time_a-time_b)
print(result)


# 现在用的是暴力方法





# tips:
# 假设全局global=[[1]]  还有局部a[2]
# global.append(a)
# 之后如果a变成[2,3]，相应的global里面也会变的，由[[1],[2]]变成[[1],[2,3]]，怎么办呢
#解决办法: b=a[:]，复制数字给b，然后global.append(b)，这样改变a不会影响global，但不能改变b

#排列可以用循环右移的办法取巧
# [1]取第一个
# [1,2]取第二个，那就通过 2-1次循环右移，得到两个 [1,2]  [2,1]
# 上面两个加入3，分别循环右移3-1次，得到6个
#


