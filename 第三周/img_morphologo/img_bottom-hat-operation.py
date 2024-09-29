#用图像闭运算操作减去原始图像后的结果，从而获取图像内部的小孔或前景色
import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("../../img/img_top_and_bottom-hat-operation.png")
kernel=np.ones((10,10),np.uint8)
img_top_hat_operation=cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
titles=["img_oridinal","after top hat operation"]
imgs=[img,img_top_hat_operation]

for i,(image,title) in enumerate(zip(imgs,titles)):
    plt.subplot(1,2,i+1)
    plt.imshow(image,"gray")
    plt.title(title)
    plt.axis('off')
plt.show()
