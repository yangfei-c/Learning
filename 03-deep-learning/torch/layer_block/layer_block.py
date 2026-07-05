import torch
from torch import nn
from torch.nn import functional as F
#第一场nn.Linear输入为20维输出为256维
#第二层nn.ReLU激活函数添加非线性
#第三层线性层输入256输出19
net=nn.Sequential(nn.Linear(20,256),nn.ReLU(),nn.Linear(256,19))

X=torch.rand(2,20)#rand0~1之间
#两个样本每个样本20个特征
print(net(X))
