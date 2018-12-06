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

# i= "%06d" %3#也一样

path=r'abc{0:05d}'.format(123)#这个写法比较好
print(path)

#二、join用法
print(' '.join('%5s' % classes[labels[j]] for j in range(4)))

#三、找出文件名glob用法
#path=r'C:\Users\mrliangcb\Desktop\note\extra_feature\nparray'
#tmp=glob.glob(r'{}\*.inkml'.format(path)) #找出符合条件的全名

#四、listdir用法
#tmp2=os.listdir(path)#获得当前文件夹下所有文件名

#五replace用法
str=r'abcdef'
str=str.replace('abc','hahaha')#将str的'abc'换成后面的

#六、



