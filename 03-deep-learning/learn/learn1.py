from mxnet import ndarray as nd#导包为
import numpy as np

''''
#数组创建
x=nd.random.normal(0,1,shape=(3,4))
y=nd.random.normal(0,1,shape=(3,4))
print(x)#打印
print(y)#打印
'''

'''
#获取基本属性
print(x.shape)#获取形状
print(x.size)#获取大小即总元素个数
'''

'''
#基本运算
print(x+y)
print(x*y)
print(nd.exp(y))#指数
print(nd.dot(x,y.T))#转置一个矩阵做乘法
'''

'''
#广播机制
a=nd.arange(3).reshape(3,1)
b=nd.arange(2).reshape(1,2)
print("a",a)
print("b",b)
print("a+b",a+b)
'''

'''
#ndarry和numpy相互转换
x=np.ones((2,3))
y=nd.array(x)
z=y.asnumpy()
print(type(x))
print(type(y))
print(type(z))
'''

'''
#替换操作
x=nd.ones((3,4))
y=nd.ones((3,4))
print(id(y))
y=x+y
print(id(y))
'''

