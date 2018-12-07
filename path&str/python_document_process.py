#
import os
import shutil

a=os.listdir(path)
print(a)
for i in a:#遍历每个元素
	b=i.split(",")
	print(b)
	
#移动文件
# shutil.move(object,target) #将object移动到target里面，都为全名
#重命名
# os.rename(target,'C:\lcb\learning_python_git\extradoc\TP-MLP\which_symbol\serve_version\b\abcde')
#复制文件
# shutil.copytree("olddir","newdir") #olddir和newdir都只能是目录，且newdir必须不存在
# shutil.copy("./hoem/123.png","./home/dir") #olddir和newdir都只能是目录，且newdir必须不存在
#源和目标都可以是文件夹或者文件

