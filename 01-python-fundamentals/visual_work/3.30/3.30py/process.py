#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: YangFei
@time: 2024/11/17 16:33 
@file: process.py
@project: ReLearn
@email: ccc420513@gmail.com
"""
import cv2
import numpy as np
from scipy.fftpack import dct, idct


# 读取JPEG图像
def read_jpeg(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img


# 分块函数
def blockify(image, block_size):
    h, w = image.shape[:2]
    return image.reshape(h // block_size, block_size, -1, block_size).swapaxes(1, 2)


# 合并块
def unblockify(blocks):
    n_blocks_h, n_blocks_w, block_h, block_w = blocks.shape
    return blocks.swapaxes(1, 2).reshape(n_blocks_h * block_h, n_blocks_w * block_w)


# DCT与IDCT变换
def dct_2d(block):
    return dct(dct(block.T, norm='ortho').T, norm='ortho')


def idct_2d(block):
    return idct(idct(block.T, norm='ortho').T, norm='ortho')


# 反量化
def dequantize(blocks, quantization_table):
    return blocks * quantization_table


# 块边界平滑
def smooth_block_boundaries(image, block_size=8):
    smoothed = image.copy()
    h, w, c = smoothed.shape
    for i in range(block_size, h, block_size):
        smoothed[i - 1:i + 1, :, :] = cv2.GaussianBlur(smoothed[i - 1:i + 1, :, :], (3, 3), 0)
    for j in range(block_size, w, block_size):
        smoothed[:, j - 1:j + 1, :] = cv2.GaussianBlur(smoothed[:, j - 1:j + 1, :], (3, 3), 0)
    return smoothed


# 高频色度恢复
def restore_chroma(ycbcr_img, block_size=8):
    y, cb, cr = cv2.split(ycbcr_img)

    # 恢复色度分量到更高分辨率
    cb_restored = cv2.resize(cb, (y.shape[1], y.shape[0]), interpolation=cv2.INTER_CUBIC)
    cr_restored = cv2.resize(cr, (y.shape[1], y.shape[0]), interpolation=cv2.INTER_CUBIC)

    # 合并恢复后的通道
    return cv2.merge([y, cb_restored, cr_restored])

# 主函数
def jpeg_deblocking(image_path, quantization_table):
    # 读取图像
    img = read_jpeg(image_path)

    # 转换为YCbCr空间
    ycbcr = cv2.cvtColor(img, cv2.COLOR_RGB2YCrCb)

    # 分块并进行DCT逆变换
    blocks = blockify(ycbcr[:, :, 0], block_size=8)
    dequantized_blocks = np.array([[dequantize(dct_2d(block), quantization_table) for block in row] for row in blocks])
    restored_y = unblockify(np.array([[idct_2d(block) for block in row] for row in dequantized_blocks]))

    # 更新亮度分量
    ycbcr[:, :, 0] = np.clip(restored_y, 0, 255)

    # 恢复高频色度信号
    restored_ycbcr = restore_chroma(ycbcr)

    # 转换回RGB空间
    restored_img = cv2.cvtColor(restored_ycbcr, cv2.COLOR_YCrCb2RGB)

    # 平滑块边界
    final_img = smooth_block_boundaries(restored_img)

    return final_img


# 测试程序
if __name__ == "__main__":
    # 示例JPEG量化表（可以从JPEG头提取更精准的量化表）
    quantization_table = np.array([
        [16, 11, 10, 16, 24, 40, 51, 61],
        [12, 12, 14, 19, 26, 58, 60, 55],
        [14, 13, 16, 24, 40, 57, 69, 56],
        [14, 17, 22, 29, 51, 87, 80, 62],
        [18, 22, 37, 56, 68, 109, 103, 77],
        [24, 35, 55, 64, 81, 104, 113, 92],
        [49, 64, 78, 87, 103, 121, 120, 101],
        [72, 92, 95, 98, 112, 100, 103, 99]
    ])

    # 输入图片路径
    input_image_path = "../3.30testImage/test_image.png"
    output_image_path = "../3.30processImage/process_image.png"

    # 去块处理
    result_img = jpeg_deblocking(input_image_path, quantization_table)

    # 保存结果
    cv2.imwrite(output_image_path, cv2.cvtColor(result_img, cv2.COLOR_RGB2BGR))
    print(f"去块处理完成，结果保存至 {output_image_path}")

