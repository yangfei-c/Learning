#!/usr/bin/python3.10
# -*- coding: utf-8 -*-
# @Time    : 2024/10/13 13:00
# @Author  : YangFei
# @Email   : ccc420513@gmail.com
# @File    : my_model.py
# @Software: PyCharm
#搭建神经网络
import torch
from torch import nn


class M_model(nn.Module):
    def __init__(self) -> None:
        super(M_model,self).__init__()
        self.model=nn.Sequential(
            nn.Conv2d(3,32,5,1,2),
            nn.MaxPool2d(2),
            nn.Conv2d(32,32,5,1,2),
            nn.MaxPool2d(2),
            nn.Conv2d(32,64,5,1,2),
            nn.MaxPool2d(2),
            nn.Flatten(),
            nn.Linear(64*4*4,64),
            nn.Linear(64,10),
        )
    def forward(self,x):
        x=self.model(x)
        return x
# 测试网络正确性
if __name__=='__main__':
    m_model=M_model()
    input=torch.ones((64,3,32,32))
    output=m_model(input)
    print(output.shape)
