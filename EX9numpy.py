#数列分割
import numpy as np

A = np.arange(12).reshape((3,4))
print(A)
#横向分割
#对数列A横向(axis=1)分割为2部分
print(np.split(A,2,axis=1))
#纵向分割
#对数列A纵向(axis=0)分割为3部分
print(np.split(A,3,axis=0))
#不等量分割数列
print(np.array_split(A,3,axis=1))
#vsplite=纵向分割,hsplit=横向分割
print(np.vsplit(A,3))
print(np.hsplit(A,2))