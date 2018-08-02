import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-3,3,50)
y1=x**2
y2=2*x+1
#figure可以生成一个窗口；num=8:指定一个窗口号 figsize=(8,5):指定纵横坐标，y=8，x=5#
plt.figure(num=8,figsize=(8,5))
#指定线的颜色和式样
plt.plot(x,y1,color='red',linestyle='--')
plt.plot(x,y2)
#指定X轴范围
plt.xlim((-1,2))
#指定Y轴范围
plt.ylim((-2,2))
#指定X轴和Y轴的说明
plt.xlabel('this is x')
plt.ylabel('this is y')

plt.show()