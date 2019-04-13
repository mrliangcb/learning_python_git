#对str操作
import numpy as np
import pandas as pd
import random
import glob
import os





#五replace用法
strr=r'abcdef'
page=1
strr=strr.replace('abc',str(page))#将str的'abc'换成后面的
print(strr)
#六、分解文件名
#head, tail = os.path.split(im_name)
# a = "hello,python,Good Night"
# a.split(',')
# ['hello', 'python', 'Good Night']

#七、os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
#topdown表示是 优先遍历top目录，否则是优先子目录
# top -- 是你所要遍历的目录的地址, 返回的是一个三元组(root,dirs,files)。
# root 所指的是当前正在遍历的这个文件夹的本身的地址
# dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
# files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)


#八、
# os.getcwd()#当前脚本路径
# os.path.dirname(path)#取得path路径的父路径
# os.path.basename(path)#取得路径的最后一项
#作用：可以先把数据分好类放在各个文件夹，然后用glob搜索全部图片，然后根据路径可以提取label和处理自定义数据


#九、format和eval的结合
#如果要读s1  s2 s3 等等变量，如何遍历
# for i in range(1,4):
	# name='{}{}'.format('s',i)#拼成's1'  's2'
	# s=eval(name)#找到这个变量并返回
	# print(s)



