#数列的深复制
import numpy as np

A = np.arange(4)
print(A)
B=A
print(B)
B[1]=9
print(A)
#利用is来判断是否同一个对象
print(A is B)
#使用copy方法来深复制
C=A.copy()
C[1]=20
print(A)
print(C)
print(C is A)