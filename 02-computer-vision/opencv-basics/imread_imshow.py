import cv2
import numpy as np
import matplotlib.pyplot as plt

# 图像文件路径和对应的标题
image_files = ["../img/ChenYao.jpg", "../img/LinYunEr.jpg", "../img/ZhaoJinMai2.webp", "../img/ChenYao3.webp"]
titles = ['ChenYao', 'LinYunEr', 'ZhaoJinMai', 'ChenYao3']

# 读取和转换图像
images = [cv2.cvtColor(cv2.imread(img_file), cv2.COLOR_BGR2RGB) for img_file in image_files]

# 显示图像
for i, (title, image) in enumerate(zip(titles, images),1):
    #opencv读取默认为BGR与很多其它库默认RGB不一样
    plt.subplot(2, 2, i)#2行2列索引从1开始
    plt.imshow(image)
    plt.title(title)
    plt.xticks([])#隐藏x刻度
    plt.yticks([])

plt.show()
