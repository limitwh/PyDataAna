import numpy as np
A = np.arange(2,14).reshape((3,4))
print(A)
#返回数列中最小值和最大值的位置
print(np.argmin(A))
print(np.argmax(A))
#返回平均值
print(np.mean(A))
print(A.mean())
print(np.average(A))
#返回中位数
print(np.median(A))
#返回累加值
print(np.cumsum(A))