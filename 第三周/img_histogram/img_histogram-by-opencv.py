'''
直方图被广泛应用于计算机视觉领域，在使用边缘和颜色确定物体边界时，
通过直方图能更好地选择边界阈值，进行阈值化处理。同时，直方图对物体与背
景有较强对比的景物的分割特别有用，可以应用于检测视频中场景的变换及图像
中的兴趣点
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
#读取图像
src = cv2.imread("../../img/lena.jpg")
#转换为 RGB 图像
img_rgb = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
#计算直方图
histb = cv2.calcHist([src], [0], None, [256], [0,255])
histg = cv2.calcHist([src], [1], None, [256], [0,255])
histr = cv2.calcHist([src], [2], None, [256], [0,255])
#设置字体
matplotlib.rcParams['font.sans-serif']=['SimHei']
#显示原始图像和绘制的直方图
plt.subplot(121)
plt.imshow(img_rgb, 'gray')
plt.axis('off')
plt.title("(a)Lena 原始图像")
plt.subplot(122)
plt.plot(histb, color='b')
plt.plot(histg, color='g')
plt.plot(histr, color='r')
plt.xlabel("x")
plt.ylabel("y")
plt.title("(b)直方图曲线")
plt.show()