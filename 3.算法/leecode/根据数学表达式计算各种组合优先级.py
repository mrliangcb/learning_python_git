
a='1+3+4*6'
def comput(a):
	result=[]

	for i in range(len(a)):
		if a[i] in ['+','-','*','/']:#找符号
			c=a[i]
			left=comput(a[:i])#左边组合的数组
			right=comput(a[i+1:])
			for j in left:
				for k in right:
					print(left,right)
					if c=='+':
						result.append(j+k)
					elif c=='-':
						result.append(j-k)
					elif c=='*':
						result.append(j * k)
			

	if not result:#如果没找到符号，那就是一个数字  这里重点
		result.append(int(a[0]))
	return result
			
			
			
r=comput(a)
print(r)
			
			
			
			
			
			
			