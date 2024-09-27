import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("../../img/ChenYao3.webp")
if img is None:
    print("未选取到图片，请检查路径从式")
else:
    img_RGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    h,w=img_RGB.shape[:2]
    matrixs=[np.float32([[1,0,0],[0,1,-100]]),
            np.float32([[1,0,0],[0,1,100]]),
            np.float32([[1,0,100],[0,1,0]]),
            np.float32([[1,0,-100],[0,1,0]])]
    imgs=[cv2.warpAffine(img_RGB,matrix,(w,h)) for matrix in matrixs]
    titls=["img_up","img_down","img_right","img_left"]
    for i,(image,title) in enumerate(zip(imgs,titls),1):
        plt.subplot(2,2,i)
        plt.title(title)
        plt.imshow(image,'gray')
    plt.show()