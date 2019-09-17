
# 方法一：可改变输入数组
# partition快排序，然后选左边的K个



def knum(tinput, k):

	if k >len(tinput) or not tinput:
		return []
	return quick_sort(tinput)[:k]
	#tinput.sort()
	#实现一个快速排序
def quick_sort(array):
	if not array:
		return []
	pivot=array[0]
	left=quick_sort([x for x in array[1:] if x<pivot])
	right=quick_sort([x for x in array[1:] if x>=pivot])
	return left+[pivot]+right

	


# 方法二: 数据量很大
# 容量为K的大顶堆小顶堆 
# 这里小的数要留下，大的数走人，所以用大顶堆，每次插入一个新元素，都要堆内K个数快排序，logk。所以总集n:nlogk


# list()和[]有什么区别
# 大顶堆做法  nlogk    选5个同学参加比赛，选好之后，又来一个新的，新的要和最高分的人PK，如果高分的人要淘汰
# 但是大顶堆写法复杂，不利于立马写出，所以可以尝试红黑树
def kmin(tinput, k):
	n = len(tinput) #全集的长度
	if k <= 0 or k > n:#K应该>0并且<tinput
		return list()
	# 建立大顶堆
	
	for i in range(int(k / 2) - 1, -1, -1):#k/2-1开始，到-1
		heapAjust(tinput, i, k - 1)#进堆
		
	for i in range(k, n):
		if tinput[i] < tinput[0]:
			tinput[0], tinput[i] = tinput[i], tinput[0]
			# 调整前k个数
			self.heapAjust(tinput, 0, k - 1)
	print(tinput[:k])


def heapAjust(nums, start, end):#用数组来保存树
	temp = nums[start]
	# 记录较大的那个孩子下标
	child = 2 * start + 1
	while child <= end:
		# 比较左右孩子，记录较大的那个
		if child + 1 <= end and nums[child] < nums[child + 1]:
			# 如果右孩子比较大，下标往右移
			child += 1
		# 如果根已经比左右孩子都大了，直接退出
		if temp >= nums[child]:
			break
		# 如果根小于某个孩子,将较大值提到根位置
		nums[start] = nums[child]
		# nums[start], nums[child] = nums[child], nums[start]
		# 接着比较被降下去是否符合要求，此时的根下标为原来被换上去的那个孩子下标
		start = child
		# 孩子下标也要下降一层
		child = child * 2 + 1
	# 最后将一开始的根值放入合适的位置(如果前面是交换，这句就不要)
	nums[start] = temp


# 红黑树
# STL容器（这种方法复杂度和堆一样，只是这个好写）
# 

a={2,3,1,5} #set插入时，理论是无序的
print(a)  #
























