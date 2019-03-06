#Series常用方法
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
obj0 = pd.Series([4,7,-5,3],index=['a','b','c','d'])
print('--obj0--')
print(obj0)
print('--obj0[\'a\']--')
print(obj0['a'])
print('--obj0[[\'c\',\'d\']]--')
print(obj0[['c','d']])
print('--obj0[obj0 > 1]--')
print(obj0[obj0 > 1])