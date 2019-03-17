#一等函数

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']

print(sorted(fruits, key=len))#按照len来排序


fact = lambda x: 1 if x == 0 else x * fact(x-1)   #匿名函数，传入x

print(list(map(fact, range(6))))  #传入0到6，作为x输入

from functools import reduce
from operator import add
print('reduce函数')
print(reduce(add, range(101)))  #采用add函数，0到101的range，每次取两个来迭代

pip install chardet
chardet.detect(data)












