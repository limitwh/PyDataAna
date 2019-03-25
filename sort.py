#排序与排名
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
#索引排序
obj0 = pd.Series(range(4),index=['d','a','b','c'])
print('--obj0.sort_index()--')
print(obj0.sort_index())
frame0 = pd.DataFrame(np.arange(8).reshape((2,4)),
                      index=['three','one'],
                      columns=['d','a','b','c'])
print('--frame0.sort_index()--')
print(frame0.sort_index())
print('--frame0.sort_index(axis=1)--')
print(frame0.sort_index(axis=1))
print('--frame0.sort_index(axis=1,ascending=False)--')
print(frame0.sort_index(axis=1,ascending=False))
#series的值排序
obj1 = pd.Series([4,7,-3,2])
print('--obj1.sort_values()--')
print(obj1.sort_values())
#指定排序列
frame1 = pd.DataFrame({'b':[4,7,-3,2],'a':[0,1,0,1]})
print('--frame1--')
print(frame1)
print('--frame1.sort_values(by=\'b\')--')
print(frame1.sort_values(by='b'))
#指定多列排开
print('--frame1.sort_values(by=[\'a\',\'b\'])--')
print(frame1.sort_values(by=['a','b']))
#排名
obj2 = pd.Series([7,-5,7,4,2,0,4])
print('--obj2.rank()--')
print(obj2.rank())
print('--obj2.rank(method=\'first\')--')
print(obj2.rank(method='first'))
#将值分配给组中的最大排名
print('--obj2.rank(ascending=False,method=\'max\')--')
print(obj2.rank(ascending=False,method='max'))
frame2 = pd.DataFrame({'b':[4.3,7,-3,2],'a':[0,1,0,1],'c':[-2,5,8,-2.5]})
print('--frame2--')
print(frame2)
print('--frame2.rank(axis=\'columns\')--')
print(frame2.rank(axis='columns'))