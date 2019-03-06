#索引对象
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
obj0 = pd.Series(range(3),index=['a','b','c'])
indexobj = obj0.index
print('--obj0.index--')
print(indexobj)
print('--obj0.index[1:]--')
print(indexobj[1:])
labels = pd.Index(np.arange(3))
print('--labels--')
print(labels)
obj1 = pd.Series([1.5,-2.5,0],index=labels)
print('--obj1--')
print(obj1)
print('--obj1.index is labels--')
print(obj1.index is labels)