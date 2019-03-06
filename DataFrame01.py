#DataFrame常用方法
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
data = {'states':['Ohio','Ohio','Ohio','Navada','Navada','Navada'],
        'year':[2000,2001,2002,2001,2002,2003],
        'pop':[1.5,1.7,3.6,2.4,2.9,3.2]}
frame0 = pd.DataFrame(data)
print('--frame0--')
print(frame0)
#head只显示前5个元素
print('--frame0.head()--')
print(frame0.head())
frame1 = pd.DataFrame(data,columns=['year','states',''])
print('--frame1--')
print(frame1)
frame2 = pd.DataFrame(data,columns=['year','states','pop','debt'],index=['one','two','three','four','five','six'])
print('--frame2--')
print(frame2)
print('--frame2[\'states\']--')
print(frame2['states'])
print('--frame2.year--')
print(frame2.year)
print('--frame2.loc[\'five\']--')
print(frame2.loc['five'])