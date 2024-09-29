#图像开运算是图像依次经过腐蚀、膨胀处理的过程，图像被腐蚀后将去除噪声，
# 但同时也压缩了图像，接着对腐蚀过的图像进行膨胀处理，
# 可以在保留原有图像的基础上去除噪声
import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("../../img/img_open-operation.png")
kernel=np.ones((10,10),np.uint8)
img_open_operation=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
titles=["img_original","after open operation"]
imgs=[img,img_open_operation]

for i,(image,title) in enumerate(zip(imgs,titles)):
    plt.subplot(1,2,i+1)
    plt.imshow(image,"gray")
    plt.title(title)
    plt.axis('off')
plt.show()
