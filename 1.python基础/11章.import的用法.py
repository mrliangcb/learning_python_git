
#关于import

#第一种
# import test
# 只要当前路径下有test.py文件，就可以连接进来   test.类名或者函数名，就可以调用   
# 如果test名字太长的话 可以后面加 as 自己定义名字

#第二种 
#当前路径下找到new文件夹，里面有个my_model模块
import new.my_model2 as model
#注意，有时候import不进来很可能是new这个文件夹的名字和一些关键字冲突了，例如test
#

#问题：引用的自定义module里面没有我写了的def 怎么办?
#可能原因： 1.读的module可能不是我自定义的这个，重名了   2.module名字有下划线(有时可以有时不可以)  
# https://zhuanlan.zhihu.com/p/36173202
# 看module或者类里面有什么  dir(类或者module)

























