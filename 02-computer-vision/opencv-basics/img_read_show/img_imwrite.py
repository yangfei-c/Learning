import cv2
import numpy as np
img=cv2.imread("../../img/ChenYao.jpg")
cv2.imshow("Chenyao",img)
cv2.imwrite("../img_read_show_images/save1.webp", img, [int(cv2.IMWRITE_WEBP_QUALITY), 0])
cv2.imwrite("../img_read_show_images/save2.webp", img, [int(cv2.IMWRITE_WEBP_QUALITY), 100])
cv2.imwrite("../img_read_show_images/save3.png", img, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])
cv2.waitKey(0)
cv2.destroyAllWindows()
