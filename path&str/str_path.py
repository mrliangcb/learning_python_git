#对str操作
import numpy as np
import pandas as pd
import random
import glob
import os

#一、#format用法
print('hello {:0>3}'.format(1))#:.2f 保留小数点后两位
#:.2%百分比格式
#{:0>3}左边补0，直到整个数长度为3   <为右边补
#%.2f保留2位小数

# i= "%06d" %3#也一样


path=r'abc{0:05d}'.format(123)#这个写法比较好
print(path)

#二、join用法
print(' '.join('%5s' % classes[labels[j]] for j in range(4)))

#三、找出文件名glob用法
#path=r'C:\Users\mrliangcb\Desktop\note\extra_feature\nparray'
#tmp=glob.glob(r'{}\*.inkml'.format(path)) #找出符合条件的全名
#如果有多级目录还可以用*代替 例如a\*\*\*.inkml 中间*会自动遍历


#image_list = glob.glob(equal_path + r'*.png')
#for im_name in image_list:

#四、listdir用法
#tmp2=os.listdir(path)#获得当前文件夹下所有文件名

#五replace用法
str=r'abcdef'
str=str.replace('abc','hahaha')#将str的'abc'换成后面的

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

os.getcwd()#当前脚本路径
os.path.dirname(path)#取得path路径的父路径
os.path.basename(path)#取得路径的最后一项
#作用：可以先把数据分好类放在各个文件夹，然后用glob搜索全部图片，然后根据路径可以提取label和处理自定义数据

