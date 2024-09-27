import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
img = cv2.imread("../../img/ChenYao3.webp")
if img is None:
    print("输入图像不存在，请检查路径")
else:
    h, w = img.shape[:2]

    # 定义量化级别的函数
    def quantize_image(img, levels):
        step = 256 // levels  # 计算每个量化级别的步长

        #这一句真特么重要
        quantized_img = (img // step) * step  # 矢量化处理，避免循环

        #clip()限制一个数组里面值再指定范围之内
        return np.clip(quantized_img, 0, 255).astype(np.uint8)  # 确保值在 0-255 之间

    # 量化图像
    imgs=[quantize_image(img,i) for i in [2,4,8]]
    # 用来正常显示中文标签
    plt.rcParams['font.sans-serif'] = ['SimHei']
    imgs.insert(0,img)
    # 显示图像
    titles = ['(a) 原始图像', '(b) 量化-L2', '(c) 量化-L4', '(d) 量化-L8']
    for i,(title,image) in enumerate(zip(titles,imgs),1) :
        plt.subplot(2, 2, i)
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # 转换为 RGB 格式
        plt.title(title)
        plt.xticks([]), plt.yticks([])

    plt.show()
