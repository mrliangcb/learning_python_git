

#o(n)的方法   马拉车算法
# https://blog.csdn.net/asd136912/article/details/78987624


def manacher(s):
	s = '#' + '#'.join(self.string) + '#'    # 123变成  #1#2#3#  
	lens = len(s)
	p = []                     # p保存串的长度
	maxj = 0                   # 当mxi 创新高的时候，同时记录左边边界j
	maxl = 0                   # 记录右边界  摸到的最新最右边的
	maxd = 0                   # 记录最长的串
	for i in range(lens):      # 遍历字符串,i是当前处理元素
		if maxl > i: #若i在 右边界内，也就是 p[i]只有 p[对称j] 右边界-i 两种情况
			count = min(maxl-i, int(p[2*maxj-i]/2)+1)  # 可以根据对称找关系   应该是p[maxj+(mx-i)]
		else :
			count = 1 #如果没有对称可以参考
		#count是用于扩大半径距离的
			
		while i-count >= 0 and i+count < lens and s[i-count] == s[i+count]:  
		# 只要左边界不超过0，右边界不超过总长， 而且扩大的左边和右边相同   所以两边扩展
			count += 1
		if(i-1+count) > maxl: #如果现在i摸到比maxl还右边  或者>= 
			maxl, maxj = i-1+count, i  #那现在的最右边界更新 左也更新
		p.append(count*2-1) #于是第i个半径就定下来了
		maxd = max(maxd, p[i])                       # 跟原来的最大值比，取大的
	return int((maxd+1)/2)-1                        # 去除特殊字符，特殊字符总是比数字多一个，+1符号，/2表示，全是数字+1符号，所以-1















