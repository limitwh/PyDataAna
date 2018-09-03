import numpy as np
A = np.arange(3,15).reshape((3,4))
print(A)
#矩阵从0行0列开始索引
print(A[2][2])
print(A[2,2])
#用冒号代替某行或者某列的所有数
print(A[2,:])
print(A[:,1])
print(A[2,2:3])
#利用for循环遍历矩阵的行
for row in A:
    print(row)
#利用矩阵置换遍历矩阵的列
for column in A.T:
    print(column)
#flatten(方法)/flat(属性)可以使矩阵序列化
print(A.flatten())
for item in A.flat:
    print(item)