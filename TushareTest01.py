import tushare as ts
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
ts_token = 'f83c630c321cb7b66e6088cc8421ca1fb91e14ea4ad0866177a7d109'
ts.set_token(ts_token)
pro = ts.pro_api()
#df0 = pro.daily(ts_code='000055.SZ', start_date='20190101', end_date='20190407')
#print(df)
df1 = ts.pro_bar(api=pro, ts_code='000055.SZ', start_date='20190101', end_date='20190408', ma=[5, 20, 50])
print(df1)