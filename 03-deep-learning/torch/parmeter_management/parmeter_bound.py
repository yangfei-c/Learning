import torch
from torch import nn
shared=nn.Linear(8,8)
net=nn.Sequential(nn.Linear(4,8),nn.ReLU(),shared,nn.ReLU(),shared,nn.ReLU(),nn.Linear(8,1))
X=torch.rand(size=(2,4))
net(X)
print(net[2].weight.data[0]==net[4].weight.data[0])
