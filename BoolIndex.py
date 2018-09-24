#布尔索引
import numpy as np
#布尔数组中，下标为0,3,4的位置是True，因此将会取出目标数组中对应位置的元素。
A = np.arange(7)
boolarr1 = np.array([True,False,False,True,True,False,False])
print(A)
print(A[boolarr1])
#布尔数组中，下标为1的位置是True，因此将会取出目标数组中第1行。
B = np.arange(12).reshape((3,4))
print(B)
boolarr2 = np.array([False,True,False])
print(B[boolarr2])
#
names = np.array(['Ben','Tom','Jack'])
print(names == 'Ben')
print('-----')
print(B[names == 'Ben'])
print('-----')
print(B[names != 'Ben'])