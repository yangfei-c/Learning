#!/usr/bin/python3.10
# -*- coding: utf-8 -*-
# @Time    : 2024/10/12 14:54
# @Author  : YangFei
# @Email   : ccc420513@gmail.com
# @File    : module_load.py
# @Software: PyCharm
import torch
from torch.nn import Sequential, Conv2d, ReLU,MaxPool2d,AvgPool2d,AdaptiveAvgPool2d,Linear,Dropout
from torchvision.models import VGG
torch.serialization.add_safe_globals([VGG,set,Sequential,Conv2d,ReLU,MaxPool2d,AvgPool2d,Linear,Dropout,AdaptiveAvgPool2d])

#方式1加载模型
# module=torch.load("../module/vgg16_method1.pth",weights_only=True)
# print(module)

#方式2加载模型
module2=torch.load("../module/vgg16_method2.pth",weights_only=True)
print(module2)