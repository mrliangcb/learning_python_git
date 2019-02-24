#os
import os
import glob

path=r'C:\Users\mrliangcb\Desktop\note\extra_feature'
a = os.listdir(path)#返回此文件夹下的所有文件及文件夹
print(a)#一个list，每个元素为一个str   文件名

path=r'C:\Users\mrliangcb\Desktop\note\extra_feature\*.txt'
tmp=glob.glob(path)#找到符合条件的文件，返回路径，一个元素为一个str，路径
print(tmp)

file_dir=r'C:\Users\mrliangcb\Desktop\pyqt_test\result'
for root, dirs, files in os.walk(file_dir):
	#print(root) #当前目录路径  
	#print(dirs) #当前路径下所有子目录  
	print(files) #当前路径下所有非目录子文件  
name=int(files[0][0])

b=os.listdir(file_dir)