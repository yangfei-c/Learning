import numpy as np
import cv2
import matplotlib.pyplot as plt

img1=cv2.imread("../../img/ChenYao.jpg")
img2=cv2.imread("../../img/ChenYao3.webp")
img2=cv2.resize(img2,(img1.shape[1],img1.shape[0]))
if img1 is None or img2 is None:
    print("读取错误")
else:
    result=cv2.addWeighted(img1,0.5,img2,1,0)
    imgs=[img1,img2,result]
    titles=["img1","img2","after fusion"]
    for i,(title,img) in enumerate(zip(titles,imgs),1):
        img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        plt.subplot(1,3,i)
        plt.imshow(img_rgb)
        plt.title(title)
        plt.axis("off")
    plt.show()
