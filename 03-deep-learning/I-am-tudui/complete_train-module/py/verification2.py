#!/usr/bin/python3.10
# -*- coding: utf-8 -*-
# @Time    : 2024/10/15 11:13
# @Author  : YangFei
# @Email   : ccc420513@gmail.com
# @File    : verification2.py
# @Software: PyCharm
import torch
import torchvision
from PIL import Image

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
model = torch.load("../model/model_26", weights_only=False)
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
