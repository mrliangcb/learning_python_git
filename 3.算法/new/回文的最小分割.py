

#就是切开，使得每个部分都是回文串


#最少能够切最少获得回文数

# AAKAA BKBAA  K  A  A
# 01234 56789 10 11 12
# 把A当做一块，那后面的给子问题解决F(1)
# 把AA当做一块,后面F(2)
# AAKAA    F(5)

# def F(str,i):
	# if i==len(str):
		# return
	# #以i位置开头
	# for i in range(i,len(str)):
		# if(isP(str,i)):

# def func():#判断i到end是否回文

x='ABABBBAK'
# num为切的数量,func1求一个字串最小切的数量

#先做判断回文的总矩阵
dp=[[0 for m in range(len(x))] for n in range(len(x))]
for m in range(len(x)):#填对角
	dp[m][m]=1
for m in range(len(dp)-1):#填对角的右边一个
	if x[m]==x[m+1]:
		dp[m][m+1]=1
for m in range(len(dp)-2,-1,-1):
	for n in range(m+2,len(x)):
		if x[m]==x[n]:
			dp[m][n]=dp[m+1][n-1]#如果头尾元素相等那取决于左下角
print(dp)
print('完成dp矩阵')

dp2=[-1 for m in range(len(x)) ]

#因为后面要用到从i开始的，所以要全局记住i，不能以新的后序列的头开始
def func1(x,i):#i是出发位置，得到最少的数量
	
	if i>=len(x):#起始已经到终止位置了
		return 0
	if dp2[i]!=-1:#以这个i开头已经算过了
		return dp2[i]
	#假设切第一位
	num=[]
	for j in range(i,len(x),1):#从i开始到结尾
		
		if dp[i][j]==1:#查表看是否回文  #最低条件是自己一个人自成回文
			print('现在:',i,j,'要查:',j+1,dp2)
			num.append(1+func1(x,j+1))#以i为开头，记录早切或者晚切的结果
			
	print(i,'开始的时候，收集到这些分割法',num)
	min_num=min(num)
	dp2[i]=min_num#得到以I开头的最少分割数
	return min_num
		
print(func1(x,0))
	
