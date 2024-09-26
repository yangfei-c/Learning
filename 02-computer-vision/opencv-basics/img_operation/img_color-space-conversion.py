import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取原始图像
img_BGR = cv2.imread('../../img/ChenYao3.webp')

# 定义标题和颜色空间转换
titles = ['BGR', 'RGB', 'GRAY', 'HSV',
          'YCrCb', 'HLS', 'XYZ', 'LAB', 'YUV']
color_spaces = [
    img_BGR,  # BGR
    cv2.cvtColor(img_BGR, cv2.COLOR_BGR2RGB),  # RGB
    cv2.cvtColor(img_BGR, cv2.COLOR_BGR2GRAY),  # GRAY
    cv2.cvtColor(img_BGR, cv2.COLOR_BGR2HSV),  # HSV
    cv2.cvtColor(img_BGR, cv2.COLOR_BGR2YCrCb),  # YCrCb
    cv2.cvtColor(img_BGR, cv2.COLOR_BGR2HLS),  # HLS
    cv2.cvtColor(img_BGR, cv2.COLOR_BGR2XYZ),  # XYZ
    cv2.cvtColor(img_BGR, cv2.COLOR_BGR2LAB),  # LAB
    cv2.cvtColor(img_BGR, cv2.COLOR_BGR2YUV)   # YUV
]

# 调用 Matplotlib 显示处理结果
plt.figure(figsize=(12, 12))
for i, (image, title) in enumerate(zip(color_spaces, titles), 1):
    plt.subplot(3, 3, i)
    if title == 'GRAY':  # 对于灰度图像
        plt.imshow(image, cmap='gray')  # 使用灰度 colormap
    else:
        plt.imshow(image)  # 其他图像正常显示
    plt.title(title)
    plt.axis("off")

plt.tight_layout()
plt.show()
