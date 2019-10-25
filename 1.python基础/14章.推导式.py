

#map reduce这些都是用到推导式

#用推导式返回奇数

e=[1,2,3,4,5,6,7,8,9]
f=[i  if i%2!=0 else 'false'  for i in e]#如果if对了就返回i，不对就返回false
print(f)

f=[i   for i in e if i%2!=0]#如果if对了就返回i，不对就不返回
print(f)

g=list(map(lambda x: x if x%2!=0 else None,e))
print(g)#一定要返回吗
res = list(filter(None, g)) #前面一项是要丢弃的
print(res)


# 1。先看map的场景

g=list(map(lambda x: x**2,e)) #map是对每个元素进行处理，每个都要返回值
print(g)

# 2.filter使用
def  add(a):
    return a%2==0 
	
	
def add2(a):
	if a%2==0:
		return True
		
print(list(filter(add2,[1,2,3,4])))#筛选符合条件的 True的返回   不用管else的情况  map要管

# 3.综合

# 如果 if放在for左边 相当于map

#放后面 相当于filter
import numpy as np
f=[1,2,3,4,5,6,7]
print(np.random.shuffle(f))
print(f)










