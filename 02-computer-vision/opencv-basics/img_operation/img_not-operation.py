#黑变白白变黑
import cv2

#第二个参数将图像读取为灰度图像
img=cv2.imread("../../img/ChenYao.jpg",cv2.IMREAD_GRAYSCALE)
if img is None:
    print("Error: Unable to read the image. Check the file path.")
    exit()

h,w=img.shape[:2]
print(h,w)

result=cv2.bitwise_not(img)

cv2.imshow("original",img)
cv2.imshow("result",result)
cv2.waitKey(0)
cv2.destroyAllWindows()