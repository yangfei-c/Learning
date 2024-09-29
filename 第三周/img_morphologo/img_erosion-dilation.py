#图像被腐蚀处理后，它将去除噪声，但同时会压缩图像，
# 而图像膨胀操作可以去除噪声并保持原有形状
import cv2
import matplotlib.pyplot as plt
import numpy as np
img=cv2.imread("../../img/img_erosion-dilation.png")
kernel=np.ones((5,5),np.uint8)

erosion=cv2.erode(img,kernel)
dilation=cv2.dilate(erosion,kernel)

titles=["img_oridinal","img_erosion","img_erode"]
imgs=[img,erosion,dilation]

for i,(image,title) in enumerate(zip(imgs,titles)):
    plt.subplot(1,3,i+1)
    plt.imshow(image,"gray")
    plt.title(title)
    plt.axis('off')
plt.show()
