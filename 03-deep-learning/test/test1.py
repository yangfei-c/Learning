import mxnet.ndarray as nd
X = nd.array([[1, 2], [3, 4]])
y = nd.array([1, 1])

# 计算矩阵和向量的点积（或称作矩阵与向量的乘积）
result = nd.dot(X, y)

print(result)  # 输出: [2. 6.]