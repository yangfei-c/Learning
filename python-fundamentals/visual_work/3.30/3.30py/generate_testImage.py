#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: YangFei
@time: 2024/11/17 16:33 
@file: generate_testImage.py
@project: ReLearn
@email: ccc420513@gmail.com
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt

# 创建测试图像
def create_test_image(image_size=(256, 256), block_size=8):
    img = np.zeros(image_size, dtype=np.uint8)

    # 添加渐变背景
    x = np.linspace(0, 255, image_size[1], dtype=np.uint8)
    gradient = np.tile(x, (image_size[0], 1))
    img = gradient.copy()

    # 添加一些几何图案
    cv2.rectangle(img, (50, 50), (200, 200), color=128, thickness=-1)  # 填充矩形
    cv2.circle(img, (128, 128), 40, color=200, thickness=-1)  # 填充圆

    # 添加高频线条
    for i in range(0, image_size[0], block_size * 2):
        cv2.line(img, (0, i), (image_size[1], i), color=64, thickness=1)

    # 转换为三通道图像（伪彩色）
    color_img = cv2.merge([img, img // 2, 255 - img])
    return color_img

test_image = create_test_image()

    # 保存测试图像
test_image_path = "../3.30testImage/test_image.png"
cv2.imwrite(test_image_path, test_image)
print(f"测试图像已保存为 {test_image_path}")


