#嵌套列表推导式
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
some_tuples = [(1,2,3),(4,5,6),(7,8,9)]
flattened1 = [x for tup1 in some_tuples for x in tup1]
print('--flattened1--')
print(flattened1)
flattened2 = []
for tup2 in some_tuples:
    for x in tup2:
        flattened2.append(x)
print('--flattened2--')
print(flattened2)
#flattened1的嵌套推导式与for循环嵌套等价