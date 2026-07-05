import torch
from torch import nn
net=nn.Sequential(nn.Linear(4,8),nn.ReLU(),nn.Linear(8,1))
X=torch.rand(size=(2,4))
# print(net(X))
# print(net[0].state_dict())
# print(net[1].state_dict())#ReLu没有可学习参数输出为空
# print(net[2].state_dict())
#获取目标参数
# print(net[2].bias)
# print(net[2].bias.data)
#一次性获取参数
# print(*[(name,param.shape) for name,param in net[0].named_parameters()])
# print(*[(name,param.shape) for name,param in net.named_parameters()])

#从嵌套中获取参数
def block1():
    return nn.Sequential(nn.Linear(4,8),nn.ReLU(),nn.Linear(8,4),nn.ReLU())
def block2():
    net=nn.Sequential()
    for i in range(4):
        net.add_module(f'block{i}',block1())
    return net
rgnet=nn.Sequential(block2(),nn.Linear(4,1))
print(rgnet(X))
print(rgnet)
print(rgnet[0][1][0].bias.data)