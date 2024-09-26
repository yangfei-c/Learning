#两个图片之间做与运算可以对图像进行区域选取
import cv2
import numpy as np

#第二个参数将图像读取为灰度图像
img=cv2.imread("../../img/ChenYao.jpg",cv2.IMREAD_GRAYSCALE)
if img is None:
    print("Error: Unable to read the image. Check the file path.")
    exit()

h,w=img.shape[:2]
print(h,w)
circleimg=np.zeros((h,w),dtype="uint8")
circle=cv2.circle(circleimg,(w//2,h//2),200,255,-1)
#在这里x从左到右y从上到下

result=cv2.bitwise_and(img,circleimg)

cv2.imshow("original",img)
cv2.imshow("circle",circle)
cv2.imshow("result",result)
cv2.waitKey(0)
cv2.destroyAllWindows()