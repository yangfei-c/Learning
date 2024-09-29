#原始图像减去图像开运算后的结果，常用于解决由于光照不均匀图像分割出错的问题中黑点，
# 也常用于解决由于光照不均匀图像分割出错的问题
import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("../../img/img_top_and_bottom-hat-operation.png")
kernel=np.ones((10,10),np.uint8)
img_bottom_hat_operation=cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)
titles=["img_original","after bottom hat operation"]
imgs=[img,img_bottom_hat_operation]

for i,(image,title) in enumerate(zip(imgs,titles)):
    plt.subplot(1,2,i+1)
    plt.imshow(image,"gray")
    plt.title(title)
    plt.axis('off')
plt.show()
