#!/usr/bin/python3.10
# -*- coding: utf-8 -*-
# @Time    : 2024/10/15 16:06
# @Author  : YangFei
# @Email   : ccc420513@gmail.com
# @File    : test.py
# @Software: PyCharm
import torch
import torch.nn as nn
import torch.nn.functional as F


# 定义残差块
class Conv_Block(nn.Module):
    def __init__(self, inchannel, outchannel, res=True):
        super(Conv_Block, self).__init__()
        self.res = res  # 是否带残差连接
        self.left = nn.Sequential(
            nn.Conv2d(inchannel, outchannel, kernel_size=(3, 3), padding=1, bias=False),
            nn.BatchNorm2d(outchannel),
            nn.ReLU(inplace=True),
            nn.Conv2d(outchannel, outchannel, kernel_size=(3, 3), padding=1, bias=False),
            nn.BatchNorm2d(outchannel),
        )

        # 如果输入输出通道数不同，使用shortcut进行1x1卷积调整
        self.shortcut = nn.Sequential()
        if inchannel != outchannel:
            self.shortcut = nn.Sequential(
                nn.Conv2d(inchannel, outchannel, kernel_size=(1, 1), bias=False),
                nn.BatchNorm2d(outchannel)
            )
        self.relu = nn.ReLU(inplace=True)

    def forward(self, x):
        out = self.left(x)
        if self.res:
            out += self.shortcut(x)
        out = self.relu(out)
        return out


# 定义新的 M_model
class M_model(nn.Module):
    def __init__(self):
        super(M_model, self).__init__()

        # 定义4个卷积块
        self.block1 = Conv_Block(inchannel=3, outchannel=64)
        self.block2 = Conv_Block(inchannel=64, outchannel=128)
        self.block3 = Conv_Block(inchannel=128, outchannel=256)
        self.block4 = Conv_Block(inchannel=256, outchannel=512)

        # 全连接层
        self.classifier = nn.Sequential(
            nn.Flatten(),  # Flatten层
            nn.Dropout(0.4),
            nn.Linear(512 * 2 * 2, 256),  # 根据特征图尺寸计算输入到全连接层的大小
            nn.ReLU(),
            nn.Linear(256, 64),  # 第二个全连接层
            nn.ReLU(),
            nn.Linear(64, 10)  # 输出层（10类）
        )

        self.maxpool = nn.MaxPool2d(kernel_size=2)  # 最大池化层，用于每个卷积块后缩减尺寸

    def forward(self, x):
        # 通过每个卷积块和池化层
        out = self.block1(x)
        out = self.maxpool(out)
        out = self.block2(out)
        out = self.maxpool(out)
        out = self.block3(out)
        out = self.maxpool(out)
        out = self.block4(out)
        out = self.maxpool(out)

        # 通过全连接层
        out = self.classifier(out)
        return out


# 测试新的模型结构
model = M_model()
print(model)
