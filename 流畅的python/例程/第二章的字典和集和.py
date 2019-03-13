#



a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3} 
c = dict(zip(['one', 'two', 'three'], [1, 2, 3])) #一列是关键字，一列是value
d = dict([('two', 2), ('one', 1), ('three', 3)]) 
e = dict({'three': 3, 'one': 1, 'two': 2})


#遍历创建字典
#idx_label = dict((int(idx), label) for idx, label in tokens)
r = range(5)
d = {n * 2: n for n in r if n < 3}
print(d)
for n in r:
	print(n)
	d.setdefault(n, 0)
print(d)

print(d[2])#按照key寻找
print(d.values())
print(d.keys())
print(d.items())

#自定义字典
from collections import UserDict

class mydict(UserDict):
	def __getitem__(self,key):#key是指name[]括号里面的东西，重写__getitem__这个方法，父类也有
		print('取数据',key)
		return super().__getitem__(key)#然后调用父类的__getitem__方法

d=mydict({1:2})
print(d[1])

#字典翻转
# new_dict = {v : k for k, v in dict.items()}



from types import MappingProxyType

d = {1: 1}
d_proxy = MappingProxyType(d)
print(d_proxy[1])
try:
	d_proxy[1] = 1
except Exception as e:
	print(repr(e))

d[1] = 2
print(d_proxy[1])

import pandas as pd
a=[['a','b','c'],[1,2,3],[1,2,3]]
print(a[0])
b=pd.DataFrame(a[1:],columns=a[0])
print(b)
c=b.loc[1,:].tolist()
e=b.loc[1,:].values
print(c)
print(e)


d[1] = 2
print(d_proxy[1])



