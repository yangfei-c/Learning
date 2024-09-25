import cv2
import numpy as np
img=np.zeros((256,256,3),np.uint8)
cv2.line(img,(0,0),(256,256),(155,115,155),5,cv2.LINE_4)
cv2.imshow("line",img)
cv2.waitKey(0)
cv2.destroyAllWindows()