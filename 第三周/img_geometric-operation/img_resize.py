import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("../../img/ChenYao3.webp")
if img is None:
    print("未选取到图片，请检查路径从式")
else:
    img_RGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    h,w=img_RGB.shape[:2]
    img_resize1=cv2.resize(img_RGB,None,fx=0.5,fy=0.3)
    img_resize2=cv2.resize(img_RGB,(int(w*0.6),int(h*0.3)))
    img_resize3=cv2.resize(img_RGB,(200,100))
    imgs=[img_RGB,img_resize1,img_resize2,img_resize3]
    titls=["img","img_resize1","img_resize2","img_resize3"]
    for i,(image,title) in enumerate(zip(imgs,titls),1):
        plt.subplot(2,2,i)
        plt.title(title)
        plt.imshow(image,'gray')
    plt.show()