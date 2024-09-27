import cv2
import matplotlib.pyplot as plt

img=cv2.imread("../../img/ChenYao3.webp")
if img is None:
    print("未选取到图片，请检查路径从式")
else:
    img_RGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    h,w=img_RGB.shape[:2]
    imgs=[cv2.flip(img_RGB,i) for i in [0,1,-1]]
    imgs.append(img_RGB)
    titls=["img_mirror-x","img_mirror-y","img_mirror-xy","img_origindal"]
    for i,(image,title) in enumerate(zip(imgs,titls),1):
        plt.subplot(2,2,i)
        plt.title(title)
        plt.imshow(image)
        plt.axis("off")
    plt.show()