

# '65+34*2/3+6*3'
# 收集数字过程 和符号分割过程
# 

# 遇到+号，65进，+进
#[65,+]
# 遇到* 号，  34和* 进 [65,+,34,*]
# 见到/  如果栈顶是+-号，则直接放进去，如果是乘除，那就先取出栈顶两位，然后34*2    结合再放入
# 然后68 / 放入栈 [65 + 68 / ]  遇到+，然后顶不是+-，所以前面是一块
# 所以取出顶两位 68/3=a 和最新符号放入 [65 + a + ]
# 遇到乘号 因为里面是+，不管 ，所以放入  [65 + a + 6 *]
# 遇到结尾元素，顶为*/ 所以取出6 * 再放入18


# 如果含括号呢
# 
# 遇到右符号或者终止，然后停下来返回位置

#
# 生成很多子栈  F(起始位置)
# 48+(36*2*(1  +  2  )  +  1)
# 0 123456789 10 11 12 13 14
# [48 + ]  遇到左括号，调用F(位置+1)   [36 * 2 *]  于是 [72 * ] 
# F[9] 遇到左括号12 返回结果   或者遇到结尾就返回
#   

x1='((36+7)*((3+2)+3/(1+2)))'
# x1=''
#先搞定有可能出现什么 ( ) + - * / 0~9数字

def add_num(que,num):
	if not que:
		if num=='':
			que.append(0)
		else:
			que.append(int(num))
	else:
		num=int(num)
		if que[-1] in ['*','/']:
			if que.pop()=='*':
				tem=que.pop() * num
				que.append(tem)
			else:
				tem=que.pop() / num
				que.append(tem)
		else:#不用取出来，直接加进去
			que.append(num)

def sum_all(que):
	out=que[0]
	
	for m in range(len(que)):
		if que[m]=='+':
			out=out+que[m+1]
			
		elif que[m]=='-':
			out-=que[m+1]
	print('返回',out)
	return out

#递归体
def F(x):
	if x=='':
		return 0
	
	huancun=''
	que=[]
	i=0
	while i<len(x) and x[i]!=')':#因为)是局部结束点  结尾是全局结束点
		if x[i]=='(':#左括号
			res,shif=F(x[i+1:])#获得新的括号()，作为缓存 然后跳到对应括号的后面
			i+=(shif+1)#获得偏移值
			huancun=res
			
		elif (x[i] in ['+','-','*','/']) :
			print('拿到符号:',x[i],huancun,que)
			add_num(que,huancun)#将huancun入栈
			huancun=''
			
			#新符号入栈
			que.append(x[i])
			print('入栈后:',que)
			
		else:#都是数字
			huancun+=x[i]
		i+=1
	# 遇到结束点就出来，总结答案，返回作为缓存或者全局答案
	if huancun:#最后一个数
		add_num(que,huancun)
	out=sum_all(que)
	print('加和',que,out)
	return out,i
	
print(F(x1))


# 左神逻辑
# num就像是我的huancun
# while i<长度 而且i不为):
	# 如果为数字
		# num=num*10+str[i++]-'0'
	# else if 不为(    那就是运算符
		# 运算函数(que,num)
		# que加入东西
		# num=0
	# else: 遇到左括号
		# i=bra[1]+1
	
# add运算(que,num)


print('-------  全局，非偏移方法  ---------------')
def F1(x,i):#获得初始位置i
	if x=='':
		return 0
	
	huancun=''
	que=[]
	
	while i<len(x) and x[i]!=')':
		if x[i]=='(':
			res,shif=F1(x,i+1)#传入初始位置,i对应'('
			i=shif#返回一个值告诉我，下一个')'在第shift个位置
			huancun=res
			print('遇到左括号后:','huancun:',huancun,'队列:',que)
			
		elif (x[i] in ['+','-','*','/']) :
			
			add_num(que,huancun)#将huancun入栈 
			huancun=''
			
			#新符号入栈
			que.append(x[i])
			print('拿到符号:',x[i],'入栈后:',que)
			
		else:#都是数字
			huancun+=x[i]
		i+=1
	#遇到最尾或者括号尾，就出来
	if huancun:#最后一个数
		add_num(que,huancun)
	out=sum_all(que)
	print('加和','队列:',que,'加和结果',out)
	
	if i<len(x):#局部结束点
		return out,i
	else:
		return out
	
print(F1(x1,0))




