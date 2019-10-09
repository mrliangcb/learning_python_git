
i=0
j=6
dp=[[0 for m in range(j-i+1)] for n in range(j-i+1)]
for m in range(j-i+1):
		dp[m][m]=1
		
x='ABABBBA' 
for m in range(len(dp)-1):
	if x[m]==x[m+1]:
		dp[m][m+1]=1
			
for m in range(len(dp)-2,-1,-1):
	for n in range(m+2,len(x)):
		if x[m]==x[n]:
			dp[m][n]=dp[m+1][n-1]#如果头尾元素相等那取决于左下角
	
	
print(dp)
