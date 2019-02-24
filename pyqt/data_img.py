import pandas as pd
import matplotlib.pyplot as plt

type1=list(range(20,68,4))
print(type1)

los1=[5,7,8,6,4,5,3,4,3,2,0,0]


df1=pd.DataFrame({'err_rate%':los1},index=type1)

df1.plot(kind='line')
df1.plot(kind='bar')
plt.show()