import cv2
import numpy as np

img=cv2.imread("../../img/ChenYao3.webp")

h,w=img.shape[:2]
matrix=cv2.getRotationMatrix2D((w//2,h//2),30,1)
img_rotate=cv2.warpAffine(img,matrix,(w,h))
cv2.imshow("img_original",img)
cv2.imshow("img_rotate",img_rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()