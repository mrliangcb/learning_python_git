#evaluate the module
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.metrics import roc_auc_score

label=	[1,0,1,0,1,0,1,0,1,1]#10个
pre=	[1,0,1,0,1,0,0,0,0,0]
proba=	[1,0.2,0.9,0.2,0.9,0.2,0.9,0.2,0.9,0.9]#这样效果就最好了，预测1的时候概率很高，预测0的时候概率就很低
												#这个概率应该说是为1的概率，就是属于正类的概率，roc曲线整个过程针对的正类只有一个

dict={'label':label,'pre':pre,'proba':proba}
df1=pd.DataFrame(dict)
print(df1)

fpr,tpr,thresholds=metrics.roc_curve(df1['label'],df1['proba'])

plt.plot(fpr,tpr)
plt.show()

#求面积
auc_score=roc_auc_score(df1['label'],df1['proba'])
print(auc_score)