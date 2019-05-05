#https://blog.csdn.net/gxlmsw1314/article/details/51684104
#knn算法
#计算这个点和其他已知点的距离，然后把已知点[1,2,2,'a']排序放到数组，取前K个作为邻居
import numpy as np
import operator
import csv
import random
import math

def eucdis(instance1,instance2,length):#根据length个特征，计算出两个目标的距离
	distance=0
	for x in range(length): #有多少个特征
		distance+=pow((instance1[x]-instance2[x]),2)
		print('长度为',x)
	return math.sqrt(distance)

def getnei(train,test,k):#选出k个邻居
	dis=[]
	length=len(test)#原来是加上-1的
	for x in range(len(train)):#有X个点已知训练点
		dist=eucdis(test,train[x],length)#
		dis.append((train[x],dist))#把每个已知点和距离绑在一起，放入dis
	dis.sort(key=operator.itemgetter(1))#根据元祖的第二位进行排序，也就是距离
	neigh=[]
	for x in range(k):
		neigh.append(dis[x][0])#把排序好了的点特征拿进来
	return neigh

train=[[2,2,2,'a'],[4,4,4,'b']]
test=[5,5,5]
k=1
nei=getnei(train,test,1)
print(nei)







