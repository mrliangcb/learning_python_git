#
# https://www.cnblogs.com/wikiwen/p/10225140.html
#输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序

# 压入顺序 1 2 3 4 5 ，注意这是顺序，中途可以取出，然后继续压，例如可以压123，然后取3，再压入45，那出栈顺序就是3 5 4 2 1
# 那取出顺序 4 3 5 1 2有可能吗

# 那就盯着出栈顺序，来模拟原本的入栈出站动作
# 

def func(pusho,popo):
	stack=[]
	while popo:#盯着出栈做
		if stack and stack[-1]==popo[0]: #看栈顶元素 是否=待出栈，如果=，则先实现出栈(stack出，待出元素丢掉，轮到下一位)
			stack.pop()
			popo.pop(0) 
			
		elif pusho:# 先入栈再判断
			stack.append(pusho.pop(0))
			
		else:
			return False
	return True

print(func([1,2,3,4,5],[3,5,4,2,1]))
































