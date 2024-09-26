import cv2
import numpy as np
img=cv2.imread("../../img/ChenYao.jpg")
print(type(img))
print(img.item(78,80,1))
img.itemset((78,80,1),255)
cv2.imshow("test",img)
cv2.waitKey(0)