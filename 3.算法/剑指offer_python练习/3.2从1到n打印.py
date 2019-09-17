#leecode 17

# 最大数的问题，容易溢出
# 字符串或者数组表达最大数
# 最大的n位数
# 停止输出条件  n=4 最大就是9999

#深度优先
#画一棵树，上层解决高位0-9遍历，下层解决低位0-9遍历,到最底才打印。


def mprint(n):#函数入口，只管最高位   因为这里没有index所以要另外设置一个函数进行循环，当然这里默认index0也是可以写成一个的
	num=['0']*n
	for i in range(10): #将最高位分别填0-9
		num[0]=str(i)
		print('主入口',num)
		print2(num,n,1)#让print2考虑第二高位

def printnum(number):
	isBeginning0=True
	nLength=len(number)
	for i in range(nLength):
		if isBeginning0 and number[i]!='0':
			isBeginning0=False
		if not isBeginning0:
			print('%c' %number[i])
	print('\t')

def print2(num,length,index): #这一层处理第index高位
	
	if index>=length:#溢出到个位的右边
		return 
	
	for i in range(10):
		num[index]=str(i)#第index高位轮着放0-9
		print('2函数中num',num)
		print2(num,length,index+1)
		
	if index==length-1:#当处理到个位的时候
		printnum(num)#将字符型num打印出来
		return
		
		
mprint(3)








