# str处理，正则表达,print,文件处理
import numpy as np
import pandas as pd
import random
import glob
import os

### 1.  .format用法  
print('hello {:0>3}'.format(1))  
:.2f 保留小数点后两位  
:.2%百分比格式，且小数点后两位  
{:0>3}左边补0，直到整个数长度为3   <为右边补  
path=r'abc{0:05d}'.format(123)


### 2. join用法
print(' '.join('%5s' % classes[labels[j]] for j in range(4)))
str.join()
















































