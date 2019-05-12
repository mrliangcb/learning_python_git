#贪心算法

#只是目前最优的算法
# 36块钱，能用几种最少数量纸币来配
#子问题最优解


# 找出众数   数目最多的那个
#序列不一定有众数  如1,2,3,
#只要计算到某个元素出现次数>n/2就可以停止了
#(1) 暴力法，循环，统计次数   ON^2
#(2) map，x:count_x  (函数，序列)  ON    字典     
a=[1,2]
a.insert(0,1)
import collections
queue=collections.deque()
queue.append(1)
queue.appendleft(2) #从左边插入  从右边直接是append   同理用pop 和popleft()
print(queue)


# (3) sort 排序  nlogn  每次比较就是o1      
# (4)分治   左右边同时找   
# (5)



# 122题 股票买卖时机
# [1,2,3,4,5]    
# 贪心算法 只要后一天价格比前一天高，就前一天买进  所以利润是4   On            
# DP动态规划   on
















