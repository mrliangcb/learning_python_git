import numpy as np
import copy

#把路过的元素加入到
import numpy as np




gram=[[1,1,1,2],
	  [1,1,2,3],
	  [1,2,1,2],
	  [1,1,1,3]]
	  
b=[[1,3],[2,4]]
cnt=set()



def search(x,y):#包含该元素的连通区域内，走过的路记录到set，再统计连通量是多少
	if (x,y) in cnt:
		return
		
	
	me=gram[x][y]
	cnt.add((x,y))
	#走上边
	if x>0 and gram[x-1][y]==me:
		search(x-1,y)
	
	#走下边
	if x<len(gram)-1 and gram[x+1][y]==me:
		search(x+1,y)
	
	#走左边
	if y>0 and gram[x][y-1]==me:
		search(x,y-1)
	
	#走右边
	if y<len(gram[0])-1 and gram[x][y+1]==me:
		search(x,y+1)
	

search(0,0)
print(cnt)


def dele(cnt):
	
	m_dele=copy.deepcopy(gram)#二维list深拷贝(开辟新区)的唯一办法
	if len(cnt)>=3:
		for x,y in cnt:
			m_dele[x][y]=0
	return m_dele
dele_m=dele(cnt)
print(dele_m)

def drop(m): #reflash
	for x in range(len(m)-1,0,-1):#自底向上
		for y in range(len(m[0])):
			if m[x][y]==0:
			#while m[x][y]==0 and sum(m[:][y])!=0:#本元素=0就做
				print('删除:',m,x,y,m[1:x+1][y])
				m[1:x+1][y]=m[0:x][y]
				m[0][y]=0
				
drop(dele_m)
print('下落之后',dele_m)

# test=input()
# print(test)
# print(type(test))

a={(1,3),(5,6)}
b=[]
b.append(a)
a=set()
a.add((4,5))
b.append(a)
print((5,6) in b)

print(b)



	





















