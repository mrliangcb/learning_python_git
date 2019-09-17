
# 调整数组的顺序使奇数位于偶数前面

# 方法一：
# 手尾指针向中间靠拢，然后交换


# 方法二：  如果还要让相对位置保持不变(用两个数组来装，最后接起来)
# 

def reOrderArray(array):
	# write code here
	res1=[]
	res2=[]
	for i in array:
		if i%2!=0:
			res1.append(i)
		else:
			res2.append(i)
	return res1+res2




