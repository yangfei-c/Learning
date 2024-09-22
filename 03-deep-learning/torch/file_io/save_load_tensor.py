import torch
from torch import nn
from torch.nn import functional as F
x=torch.tensor([2,1,23,1])
torch.save(x,'x_file')
x2=torch.load('x_file',weights_only=True)
print(x2)