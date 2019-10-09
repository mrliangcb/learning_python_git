


# 最大子和的长度  同样和取最长的
# 有的题目会问长度

# 输入:
# {6,-3,-2,7,-15,1,2,2}
# {-2,-8,-1,-5,-9}
x=input().strip()[1:-1]
x=list(map(int,x.split(',')))
print(x)

# max_cal=0
# max_len=0
# for i in range(len(x)):#轮番做起点，找最大
	# for j in range(i,len(x)):
		# tem=sum(x[i:j+1])
		# if max_cal<tem:
			# max_cal=tem
			# max_len=j-i+1
			
# print(max_cal,max_len)

# 优化成 当我要i做起点的时候，是要i做单独一块，还是要i为起点的一块，使和更大
# 是否要i右边的一个（要的话，有两种，一是只要右边，一是要右边的一块）

# 如果不取的话，已有块的左边界就往右缩小，因为有可能丢掉左边的一个元素，可以导致吸入右边的一个序列，就赚翻了
# 比如有现成一块，最左边是10，丢掉10，右边有10个1，那就吸收这10个1进来(使自己的和比已有最大和更大或者不变但是长度增加)
# (或者使自己<=某个要求数，然后长度更长)，

# 所以左边界往右缩是 为了丢掉已有的一个数，看能不能换来一个更长的序列

# 因为找最大和，所以只要使自己和更大，就是纳入右边的子块
# [6 -3 -2 7 -15 1 2 2]
# [0  1  2 3  4  5 6 7] #真实下标
# [3  3  3 3  7  7 7 7] 作为尾节点 从尾开始，找最优子结构
# [8  2  5 7 -10 5 4 2]

# 新建一块 拿6还是拿6所在块呢？因为6所在块的和更大，所以拿[6 -3 -2 7] 这块 和为 8
# 右边收入-15 还是收入-15这块  都不收入因为会拉低自己
# 丢掉8 ，子和为2 如果收入-15，或者-10，对应新块子和(-13,-8)都不够原来的8大，所以不收进来
# 旧子块继续减少 和变成8，右边还是收不进来，继续减少，和变成7，重合了于是新起块
# 新起-15还是-10，那就-10(作为基地，每次是否纳入块都和基地比，而不是和最大和比)
# 子和

# max_sum=[0 for i in range(len(x))]
# max_sum[-1]=x[-1]
# max_over=[0 for i in range(len(x))]
# max_over[-1]=len(x)-1
# for i in range(len(x)-2,-1,-1):
	# print('进来')
	# if x[i]+max_sum[i+1]>=x[i]:#如果归入右边队伍，可以提升自己
		# max_sum[i]=x[i]+max_sum[i+1]
		# max_over[i]=max_over[i+1]
	# else:
		# max_sum[i]=x[i]
		# max_over[i]=i
# print(max_sum,max_over)

# # l左边界,r右边界
# r=-1#右边界指向第一个块末尾
# sum_loca=0#第一块和
# max_L=0
# max_all=0
# #设置左边界往右移
# for l in range(len(x)):
	
	# if r==len(x)-1:
		# # 如果右边界满了，则不用看了
		# break
	
	# while sum_loca==0 or (r<len(x)-1 and max_sum[r+1]+sum_loca>=sum_loca) :#两种情况右扩，一种是左边减没了local_sum==0 一种是左边还有 
		# #右边块的和 就是r+1的sum累计  
		# sum_loca+=max_sum[r+1]
		# r=max_over[r+1]#右指针走到右边一块的末尾
		
		
	# # 统计长度 j-i 
	# if sum_loca==max_all:#局部和=全局  取长的
		# if r-l+1>max_L:
			# max_L=r-l+1
	# if sum_loca>max_all:
		# max_all=sum_loca
		# max_L=r-l+1
		
	# print(max_L,max_all,sum_loca)
	# #左边右移，所以
	# print(x[l])
	# sum_loca=sum_loca-x[l]
	
	
# print(max_all,max_L)

# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        # 连续子和最大，含有负数
        # 先计算辅助序列，尽可能往右归
        x=array
        aft_sum=[0 for i in range(len(x))]
        aft_sum[-1]=x[-1]
        rig_bound=[0 for i in range(len(x))]
        rig_bound[-1]=len(x)-1
        start=1
        for i in range(len(x)-2,-1,-1):
            if x[i]+aft_sum[i+1]>=x[i]:#如果归入右边队伍，可以提升自己
                aft_sum[i]=x[i]+aft_sum[i+1]
                rig_bound[i]=rig_bound[i+1]
            else:
                aft_sum[i]=x[i]
                rig_bound[i]=i
        print('辅助队列',aft_sum,rig_bound)
        r=-1#右边界指向第一个块末尾
        local_sum=0#第一块和
        max_L=0
        all_sum=0
        for l in range(len(x)):
            if r==len(x)-1:
            # 如果右边界满了，则不用看了
                break
            #右边扩展
            while r<l or (r<len(x)-1 and aft_sum[r+1]+local_sum>=local_sum) :#两种情况右扩，一种是左边减没了local_sum==0 一种是左边还有 
            #原本i<j 是写local_sum==0 但如果有0元素就麻烦了
                #右边块的和 就是r+1的sum累计  
                local_sum+=aft_sum[r+1]
                r=rig_bound[r+1]
            #和全局做替换
            if local_sum==all_sum:#局部和=全局  取长的
                if r-l+1>max_L:
                    max_L=r-l+1
            elif local_sum>all_sum or start:
                all_sum=local_sum
                max_L=r-l+1
                start=0
                
            #左边右移
            local_sum=local_sum-x[l]
            print('结束',l,r,max_L,local_sum,all_sum)
        return all_sum
            
exa=Solution()
exa.FindGreatestSumOfSubArray(x)
            
            
            
            
            
