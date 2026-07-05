import torch
import torch.nn.functional as F
from torch import nn

class centered_layer(nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self,X):
        return X-X.mean()

layer=centered_layer()
layer(torch.FloatTensor([1,2,3,4,5]))