#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: YangFei
@time: 2024/11/14 21:05 
@file: 3.20_testImage.20.py
@email: ccc420513@gmail.com
"""
import cv2
import numpy as np

# 构建高斯金字塔
def gaussian_pyramid(image, levels):
    gaussian_pyramid = [image]
    for i in range(levels - 1):
        image = cv2.pyrDown(image)
        gaussian_pyramid.append(image)
    return gaussian_pyramid

# 构建拉普拉斯金字塔
def laplacian_pyramid(gaussian_pyramid):
    laplacian_pyramid = []
    for i in range(len(gaussian_pyramid) - 1):
        next_gaussian = cv2.pyrUp(gaussian_pyramid[i + 1],#这里确保尺寸一致用于后续做差
                                  dstsize=(gaussian_pyramid[i].shape[1], gaussian_pyramid[i].shape[0]))
        laplacian = cv2.subtract(gaussian_pyramid[i], next_gaussian)
        laplacian_pyramid.append(laplacian)
    laplacian_pyramid.append(gaussian_pyramid[-1])  # 添加最后一层的高斯图像
    return laplacian_pyramid

# 混合拉普拉斯金字塔
def blend_pyramids(laplacian_pyr1, laplacian_pyr2, mask_pyr):
    blended_pyramid = []
    for l1, l2, mask in zip(laplacian_pyr1, laplacian_pyr2, mask_pyr):
        blended = l1 * mask + l2 * (1 - mask)
        blended_pyramid.append(blended)
    return blended_pyramid

# 重建图像
def reconstruct_from_pyramid(laplacian_pyramid):
    image = laplacian_pyramid[-1]
    for i in range(len(laplacian_pyramid) - 2, -1, -1):
        image = cv2.pyrUp(image, dstsize=(laplacian_pyramid[i].shape[1], laplacian_pyramid[i].shape[0]))
        image = cv2.add(image, laplacian_pyramid[i])
    return image

#输入两幅图像和掩模图像进行金字塔融合
def laplacian_pyramid_blending(image1, image2, mask, levels=5):
    # 构建两个图像的高斯和拉普拉斯金字塔
    gaussian_pyr1 = gaussian_pyramid(image1, levels)
    gaussian_pyr2 = gaussian_pyramid(image2, levels)
    laplacian_pyr1 = laplacian_pyramid(gaussian_pyr1)
    laplacian_pyr2 = laplacian_pyramid(gaussian_pyr2)
    # 构建掩模图像的高斯金字塔
    mask_gaussian_pyr = gaussian_pyramid(mask, levels)
    # 将掩模二值化以便用于混合
    mask_gaussian_pyr = [m.astype(np.float32) / 255 for m in mask_gaussian_pyr]
    # 混合拉普拉斯金字塔
    blended_pyramid = blend_pyramids(laplacian_pyr1, laplacian_pyr2, mask_gaussian_pyr)
    # 从混合的拉普拉斯金字塔重建最终图像
    blended_image = reconstruct_from_pyramid(blended_pyramid)

    return blended_image
#测试图像准备
def testImage_prepare():
    image1 = cv2.resize(cv2.imread('../3.20_testImage/input_1.png'),(128,128))
    image2 = cv2.resize(cv2.imread('../3.20_testImage/input_5.png'),(128,128))
    height, width = image1.shape[:2]
    mask = np.zeros((height, width), dtype=np.uint8)
    for i in range(width):
        mask[:, i] = int((i / width) * 255)  # 从左到右渐变
    # 确保 mask 和图像尺寸一致
    assert mask.shape[:2] == image1.shape[:2], "Mask size doesn't match image size!"
    cv2.imwrite('../3.20_testImage/mask.jpg', mask)
    mask = np.stack([mask] * 3, axis=-1)  # 将单通道 mask 扩展为 (128,128,3)
    return image1,image2,mask
# # 测试
# image1 = cv2.imread('../3.20_testImage/input_1.png')
# image2 = cv2.imread('../3.20_testImage/input_5.png')
# image1 = cv2.resize(image1, (128, 128))
# image2 = cv2.resize(image2, (128, 128))
# height, width = image1.shape[:2] # 假设图像尺寸
# mask = np.zeros((height, width), dtype=np.uint8)
# for i in range(width):
#     mask[:, i] = int((i / width) * 255)  # 从左到右渐变
#
# # 确保 mask 和图像尺寸一致
# assert mask.shape[:2] == image1.shape[:2], "Mask size doesn't match image size!"
# cv2.imwrite('../3.20_testImage/mask.jpg', mask)
#
# # 确保 mask 是三通道图像
# mask = np.stack([mask] * 3, axis=-1)  # 将单通道 mask 扩展为 (128,128,3)
result = laplacian_pyramid_blending(testImage_prepare()[0], testImage_prepare()[1], testImage_prepare()[2], levels=5)
if result is not  None:
    print(f'处理成功')
else:
    print('处理失败')
cv2.imwrite('../3.20processImage/blended_image.jpg', result)

