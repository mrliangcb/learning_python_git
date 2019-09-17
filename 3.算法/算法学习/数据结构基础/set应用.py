
aa={1,2,3}
a=set([1,2,3,5])
b=set([3,4,5])
print(a)


#求交并差集
print("\n\n ####### 交集并集差集 ########")
print('a:',a)
print('b',b)
print("求交集intersection:",a&b)
print("求并集union:",a|b)
print("求差集union:",b-a) #可以小-大

if 4 in a: print("4 in a")
if 3 in a: print("3 in a")



#增加元素
# a.add()

#删除
print("\n\n #######删除元素########")
c=a
print('原c:',c)
c.remove(3)
print('c删除3:',c)
# c.remove(100)#出错
c.discard(100) #即使set中没有100也不报错

# 删除所有元素 a.clear()




#长度
print("\n\n ####### 长度 ########")
print("长度:",len(a))

#判断子集
print("\n\n #######判断子集########")
print('a:',a,'b:',b)
print('b是a的子集吗:',b<=a)
print('[5]是a的子集吗:',set([5]).issubset(a))  #前是后的子集吗


#出集
print("\n\n ####### 出集 ########")
print('原a:',a)
print(a.pop(),a.pop(),a)#pop出左边的元素，为空则出错












