import cv2
import matplotlib.pyplot as plt

# 读取图像
img = cv2.imread("../../img/LinYunEr.jpg")

# 创建一个与原图相同的图像，用于显示修改前的图像
original_img = img.copy()

h,w,channel=img.shape
print(h,w)
#根据尺寸修改一个区域
img[h//2-20:h//2+20, w//2-20:w//2+20] = [100, 100, 100]
imagefiles=[original_img,img]
images=[cv2.cvtColor(image,cv2.COLOR_BGR2RGB) for image in imagefiles]
titles=["origin","edit"]
for i,(title,image) in enumerate(zip(titles,images),1):
    plt.subplot(1,2,i)
    plt.imshow(image)
    plt.title(title)
    plt.axis('off')

# 显示图像
plt.show()
