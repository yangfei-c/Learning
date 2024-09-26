import cv2
import numpy as np
img=cv2.imread("../../img/ChenYao.jpg")
if img is None:
    print("Error: Unable to read the image. Check the file path.")
    exit()
h,w=img.shape[:2]
img1=np.ones(img.shape,dtype="uint8")*50
result=cv2.subtract(img,img1)
cv2.imshow("original",cv2.resize(img,(h//2,w//2)))
cv2.imshow("result",cv2.resize(result,(h//2,w//2)))
cv2.waitKey(0)
cv2.destroyAllWindows()