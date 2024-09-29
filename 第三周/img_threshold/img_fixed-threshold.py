#对于图像分割提取轮廓很有用
import cv2
import matplotlib.pyplot as plt

img=cv2.imread("../../img/LinYunEr.jpg")
img0=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_gray=cv2.cvtColor(img0,cv2.COLOR_BGR2GRAY)
threshes=[cv2.THRESH_BINARY,cv2.THRESH_BINARY_INV,cv2.THRESH_TRUNC,cv2.THRESH_TOZERO,cv2.THRESH_TOZERO_INV]
titles=["img_origin","img_gray","BINARY","INV","TRUNC","TOZERO","TOZERO_INV"]
imgs=[cv2.threshold(img_gray,127,255,thresh)[1] for thresh in threshes]
imgs.insert(0,img0)
imgs.insert(1,img_gray)
for i,(image,title) in enumerate(zip(imgs,titles),1):
    plt.subplot(3,3,i)
    plt.imshow(image,'gray')#matplotlib默认将图像视为三通道
    plt.title(title)
    plt.axis('off')
plt.show()