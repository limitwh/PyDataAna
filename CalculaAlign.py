#算数对齐
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
ser1 = pd.Series([7.3,-2.5,3.4,1.5],index=['a','c','d','e'])
ser2 = pd.Series([-2.1,3.6,-1.5,4,3.1],index=['a','c','e','f','g'])
print('--ser1--')
print(ser1)
print('--ser2--')
print(ser2)
print('--ser1 + ser2--')
print(ser1 + ser2)
df1 = pd.DataFrame(np.arange(9.).reshape((3,3)),columns=list('bcd'),index=['Ohio','Texas','Colorado'])
df2 = pd.DataFrame(np.arange(12.).reshape((4,3)),columns=list('bde'),index=['Utah','Ohio','Texas','Oregon'])
print('--df1--')
print(df1)
print('--df2--')
print(df2)
print('--df1 + df2--')
print(df1 + df2)
df3 = pd.DataFrame(np.arange(12.).reshape((3,4)),columns=list('abcd'))
df4 = pd.DataFrame(np.arange(20.).reshape((4,5)),columns=list('abcde'))
df4.loc[1,'b']=np.nan
print('--df3--')
print(df3)
print('--df4--')
print(df4)
print('--df3 + df4--')
print(df3 + df4)
print('--df3.add(df4,fill_value=0)--')
print(df3.add(df4,fill_value=0))
#除法
print('--1/df3--')
print(1/df3)
#除法 - 效果同上
print('--df3.rdiv(1)--')
print(df3.rdiv(1))
print('--df3.reindex(columns=df4.columns,fill_value=0--')
print(df3.reindex(columns=df4.columns,fill_value=0))
arr0 = np.arange(12.).reshape((3,4))
print('--arr0--')
print(arr0)
print('--arr0[0]--')
print(arr0[0])
#numpy的广播机制
print('--arr0 - arr0[0]--')
print(arr0 - arr0[0])
frame0 = pd.DataFrame(np.arange(12.).reshape((4,3)),columns=list('bde'),index=['Utah','Ohio','Texas','Oregon'])
seriers0 = frame0.iloc[0]
print('--frame0--')
print(frame0)
print('--seriers0--')
print(seriers0)
#pandas的广播机制
print('--frame0 - seriers0--')
print(frame0 - seriers0)
#如果一个索引值不在dataframe的列中，也不在series的索引中，则会重建索引并形成联合
seriers1 = pd.Series(range(3),index=['b','e','f'])
print('--frame0 + series1--')
print(frame0 + seriers1)
#如果想改为在列上广播，在行上匹配，必须使用算数方法
seriers2 = frame0['d']
print('--frame0--')
print(frame0)
print('--series2--')
print(seriers2)
print('--frame0.sub(series2,axis=\'index\')--')
print(frame0.sub(seriers2,axis='index'))