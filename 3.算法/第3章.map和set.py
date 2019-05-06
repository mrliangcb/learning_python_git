# 第3章.map 和 set 



# 哈希函数和哈希表
# 比如存10个同学的名字，然后利于查找，就用到哈希函数，比如'abc'这个名字，把a,b,c三个字符的asc码求和，然后对总人数10求模，就是取余，就是排名了  
# 计算排名的这个函数，就是哈希函数
# 问题：会有重复，一个排名对多个元素:哈希碰撞
# 拉链法:横向放元素
# 对比list、map、set   map可以理解为字典，集和就是map的key，但不重复
# map/set 都有哈希(搜索的复杂度o1)和树(排好顺序)两种实现形式    若不要求搜索过程有序，则优先用哈希表
#


# 复杂度怎么会有log:
# [1,2,3,4,5,6,7]  假设我们要找数组中6值的位置，我们假设每次都是做最坏打算的操作，中点为4，最坏我们搜索左边,即1/2 * 7= 3次,剩下4元，我们又分一半,4/2=2是先搜左边4,5,
# 然后分半2/2=1 搜7,最后才是6    7*(1/2)^3=1    n=2^k  注意这里是搜索（二分搜索）不是遍历


# 题目 242   anagram 字母都一样，但顺序不同的两个词.  cat  tac  atc   判断两个词是否这种情况
# 快排序NlogN
# map计数{letter:出现次数}   因为要遍历字符串On  插入删除查询都O1  这个速度比快排序快

#快排序  NlogN
def test(s,t):
	return sorted(s)==sorted(t) #先各自排序，然后判断是否一模一样

	
# map 哈希
def test2(s,t):
	dic1,dic2={},{}
	for item in s:
		dic1[item]=dic1.get(item,0)+1#dict.get(key, default=None)返回指定key的value，如果不存在，则返回默认的0
	for item in t:
		dic2[item]=dic2.get(item,0)+1
	return dic1==dic2

print(test2('dabc','bacd'))


# two sum   three sum 用map解决 
# [2,7,11,15]   和9   返回下标[0,1]
# 法一：暴力for循环,On^2
# 法二：set x+y=9转化为y=9-x   On找x,set为9-x(O1)    
#

# 三数之和  
# [-1 0 1 2 -1 -4 ]    a+b+c=0
# 暴力循环 On^3
# c=-a-b  




















