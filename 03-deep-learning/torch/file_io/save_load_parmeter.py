import torch
from torch import nn
from torch.nn import functional as F

class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.hidden=nn.Linear(20,256)
        self.output=nn.Linear(256,10)
    def forward(self,x):
        return self.output(F.relu(self.hidden(x)))

net=MLP()
X=torch.randn(size=(2,20))
Y=net(X)

#state_dict()字典，包含模型的所有可学习参数
torch.save(net.state_dict(),'mlp.params')
clone=MLP()
clone.load_state_dict(torch.load('mlp.params',weights_only=True))
print(clone.eval())
print(clone.training)