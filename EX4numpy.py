import numpy as np

#初始化一个3*4，所有值为0的矩阵，数据类型为float32
a = np.zeros((3,4),dtype=np.float32)
print(a)
#初始化一个3*4，所有值为1的矩阵，数据类型为int32
b = np.ones((3,4),dtype=np.int32)
print(b)
#初始化一个3*4，所有值接近0(empty)的矩阵，数据类型为float32
c = np.empty((3,4),dtype=np.float32)
print(c)
#初始化一个数列，从10开始，步长为2，到20为止数列
d = np.arange(10,20,2)
print(d)
#生成一个3*4，从0到12的矩阵
e= np.arange(12).reshape((3,4))
print(e)
#生产一个数列，数列中从1开始到10，分为5段,同样可以通过reshape来变化为矩阵
f= np.linspace(1,10,6).reshape((2,3))
print(f)