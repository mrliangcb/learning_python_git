

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




















