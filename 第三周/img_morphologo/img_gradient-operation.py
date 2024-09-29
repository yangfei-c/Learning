#图像梯度运算是图像膨胀处理减去图像腐蚀处理后的结果，
# 从而得到图像的轮廓
import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("../../img/img_gradient-operation.png")
kernel=np.ones((10,10),np.uint8)
img_gradient_operation=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
titles=["img_original","after gradient operation"]
imgs=[img,img_gradient_operation]

for i,(image,title) in enumerate(zip(imgs,titles)):
    plt.subplot(1,2,i+1)
    plt.imshow(image,"gray")
    plt.title(title)
    plt.axis('off')
plt.show()
