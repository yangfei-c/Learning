import cv2
import numpy as np
import matplotlib.pyplot as plt

img1=cv2.imread("../../img/ChenYao.jpg")
img2=cv2.imread("../../img/ChenYao3.webp")
img2=cv2.resize(img2,(img1.shape[1],img1.shape[0]))

face=np.ones((150,150,3))
cv2.imshow("Chen Yao",img1)
face=img2[100:400,100:400]
img1[100:400,100:400]=face
cv2.imshow("result",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()