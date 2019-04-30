#堆栈队列  stack  queue

# 先入后入

#判断()是否合法，左右匹配
#()[]  ([])]不合法
#[先入，遇到]就都出去  [ ( ] 于是都出不去，string已经遍历完了，栈还没出空，所以不匹配
# 每个元素O1，n个元素就是on    空间也是on

# def isValid(self,s):
	# stack=[]
	# paren_map={')':'(',']':'[','}':'{'}  
	# for c in s:
		# if c not in paren_map:# 不在右边，则压入
			# stack.append(c) #压入用append
		# elif not stack or paren_map[c]!=stack.pop() #如果是右边元，但是又不和栈顶匹配，就返回不匹配
			# return Fales
		# return not stack #如果遍历完了，检查一下是否空，空则返回true

a={'a':'b'} #检查b在Key中有出现吗，不是value
print('b' in a) #False
b=[1,2,3]
print(b.pop()) #pop(0)打出栈底
print(b)


#replace"()",""   从小到大匹配然后消除,时间复杂度不好计算

























