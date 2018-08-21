import numpy as np
A = np.arange(14,2,-1).reshape((3,4))
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
#返回累差值
print(np.diff(A))
#返回数列中非零元素的坐标
print(np.nonzero(A))
#返回排序后的数列
print(A)
print(np.sort(A))
#矩阵的反向
print(A.T)
print(np.transpose(A))
#矩阵相乘
print(A.T.dot(A))
#所有小于5的元素变为5，大于9的元素变为9
print(np.clip(A,5,9))