#索引，选择与过滤
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
#索引
obj0 = pd.Series(np.arange(4.),index=['a','b','c','d'])
print('--obj0--')
print(obj0)
print('--obj0[\'b\']--')
print(obj0['b'])
print('--obj0[2]--')
print(obj0[2])
print('--obj0[2:4]--')
print(obj0[2:4])
print('--obj0[[\'d\',\'c\',\'a\']]--')
print(obj0[['d','c','a']])
print('--obj0[[1,3]--')
print(obj0[[1,3]])
print('--obj0[obj0 > 2]--')
print(obj0[obj0 > 2])
print('ojb0[\'b\':\'c\'] = 5')
obj0['b':'c'] = 5
print(obj0)
data0 = pd.DataFrame(np.arange(16).reshape((4,4)),
                    index=['Ohio','Colorado','Utah','NewYork'],
                    columns=['one','two','three','four'])
print('--data0--')
print(data0)
print('--data0[\'two\']--')
print(data0['two'])
print('--data0[[\'three\',\'one\']]--')
print(data0[['three','one']])
print('--data0[:2]--')
print(data0[:2])