
#三.文件操作

file = open(path)
a = file.readlines()#按行读取，作为字符型  ['第一行'，'第二行']

#如果file.readline 就是得到一个字符型，内容为第一行

with open(r'.\trainLabels.csv', 'r') as f:
	lines = f.readlines()[1:]
	tokens = [i.rstrip().split(',') for i in lines]#rstrip('内容') 删除字符串末尾的'内容'
	#经过split
	#a=[[一行],[二行],['1','2']]#,为分隔符
	idx_label = dict((int(idx), label) for idx, label in tokens)#创建字典，数字：‘名字’
	print(tokens)



