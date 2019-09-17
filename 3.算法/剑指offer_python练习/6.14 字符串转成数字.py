




s='1023'
numstrs=['0','1','2','3','4','5','6','7','8','9']
sum = 0
label=1
for i in range(len(s)):
	#先判断正负
	if i==0: #第0位
		if s[i]=='-':#如果是负数
			label=-1 #符号位-1
			
		elif s[i]=='+':
			label=+1#不是-号就是正数
	# 如果第i位在numsrs存储中，就原来数*10，+现在数
	if s[i] in numstrs:
		sum =sum*10+numstrs.index(s[i])#*10 相当于整数左移
	
	#不在存储中，不是数字
	else:
		sum=0
print(sum*label)
























