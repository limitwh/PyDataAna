#数列合并
import numpy as np
A = np.array([1,1,1])
B = np.array([2,2,2])
#数列的合并  上下合并
print(np.vstack((A,B)))
#数列的合并  左右合并
print(np.hstack((A,B)))
#可以看到上下合并与左右合并的维度的变化
print(A.shape,np.vstack((A,B)).shape,np.hstack((A,B)).shape)
#添加维度
print(A[np.newaxis,:])
print(A[np.newaxis,:].shape)
print(B[:,np.newaxis])
print(B[:,np.newaxis].shape)
#多个数列合并,通过设置axis来决定纵向合并或者横向合并
C=np.concatenate((A[:,np.newaxis],B[:,np.newaxis],B[:,np.newaxis],A[:,np.newaxis]),axis=0)
print(C)