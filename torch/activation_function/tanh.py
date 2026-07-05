import matplotlib.pyplot as plt
import torch
x = torch.arange(-8.0, 8.9, 0.1, requires_grad=True)
y=torch.tanh(x)
y.backward(torch.ones_like(x),retain_graph=True)
if x.grad is None:
    raise ValueError("Gradient calculation failed or is not available.")
fig, axs = plt.subplots(1, 2, figsize=(12, 6))
# 绘制 tanh 函数的子图
axs[0].plot(x.detach(), y.detach())
axs[0].set_xlabel('x')
axs[0].set_ylabel('tanh(x)')
axs[0].set_title('tanh Function')

axs[1].plot(x.detach(), x.grad)
axs[1].set_xlabel('x')
axs[1].set_ylabel('grad of tanh')
axs[1].set_title('Gradient of tanh')
# 调整布局并显示图像
plt.tight_layout()
plt.show()