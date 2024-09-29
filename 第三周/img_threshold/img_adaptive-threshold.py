import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

img=cv2.imread("../../img/ZhaoJinMai2.webp")
img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_mean_thresh=cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
img_gaussian_thresh=cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
matplotlib.rcParams['font.sans-serif']=['SimHei']
titles=["img_rgb","img_gray","img_mean","img_gaussian"]
imgs=[img_rgb,img_gray,img_mean_thresh,img_gaussian_thresh]
for i,(image,title) in enumerate(zip(imgs,titles)):
    plt.subplot(2,2,i+1)
    plt.title(title)
    plt.imshow(image,'gray')
    plt.axis('off')
plt.show()
