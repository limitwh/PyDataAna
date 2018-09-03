import numpy as np
A = np.array([1,1,1])
B = np.array([2,2,2])
#数列的合并  上下合并
print(np.vstack((A,B)))
#数列的合并  左右合并
print(np.hstack((A,B)))
#可以看到上下合并与左右合并的维度的变化
print(A.shape,np.vstack((A,B)).shape,np.hstack((A,B)).shape)