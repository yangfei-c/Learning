import torch
from torch import nn
def init_xavier(m):
    if type(m)==nn.Linear:
        nn.init.xavier_uniform_(m.weight)
def init_42(m):
    if type(m)==nn.Linear:
        nn.init.constant_(m.weight,42)
net = nn.Sequential(nn.Linear(4, 8), nn.ReLU(), nn.Linear(8, 1))
net[0].apply(init_xavier)
net[2].apply(init_42)
print(net[0].weight.data[0])
print(net[2].weight.data)