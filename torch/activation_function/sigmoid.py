import matplotlib.pyplot as plt
import torch
from d2l import torch as d2l
# 创建张量 x，并启用梯度计算
x = torch.arange(-8.0, 8.9, 0.1, requires_grad=True)
# 计算 Sigmoid 函数的值
y = torch.sigmoid(x)
# 计算梯度
y.backward(torch.ones_like(x), retain_graph=True)
# 确保 x.grad 已经计算并且不是 None
if x.grad is None:
    raise ValueError("Gradient calculation failed or is not available.")
# 创建一个 1 行 2 列的子图布局
fig, axs = plt.subplots(1, 2, figsize=(12, 6))
# 绘制 Sigmoid 函数的子图
axs[0].plot(x.detach(), y.detach())
axs[0].set_xlabel('x')
axs[0].set_ylabel('sigmoid(x)')
axs[0].set_title('Sigmoid Function')

# 绘制 Sigmoid 函数导数的子图
axs[1].plot(x.detach(), x.grad)
axs[1].set_xlabel('x')
axs[1].set_ylabel('grad of sigmoid')
axs[1].set_title('Gradient of Sigmoid')

# 调整布局并显示图像
plt.tight_layout()
plt.show()
