#!/usr/bin/python3.10
# -*- coding: utf-8 -*-
# @Time    : 2024/10/7 19:17
# @Author  : YangFei
# @Email   : ccc420513@gmail.com
# @File    : nn_module.py
# @Software: PyCharm
import torch
from torch import nn

class module(nn.Module):

    def __init__(self) -> None:
        super().__init__()

    def forward(self,input):
        output=input+2
        return output

my=module()
x=torch.tensor(2.0)
y=my(x)
print(y)