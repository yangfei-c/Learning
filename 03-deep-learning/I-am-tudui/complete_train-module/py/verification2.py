#!/usr/bin/python3.10
# -*- coding: utf-8 -*-
# @Time    : 2024/10/15 11:13
# @Author  : YangFei
# @Email   : ccc420513@gmail.com
# @File    : verification2.py
# @Software: PyCharm
import torch
import torch.nn as nn
import torchvision
from PIL import Image

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

# 图片路径列表
img_paths = ["../imgs/dog.jfif", "../imgs/bird.jfif", "../imgs/airplane.jfif", "../imgs/cat.webp",
             "../imgs/deer.jfif","../imgs/truck.jfif","../imgs/ship.jfif",
             "../imgs/frog.jfif","../imgs/horse.jfif","../imgs/automobile.jfif",]
# CIFAR-10 数据集中的目标类别列表
targets = ['airplane', 'automobile', 'bird', 'cat', 'deer',
           'dog', 'frog', 'horse', 'ship', 'truck']

# 图片预处理步骤
transform = torchvision.transforms.Compose([
    torchvision.transforms.Resize((32, 32)),  # 调整图片大小为 (32, 32)
    torchvision.transforms.ToTensor()  # 将图片转换为 Tensor
])

# 加载模型
model = torch.load("../model/model_36", weights_only=False,map_location=torch.device('cpu'))
model.eval()

# 遍历每张图片进行验证
for i, img_path in enumerate(img_paths):
    try:
        # 加载图片
        img_test = Image.open(img_path)

        # 进行预处理
        img_test = transform(img_test)

        # 调整图片维度为模型输入格式
        img_test = torch.reshape(img_test, (1, 3, 32, 32))

        # 使用模型进行预测
        with torch.no_grad():
            output = model(img_test)

        # 获取预测的类别索引
        predicted_class_idx = output.argmax(1).item()

        # 获取模型预测的类别和真实的目标类别
        predicted_label = targets[predicted_class_idx]
        # 打印结果
        print(f"Image: {img_path}")
        print(f"Model Prediction: {predicted_label}")
        print("-" * 30)

    except Exception as e:
        print(f"Error processing image {img_path}: {e}")
