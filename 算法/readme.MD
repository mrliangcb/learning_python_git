# 算法

## 目录  
- 数据结构
> 数组  
> 队列  
> 列表
> 树
> 哈希表hashtable
> Disjoint Set / trie / trie /BloomFilter / LRU cache

- 算法  
> 前中后序遍历  
> 贪心算法  
> 递归  
> 深度优先，广度优先  
> 动态规划  
> 二分查找  
> graph  

## 复杂度  
o(1)常数复杂度   
o(log n) 对数复杂度 
o(n)线性时间复杂度  
o(n^2)平方  
o(2^n)指数  
按照最高复杂度  


```
o(1)常数次的都是o1
int n =1000;
for i in range n
print("hello"+n)
```

```
o(N) n*常  就是n  
for i in range n
print("hello"+n)
```

```
o(N^2) 
运行了n*n*常次，所以为o(n^2)
for i in range n
	for j in range n
		print("hello"+n)
```

```
for i in range factorial(n)
	print(常数次)
o(n!)阶乘次操作
```

o(n)的时候随着迭代次数的增加，对大数据operations数量就很小

优化算法举例：  
普通:  
```
y=0
for i in range n
	y=i+y
```

优化:  
```
y=n*(n+1)/2  不管n是多少，只运算一次
```

递归的问题:  
```
F(n)=F(n-1)+F(n-2)  

def a(n):
	if n==0 or n==1
		return n
	return a(n-1)+a(n-2) 
```
可以画叉树理解  
2^n复杂度  

这一课的14:30还没看  
















