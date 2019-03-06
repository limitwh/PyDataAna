#再索引
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
obj0 = pd.Series([4.5,7.2,-5.3,3.6],index=['d','b','a','c'])
print('--obj0--')
print(obj0)
obj1 = obj0.reindex(['a','b','c','d','e'])
print('--obj1--')
print(obj1)
obj2 = pd.Series(['blue','purple','yellow'],index=[0,2,4])
print('--obj2--')
print(obj2)
obj3 = obj2.reindex(range(6),method='ffill')
print('--obj3--')
print(obj3)
frame0 = pd.DataFrame(np.arange(9).reshape((3,3)),index=['a','c','d'],columns=['Ohio','Texas','California'])
print('--frame0--')
print(frame0)
frame1 = frame0.reindex(['a','b','c','d'])
print('--frame1--')
print(frame1)
states = ['Texas','Utah','California']
frame2 = frame0.loc[['a','b','c','d'],states]
print('--frame2--')
print(frame2)