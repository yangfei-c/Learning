#!/usr/bin/python3.10
# -*- coding: utf-8 -*-
# @Time    : 2024/11/15 11:01
# @Author  : YangFei
# @Email   : ccc420513@gmail.com
# @File    : 3.11_generate_testImage.py
# @Software: PyCharm
import numpy as np
import cv2

def generate_softTestImage():
    width, height = 256, 256
    gradient = np.zeros((height, width), dtype=np.uint8)
    # 创建横向渐变图像
    for i in range(width):
        gradient[:, i] = i
    # 添加一些随机噪声
    noise = np.random.normal(0, 30, (height, width))  # 均值为0，标准差为30的正态噪声
    noisy_image = np.clip(gradient + noise, 0, 255).astype(np.uint8)
    return noisy_image

def generate_sharpenedTestImage():
    # 创建一个白色背景的图像
    image = np.ones((256, 256, 3), dtype=np.uint8) * 255

    # 在图像上绘制一些几何形状
    # 绘制一个蓝色矩形
    cv2.rectangle(image, (50, 50), (200, 150), (255, 0, 0), -1)  # 红色矩形

    # 绘制一个绿色圆形
    cv2.circle(image, (150, 200), 40, (0, 255, 0), -1)  # 绿色圆形

    # 绘制一条红色直线
    cv2.line(image, (20, 200), (100, 100), (0, 0, 255), 2)  # 红色直线

    # 在图像中添加文本
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, 'Sharpness Test', (50, 230), font, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
    return image

def generate_nonLinearDiffusionTestImage():
    image = np.zeros((256, 256), dtype=np.uint8)

    # 在图像中添加一个白色矩形
    cv2.rectangle(image, (50, 50), (200, 200), 255, -1)

    # 在矩形内添加一个黑色圆形
    cv2.circle(image, (125, 125), 50, 0, -1)

    # 添加一些高斯噪声
    noise = np.random.normal(0, 30, (256, 256))  # 均值为0，标准差为30的噪声
    noisy_image = np.clip(image + noise, 0, 255).astype(np.uint8)
    return noisy_image

functions=[generate_softTestImage(),generate_sharpenedTestImage(),generate_nonLinearDiffusionTestImage()]
img_names=['soft_test.jpg','sharpened_test.jpg','nonLinear_test.jpg']
for _,(func,img_name) in enumerate(zip(functions,img_names)):
    cv2.imwrite(f'../../3.11/3.11_testImage/{img_name}', func)
    print(f'{img_name} 已经生成')