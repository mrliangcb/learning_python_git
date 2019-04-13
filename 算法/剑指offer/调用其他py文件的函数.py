#外部调用一个python文件的函数
import python_mul as pym
import numpy as np

a=pym.mul2(np.array([1,2,3]))
print(a.a)