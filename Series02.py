#Series常用方法
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
sdata = {'Ohio':35000,'Texas':71000,'Oregen':16000,'Utah':5000}
states = ['California','Ohio','Oregon','Texas']
obj0 = pd.Series(sdata)
obj1 = pd.Series(sdata,index=states)
obj2 = pd.isnull(obj1)
obj3 = pd.isna(obj1)
obj4 = obj0 + obj1
obj4.name = 'population'
obj4.index.name = 'state'
print('--obj0--')
print(obj0)
print('--obj1--')
print(obj1)
print('--obj2--')
print(obj2)
print('--obj3--')
print(obj3)
print('--obj4--')
print(obj4)