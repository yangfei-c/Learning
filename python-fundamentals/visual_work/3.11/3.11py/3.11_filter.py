#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: YangFei
@time: 2024/11/14 20:15 
@file: 3.20_testImage.11.py
@email: ccc420513@gmail.com
"""

import os
import cv2
import numpy as np

# 读取图像
image_paths=['../3.11_testImage/soft_test.jpg','../3.11_testImage/sharpened_test.jpg','../3.11_testImage/nonLinear_test.jpg']
images=[]
image_names=[]
for img_path in image_paths:
    image = cv2.imread(img_path)
    image_name=os.path.splitext(os.path.basename(img_path))[0]
    images.append(image)
    image_names.append(image_name)


def soft_filter(image):
    #软化滤波器
    '''
    用于减少图像中的噪声或细节
    下面将实现一个基于加权平均的软化滤波器。
    '''
    soft_kernel=np.array([
                        [1, 2, 1],
                        [2, 4, 2],
                        [1, 2, 1]])
    softened_image = cv2.filter2D(image, -1, soft_kernel)  # 应用滤波器
    soft_image = np.clip(softened_image, 0, 255).astype(np.uint8)  # 确保像素值在0-255之间
    return soft_image

def sharpened_filter(image):
    # 锐化滤波器
    '''
    图像边缘信息主要集中在其高频部分，噪声所在的频段主要在高频段
    原始图像在平滑处理之后，会出现图像边缘和图像轮廓模糊的情况
    图像锐化处理的目的是为了使图像的边缘、轮廓线以及图像的细节变得清晰，
    '''
    sharpened_kernel = np.array([
                        [1, 1, 1],
                        [1, -7, 1],
                        [1, 1, 1]])
    sharpened_image = cv2.filter2D(image, -1, sharpened_kernel)
    sharpened_image = np.clip(sharpened_image, 0, 255).astype(np.uint8)  # 确保值在0-255之间
    return sharpened_image

def nonlinear_diffusion_filter(image):
    num_iteration=30
    diffusion_strength=15
    step=0.25
    image = image.astype(np.float32)
    for _ in range(num_iteration):
        # 计算图像的梯度（使用Sobel算子）
        grad_x = cv2.Sobel(image, cv2.CV_32F, 1, 0, ksize=3)
        grad_y = cv2.Sobel(image, cv2.CV_32F, 0, 1, ksize=3)

        # 计算梯度的幅值
        grad_magnitude = np.sqrt(grad_x ** 2 + grad_y ** 2)

        #扩散函数
        diffusion_function= 1/ (1 + (grad_magnitude / diffusion_strength) ** 2)

        #计算梯度方向扩散
        div_x = cv2.Sobel(diffusion_function * grad_x, cv2.CV_32F, 1, 0, ksize=3)
        div_y = cv2.Sobel(diffusion_function * grad_y, cv2.CV_32F, 0, 1, ksize=3)
        image=image+step*(div_x+div_y)
        image= np.clip(image, 0, 255)
    return image
process_function=[soft_filter,sharpened_filter,nonlinear_diffusion_filter]
process=['软化','锐化','非线性扩散']
if len(images)==3:
    for i,(img,img_name,func,process) in enumerate(zip(images,image_names,process_function,process)):
        process_image = func(img)
        cv2.imwrite(f'../../3.11/3.11_processedImage/{img_name}_after_process.jpg', process_image)  # 保存锐化图像
        print(f"{process}图像已保存。")
else:
    print("图像读取失败，程序终止。")
