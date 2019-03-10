#Drop用法
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
obj0 = pd.Series(np.arange(5),index=['a','b','c','d','e'])
print('--obj0--')
print(obj0)
obj1 = obj0.drop('c')
print('--obj1--')
print(obj1)
obj2 = obj0.drop(['b','d'])
print('--obj2--')
print(obj2)
#inplace=True会将drop的元素清除
obj0.drop('d',inplace=True)
print('--obj0:inplace=True--')
print(obj0)
data0 = pd.DataFrame(np.arange(16).reshape((4,4)),
                    index=['Ohio','Colorado','Utah','NewYork'],
                    columns=['one','two','three','four'])
print('--data0--')
print(data0)
data1 = data0.drop(['Colorado','Ohio'])
print('--data1--')
print(data1)
data2 = data0.drop('two',axis=1)
print('--data2--')
print(data2)
data3 =data0.drop(['two','four'],axis='columns')
print('--data3--')
print(data3)