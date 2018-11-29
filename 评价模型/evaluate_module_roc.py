#evaluate the module
#以下博客例子很好
#https://www.cnblogs.com/lc1217/p/6699377.html

import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.metrics import roc_auc_score
#预测正例和负例的效果

label=	[1,0,1,0,1,0,1,0,1,1]#10个ground_true ,1为有用positive，0为垃圾,
pre=	[1,0,1,0,1,0,0,0,0,0]#预测
positive_proba=	[0.9,0.9,0.9,0.2,0.9,0.2,0.9,0.2,0.9,0.9]
#
#

dict={'label':label,'pre':pre,'pro':positive_proba}
df1=pd.DataFrame(dict)
print(df1)

fpr,tpr,thresholds=metrics.roc_curve(df1['label'],df1['pre'],pos_label=1)
#第一个参数是guangtrue分类，第二是预测类，或者是positive的softmax概率(不是N的),三表明1才是positive

plt.plot(fpr,tpr)
plt.show()

#求面积
auc_score=roc_auc_score(df1['label'],df1['pre'])
print(auc_score)