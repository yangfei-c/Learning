import matplotlib.pyplot as plt
import torch
from d2l import torch as d2l

# ReLU 函数曲线图
x = torch.arange(-8.0, 8.9, 0.1, requires_grad=True)
y = torch.relu(x)

# 创建子图，1行2列的布局
fig, axs = plt.subplots(1, 2, figsize=(10, 4))

# 第一个子图：ReLU 函数
axs[0].plot(x.detach(), y.detach())
axs[0].set_xlabel('x')
axs[0].set_ylabel('relu(x)')
axs[0].set_title('ReLU Function')

# 计算 ReLU 函数的导数并绘制
y.backward(torch.ones_like(x), retain_graph=True)
axs[1].plot(x.detach(), x.grad)
axs[1].set_xlabel('x')
axs[1].set_ylabel('grad of relu')
axs[1].set_title('Gradient of ReLU')

# 显示图像
plt.tight_layout()#自动调整布局防止子图重叠
plt.show()
