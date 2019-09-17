

#leecode 10

# 给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。

# '.' 匹配任意单个字符。

# '*' 匹配零个或多个前面的元素。

# 匹配应该覆盖整个字符串 (s) ，而不是部分字符串。

# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。

# 例如给abc 和a*b*c  返回true

# 动态规划法(子问题的最优，表格法)
# 匹配 A和B串，   分别放行列，左上角为起点




# 递归解法   解决完全匹配问题   abc  和a.c   不能解决abcdef vs  bcd
#  最大问题是*
def match(s,pattern):

	if len(s)==0 and len(pattern)==0:return True
	if len(s)>0 and len(pattern)==0:return False

	#第二位是*     ac   a*c  |  abc a*c  |    
	if len(pattern)>1 and pattern[1]=="*": #
		if len(s)>0 and (s[0]==pattern[0] or pattern[0]=='.'):#第一位匹上（真匹或者通匹）
		
			return match(s[1:],pattern[2:]) or match(s[1:],pattern)  #a*c 下放c  c  *c  #match(s,pattern[2:])
		else: #第一位没配上
			return match(s,pattern[2:])# 跳过*   'ef','c*ef'这种认为true  *要贴着前面看，如c*可以认为是空，而不是c或很多c，还有没c
			
	#第二位不是*，于是只配一位就好
	if len(s)>0:
		if (s[0] == pattern[0] or pattern[0] == '.'):#第一位匹配
			return match(s[1:],pattern[1:])#剩余做匹配

			
	return False


print(match('aef','ac*ef'))

#遇到* 

# 第一位也不中 bc  a*c  跳过星号，再跟s比较
# s p[2]     知道

#第一位中

#匹0次  如ac  a*c          
#   s[1] o[2] 

# 匹1次   如aac   a*c         
# s[1]   p

#匹2次  如aaac  a*c
# 



