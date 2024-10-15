#!/usr/bin/python3.10
# -*- coding: utf-8 -*-
# @Time    : 2024/10/15 9:37
# @Author  : YangFei
# @Email   : ccc420513@gmail.com
# @File    : verification.py
# @Software: PyCh

import torch
import torchvision
from PIL import Image

img_path=("../imgs/cat.webp")
img_test=Image.open(img_path)
if img_test is None:
    print("文件不存在，请检查路径!")
print(img_test)
transform=torchvision.transforms.Compose([
    torchvision.transforms.Resize((32,32)),
    torchvision.transforms.ToTensor()
])
img_test=transform(img_test)
img_test=torch.reshape(img_test,(1,3,32,32))
print(img_test.shape)
model=torch.load("../model/model_30",weights_only=False)
print(model)

model.eval()
with torch.no_grad():
    output=model(img_test)
print(output)
print(output.argmax(1))

