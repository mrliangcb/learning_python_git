import pandas as pd
import numpy as np
path=r'C:\Users\mrliangcb\Desktop\pyqt_test\result\1.csv'#遇到逗号算一个列分割，遇到\n转下一行
df1 = pd.read_csv(path) 
df2=df1

print(df1.shape[0])#243行
#准确率，先取出所有的角度，拼一个完成的角度矩阵
df2.loc[:,'angle']=range(242)
left_index=df1[(df1.loc[:,'que1']!=1) & (df1.loc[:,'que1']!=2)].index#这些是在左边的,不要急着赋值，先取index
df2.loc[left_index,'angle']=df2.loc[left_index,'que1']
right_index=df1[(df1.loc[:,'que3']!=1) & (df1.loc[:,'que3']!=2)].index#这些是在右边的,不要急着赋值，先取index
df2.loc[right_index,'angle']=df2.loc[right_index,'que3']
#df2.to_csv(r'C:\Users\mrliangcb\Desktop\pyqt_test\result\tongji\test.csv',sep=',',index=0)

#取出角度后，准确率=

#60度的情况
df_60=df2[df2.loc[:,'que2']==1]
df_60_false=df_60[df_60.loc[:,'answer']!=df_60.loc[:,'ground_true']]
error_60=df_60_false['angle'].tolist()

all=df_60.angle.value_counts().index.tolist()
error_rate_60=np.zeros(len(all))

for i in range(len(all)):
	while all[i] in error_60:
		error_rate_60[i]+=1
		error_60.remove(all[i])
print('error_result_oblique:\n',all,'\n',error_rate_60)

#90度情况
df_90=df2[df2.loc[:,'que2']==2]


df_90_false=df_90[df_90.loc[:,'answer']!=df_90.loc[:,'ground_true']]
error_90=df_90_false['angle'].tolist()


all2=df_90.angle.value_counts().index.tolist()
error_rate_90=np.zeros(len(all2))

for i in range(len(all2)):
	while all2[i] in error_90:
		error_rate_90[i]+=1
		error_90.remove(all2[i])
print('error_result_verticle:\n',all2,'\n',error_rate_90)