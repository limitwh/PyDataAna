#DataFrame常用方法
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
data = {'Navada':{2001:2.4,2002:2.9},
        'Ohio':{2000:1.5,2001:1.7,2002:3.6}}
frame0 = pd.DataFrame(data)
frame0.index.name = 'year'
frame0.columns.name = 'states'
print('--frame0--')
print(frame0)
print('--frame0.T--')
print(frame0.T)
frame1 = pd.DataFrame({'Ohio':frame0['Ohio'][:-1],'Navada':frame0['Navada'][:2]})
print('--frame1--')
print(frame1)