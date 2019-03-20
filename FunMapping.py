#函数与映射
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
frame0 = pd.DataFrame(np.random.randn(4,3),columns=list('bde'),index=['Utah','Ohio','Texas','Oregon'])
print('--frame0--')
print(frame0)
print('--np.abs(frame0)--')
print(np.abs(frame0))
#使用dataframe的apply方法将行数应用到某一行还在某一列的一维数组
f = lambda x:x.max()-x.min()
print('--frame0.apply(f)--')
print(frame0.apply(f))
#应用到某行
print('--frame.apply(f,axis=\'columns\')--')
print(frame0.apply(f,axis='columns'))
#应用函数
def fun(x):
    return pd.Series([x.min(),x.max()],index=['min','max'])
print('--frame0.apply(fun)--')
print(frame0.apply(fun))
#逐元素应用使用applymap方法
format0 = lambda x: '%.2f' % x
print('--frame0.applymap(format0)--')
print(frame0.applymap(format0))
#逐元素应用到series使用map方法
print('--frame0[\'e\'].map(format0)--')
print(frame0['e'].map(format0))