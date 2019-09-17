#leecode  18-20  

# 判断字符串是否表示数值（包括整数和小数）
# 大写字符转换为小写后生成的字符串
# 只要排除 违反规则的就行

# 重点是盯着e e前 e后

def isNumb(s):
	if not s or len(s)<0:
		return False
	alist=[i.lower() for i in s] #将字符串转到一个数组
	if 'e' in alist:
		index=alist.index('e') #找出第一个e的位置
		front=alist[:index] #e之前的
		behind=alist[index+1:] #e之后的
		if '.'in behind or len(behind)==0: #小数点在e后，返回错
			return False
		isfront=isDigit(front) #判断e前是否数字
		isbehind=isDigit(behind)  #判断e后是否数字
		return isfront and isbehind #
	else:
		return isDigit(alist)
		
		
def isDigit(alist):
	dotNum=0
	allow_num = ['0', '1', '2', '3', '4', '5',
				 '6', '7', '8', '9', '+', '-', '.']  #如果有e也被排除了
	for i in range(len(alist)):
		if alist[i] not in allow_num:
			return False
		if alist[i]=='.':
			dotNum += 1
		if alist[i] in '+-' and i!=0:#只能首位为+-号
			return False
	if dotNum>1:
		return False
	return True
		
print('A'.lower())  #大写字符转化成小写
print(isNumb('.123'))

# 出现两个E的不要
#e前要有数字，后面也要有
#+-号只能出现在首位或者e后面
#

# s='' 则s 为False


	

# a='aebcde'
# print(a.index('e'))   #返回第一个e



