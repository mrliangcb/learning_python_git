import shutil
#三.文件操作

# file = open(path) #file指向地址
# a = file.readlines() #按行读取，作为字符型  ['第一行'，'第二行']

#如果file.readline 就是得到一个字符型，内容为第一行
a=os.listdir(path)
print(a)
for i in a:#遍历每个元素
	b=i.split(",")
	print(b)
	
with open(r'.\trainLabels.csv', 'r') as f: #f指向这个地址
	lines = f.readlines()[1:]
	tokens = [i.rstrip().split(',') for i in lines]#rstrip('内容') 删除字符串末尾的'内容'
	#经过split
	#a=[[一行],[二行],['1','2']]#,为分隔符
	idx_label = dict((int(idx), label) for idx, label in tokens)#创建字典，数字：‘名字’
	print(tokens)
	
#移动文件
# shutil.move(object,target) #将object移动到target里面，都为全名
#重命名
# os.rename(target,'C:\abcde')
#复制文件
# shutil.copytree("olddir","newdir") #olddir和newdir都只能是目录，且newdir必须不存在
# shutil.copy("源文件地址","目的路径+文件名") #old可以是文件全名/home/123.txt  new可以是一个目录/home/lcb/data
#源和目标都可以是文件夹或者文件
#