#!/usr/bin/python3.10
# -*- coding: utf-8 -*-
# @Time    : 2024/10/12 14:46
# @Author  : YangFei
# @Email   : ccc420513@gmail.com
# @File    : mode_save.py
# @Software: PyCharm
import torch
import torchvision

vgg16=torchvision.models.vgg16(pretrained=False)

#保存方式1,模型结构加参数
torch.save(vgg16,"../module/vgg16_method1.pth")

#保存方式2，模型参数，官方推荐
torch.save(vgg16.state_dict(),"../module/vgg16_method2.pth")
